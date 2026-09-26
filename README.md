# Jarvis - AI Voice Assistant

A Python-based voice assistant that can listen to voice commands, perform basic tasks, and use Google's Gemini API to answer general questions.

## 🚀 Features

- Voice command recognition
- Text-to-speech responses
- Open websites using voice commands
- Play songs using predefined music links
- Gemini AI integration for general questions
- Environment variables for secure API key management

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- Google Gemini API
- python-dotenv

## 🔐 API Key Setup

Create a `.env` file in the project directory:

GEMINI_API_KEY=your_api_key_here

The `.env` file is excluded from GitHub using `.gitignore`.

## ▶️ How to Run

Install the required packages:

```bash
pip install -r requirements.txt