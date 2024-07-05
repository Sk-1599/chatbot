# AI Chatbot Using YouTube and Google Drive as Knowledge Base

This project is a generative AI chatbot that uses YouTube videos and Google Drive documents as its knowledge base. The chatbot integrates with various APIs to fetch and process data, and uses OpenAI's GPT model to generate responses based on the fetched content.

## Project Structure

chatbot_project/
├── app.py
├── chatbot.py
├── config.py
├── drive_service.py
├── openai_service.py
├── youtube_service.py
└── README.md


### Files

- **app.py**: Flask web application to serve the chatbot.
- **chatbot.py**: Main logic to combine YouTube and Google Drive content and generate responses.
- **config.py**: Configuration file to store API keys and credentials.
- **drive_service.py**: Handles Google Drive API interactions.
- **openai_service.py**: Handles interactions with the OpenAI API.
- **youtube_service.py**: Handles YouTube API interactions.

## Prerequisites

- Python 3.7+
- Google Cloud Project with YouTube Data API v3 enabled
- Google Cloud Project with Google Drive API enabled
- OpenAI account and API key

## Setup

### 1. Install Required Packages

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib pytube youtube-transcript-api openai flask

```

2. Obtain API Keys and Credentials

YouTube API Key
1. Go to the Google Cloud Console(I prefer GCP you can use any AWS,Azure).
2. Create a new project.
3. Enable the YouTube Data API v3.
4. Create API credentials and get your API key.

Google Drive Credentials JSON
1. Go to the Google Cloud Console.
2. Create a new project.
3. Enable the Google Drive API.
4. Create a service account and generate a JSON key file.

OpenAI API Key
1. Go to the OpenAI website.
2. Sign up for an account.
3. Create an API key.


3. Configure the Project
Replace the placeholders in config.py with your actual API keys and credentials.

# config.py
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'
DRIVE_CREDENTIALS_JSON = 'path/to/your/credentials.json'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

Running the Project
Navigate to the project directory.

Start the Flask application:

python app.py

The server should be running on http://127.0.0.1:5000/.

