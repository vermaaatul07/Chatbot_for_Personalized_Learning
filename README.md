Chatbot for Personalized Learning
Project Description
The Chatbot for Personalized Learning is an AI-powered assistant designed to enhance the learning experience. Using advanced machine learning models and APIs, the chatbot:

Generates content based on user queries.
Recommends YouTube videos relevant to the topic.
This chatbot aims to make learning interactive, engaging, and tailored to the user's needs.


Features

Content Generation: Utilizes Hugging Face's google/flan-t5-large model for generating detailed and accurate responses to user queries.
Video Recommendations: Integrates YouTube API to provide curated video recommendations based on the user's query.


Outcomes

Personalized Learning: Successfully developed a chatbot that delivers customized educational resources and guidance tailored to individual users' needs.
Seamless LMS Integration: The chatbot interacts with external educational repositories to provide topic-specific content.
NLU-Driven Interactions: Advanced Natural Language Understanding (NLU) techniques enable the chatbot to maintain intelligent and context-aware conversations, ensuring accurate assistance.


Modules Implemented

Intent Recognition and Dialogue Management: The chatbot effectively identifies user intents and maintains coherent, context-aware conversations.
Integration with Educational Repositories and LMS: Connected the chatbot with LMS to access and deliver relevant educational materials seamlessly.
Personalized Content Delivery: Ensured that generated content aligns with user queries, offering accurate and helpful responses.


Tech Stack

Language: Python
Framework: RASA for chatbot development
Machine Learning Model: Hugging Face Transformers (google/flan-t5-large)
APIs: YouTube Data API v3
IDE: Visual Studio Code
Deployment: Streamlit


Setup Instructions
Prerequisites

Python 3.8+
Virtual Environment
API Keys:

YouTube Data API key



Installation Steps

Clone the repository:
bashCopygit clone https://github.com/vermaaatul07/Chatbot_for_Personalized_Learning.git
cd Chatbot-for-Personalized-Learning

Create and activate a virtual environment:
bashCopypython -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies:
bashCopypip install -r requirements.txt

Set up your API keys:

Create a .env file in the root directory and add your YouTube API key:
envCopyYOUTUBE_API_KEY=your_key_here



Train the RASA model:
bashCopyrasa train



Deployment with Streamlit
Local Deployment

Install Streamlit:
bashCopypip install streamlit

Run the Streamlit app:
bashCopystreamlit run app.py

Access the application at http://localhost:8501

Cloud Deployment

Create a requirements.txt file:
bashCopypip freeze > requirements.txt

Create a setup.sh file with the following content:
bashCopymkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml

Deploy to Streamlit Cloud:

Login to Streamlit Cloud
Connect your GitHub repository
Select the repository and branch
Specify the main file as app.py
Deploy the application



Environment Variables
Set the following environment variables in Streamlit Cloud:

YOUTUBE_API_KEY
RASA_API_ENDPOINT


Usage

Ask a Question:

Access the Streamlit interface through your web browser
Type a topic or question in the input field


Receive Content:

The chatbot generates detailed information using the google/flan-t5-large model


Watch Recommended Videos:

The chatbot provides relevant YouTube videos
Click on the video links to watch them directly
