# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk import Tracker
import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

logger = logging.getLogger(__name__)

class ActionGenerateContent(Action):
    def __init__(self):
        self.model_name = "google/flan-t5-large"
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            logger.info(f"Model {self.model_name} loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            self.model = None
            self.tokenizer = None

    def name(self) -> Text:
        return "action_generate_content"

    def generate_prompt(self, topic: str) -> str:
        return f"""Generate a detailed and educational explanation about {topic}.
        Include:
        - Definition and key concepts
        - Main principles or components
        - Real-world applications or examples
        - Important facts and developments
        - Current trends or future perspectives
        Make it informative yet easy to understand."""

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        if not self.model or not self.tokenizer:
            dispatcher.utter_message(text="Sorry, I'm having technical difficulties. Please try again later.")
            return []

        topic = next(tracker.get_latest_entity_values("topic"), None)
        if not topic:
            dispatcher.utter_message(text="I couldn't find a topic. Can you please specify what you'd like to learn about?")
            return []
        
        try:
            input_text = self.generate_prompt(topic)
            inputs = self.tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
            
            outputs = self.model.generate(
                inputs.input_ids,
                max_length=512,          # Increased length for more detailed content
                min_length=100,          # Ensure minimum content length
                num_beams=5,            
                temperature=0.7,         # Slightly increased for more creativity
                do_sample=True,
                top_p=0.92,             # Adjusted for better quality
                top_k=50,               # Added top-k sampling
                repetition_penalty=2.5,  # Increased penalty for repetitions
                length_penalty=1.5,      # Encourage longer outputs
                no_repeat_ngram_size=3,  # Prevent 3-gram repetitions
                early_stopping=True
            )
            
            content = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Format the content for better readability
            formatted_content = content.replace(". ", ".\n\n")
            
            dispatcher.utter_message(text=f"Here's a detailed explanation about {topic}:\n\n{formatted_content}")
            logger.info(f"Generated content for topic: {topic}")
            
        except Exception as e:
            logger.error(f"Error generating content: {e}")
            dispatcher.utter_message(text="I apologize, but I couldn't generate the content at this moment.")
        
        return [SlotSet("topic", topic)]
    


class ActionFetchYoutubeVideos(Action):
    def name(self) -> Text:
        return "action_fetch_youtube_videos"
        
    def __init__(self):
        self.youtube = build('youtube', 'v3', developerKey='AIzaSyDFkrvlDdNQd-aRtIq1w5Gh_jIZpDQeRHs')

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            topic = tracker.get_slot("topic")
            if not topic:
                dispatcher.utter_message(text="I need a topic to search for videos.")
                return []

            search_response = self.youtube.search().list(
                q=topic,
                part='snippet',
                maxResults=2,
                type='video'
            ).execute()

            if not search_response.get('items'):
                dispatcher.utter_message(text=f"Sorry, I couldn't find any videos about {topic}")
                return []

            videos = []
            for item in search_response['items']:
                video_id = item['id']['videoId']
                title = item['snippet']['title']
                url = f"https://www.youtube.com/watch?v={video_id}"
                videos.append(f"{title}\n{url}")

            dispatcher.utter_message(text=f"Here are 2 helpful videos about {topic}:\n\n" + "\n\n".join(videos))
            return []  # Return immediately after sending videos

        except HttpError as e:
            dispatcher.utter_message(text="Sorry, I couldn't fetch any videos at the moment.")
            return []  # Return immediately after error
    
class ActionGenerateQuiz(Action):
    def name(self) -> Text:
        return "action_generate_quiz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        topic = tracker.get_slot("topic")
        current_question = tracker.get_slot("current_question") or 0
        
        questions = [
            {
                "question": f"What is the main purpose of {topic}?",
                "answer": "To solve problems",
                "explanation": f"{topic} is primarily used to solve specific problems in its domain."
            },
            {
                "question": f"What are the key components of {topic}?",
                "answer": "Core elements",
                "explanation": f"The key components help structure and organize {topic}."
            },
            {
                "question": f"How is {topic} applied in real-world scenarios?",
                "answer": "Practical applications",
                "explanation": f"{topic} has various practical applications in industry and daily life."
            }
        ]
        
        if current_question < len(questions):
            dispatcher.utter_message(text=questions[current_question]["question"])
            return [SlotSet("current_question", current_question + 1),
                   SlotSet("correct_answer", questions[current_question]["answer"]),
                   SlotSet("explanation", questions[current_question]["explanation"])]
        
        return [SlotSet("current_question", 0)]

class ActionValidateAnswer(Action):
    def name(self) -> Text:  
        return "action_validate_answer"    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_answer = tracker.latest_message.get("text", "").lower()
        correct_answer = tracker.get_slot("correct_answer").lower()
        explanation = tracker.get_slot("explanation")
        current_question = tracker.get_slot("current_question")
        
        # Clean up user answer
        user_answer = user_answer.replace("the answer is", "").strip()
        user_answer = user_answer.replace("i think", "").strip()
        
        # Check if answer contains key components
        if any(word in user_answer for word in correct_answer.split()):
            dispatcher.utter_message(text="That's correct! 🎉")
        else:
            dispatcher.utter_message(text=f"Not quite right. The correct answer is: {correct_answer}\nExplanation: {explanation}")
        
        if current_question >= 2:
            dispatcher.utter_message(text="Quiz completed! You've answered 2 questions.")
            return [SlotSet("current_question", 0)]
        
        return []