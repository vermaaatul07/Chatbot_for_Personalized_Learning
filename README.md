Chatbot for Personalized Learning
An AI-powered educational assistant that provides personalized content and video recommendations to enhance the learning experience.
Features

Smart Content Generation: Leverages Hugging Face's google/flan-t5-large model for detailed responses
Video Learning: Integrates YouTube API for topic-specific video recommendations
Intelligent Conversations: Uses advanced NLU for context-aware interactions
LMS Integration: Seamlessly connects with educational repositories

Tech Stack

Core: Python, RASA
ML Model: Hugging Face Transformers (google/flan-t5-large)
API: YouTube Data API v3
Deployment: Streamlit
Development: Visual Studio Code

Installation
Prerequisites

Python 3.8+
Virtual Environment
YouTube Data API key

Setup
bashCopy# Clone repository
git clone https://github.com/vermaaatul07/Chatbot_for_Personalized_Learning.git
cd Chatbot-for-Personalized-Learning

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API key
echo "YOUTUBE_API_KEY=your_key_here" > .env

# Train RASA model
rasa train
🚀 Deployment {#deployment}
Local Development
bashCopy# Install Streamlit
pip install streamlit

# Run application
streamlit run app.py
Access at http://localhost:8501
Streamlit Cloud Deployment

Prepare deployment files

bashCopy# Generate requirements
pip freeze > requirements.txt

# Create setup file
cat > setup.sh << EOL
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = \$PORT
enableCORS = false" > ~/.streamlit/config.toml
EOL

Deploy


Visit Streamlit Cloud
Connect your GitHub repository
Configure:

Main file: app.py
Environment variables: YOUTUBE_API_KEY, RASA_API_ENDPOINT



💡 Usage {#usage}

Access the chatbot through your web browser
Enter your learning topic or question
Receive AI-generated explanations and curated video recommendations

🤝 Contributing {#contributing}
Pull requests are welcome! For major changes, please open an issue first to discuss proposed changes.
📝 License {#license}
MIT
