# Chatbot for Personalized Learning

## Project Description

The **Chatbot for Personalized Learning** is an AI-powered assistant designed to enhance the learning experience. Using advanced machine learning models and APIs, the chatbot:

1. Generates content based on user queries.
2. Recommends YouTube videos relevant to the topic.

This chatbot aims to make learning interactive, engaging, and tailored to the user's needs.

---

## Features

- **Content Generation:** Utilizes Hugging Face's google/flan-t5-large model for generating detailed and accurate responses to user queries.
- **Video Recommendations:** Integrates YouTube API to provide curated video recommendations based on the user's query.

---

## Outcomes

- **Personalized Learning:** Successfully developed a chatbot that delivers customized educational resources and guidance tailored to individual users' needs.
- **Seamless LMS Integration:** The chatbot interacts with external educational repositories to provide topic-specific content.
- **NLU-Driven Interactions:** Advanced Natural Language Understanding (NLU) techniques enable the chatbot to maintain intelligent and context-aware conversations, ensuring accurate assistance.

---

## Modules Implemented

1. **Intent Recognition and Dialogue Management:** The chatbot effectively identifies user intents and maintains coherent, context-aware conversations.
2. **Integration with Educational Repositories and LMS:** Connected the chatbot with LMS to access and deliver relevant educational materials seamlessly.
3. **Personalized Content Delivery:** Ensured that generated content aligns with user queries, offering accurate and helpful responses.

---

## Tech Stack

- **Language:** Python
- **Framework:** RASA for chatbot development
- **Machine Learning Model:** Hugging Face Transformers (google/flan-t5-large)
- **APIs:** YouTube Data API v3
- **IDE:** Visual Studio Code

---

## Setup Instructions

### Prerequisites

1. **Python 3.8+**
2. **Virtual Environment**
3. **API Keys:**
   - YouTube Data API key

### Installation Steps

1. Clone the repository:

   
bash
   git clone https://github.com/vermaaatul07/Chatbot_for_Personalized_Learning.git
   cd Chatbot-for-Personalized-Learning


2. Create and activate a virtual environment:

   
bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate


3. Install dependencies:

   
bash
   pip install -r requirements.txt


4. Set up your API keys:

   - Create a .env file in the root directory and add your YouTube API key:
     
env
     YOUTUBE_API_KEY=your_key_here


5. Train the RASA model:

   
bash
   rasa train


6. Run the chatbot:

   
bash
   rasa run actions & rasa shell


---

## Usage

1. **Ask a Question:**

   - Start the chatbot and type a topic or question.

2. **Receive Content:**

   - The chatbot generates detailed information using the google/flan-t5-large model.

3. **Watch Recommended Videos:**

   - The chatbot provides a couple of relevant YouTube videos.
   - Respond "yes" to receive the links.
