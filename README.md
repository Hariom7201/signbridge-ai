🤝 SignBridge AI

Unified Sign Language Translation Platform

Breaking communication barriers by translating sign language into text and speech using AI — in real time and from videos or images.

🚀 Overview

SignBridge AI is an AI-powered platform that translates sign language gestures into readable captions and audible speech.
It supports live camera input, uploaded videos, and images, all within a single unified web interface.

This project aims to improve accessibility for the deaf and hard-of-hearing community by enabling seamless communication with the hearing world.

🎯 Key Features

✅ Live Camera Sign Translation
✅ Video Upload → Captions + Voice Output
✅ Image Upload → Gesture Recognition
✅ Real-time captions
✅ Text-to-Speech (TTS)
✅ Modular & Scalable Architecture
✅ Web-based (No installation required)

🧠 How It Works (High Level)

User selects an input mode:

Live Camera

Video Upload

Image Upload

Media is processed frame-by-frame using OpenCV

Hand landmarks are extracted using MediaPipe

Gestures are classified using trained ML logic

Output is generated as:

Text captions

Optional voice output (TTS)

Everything runs inside a Streamlit-powered web app

🏗️ System Architecture Diagram

┌──────────────────────────┐
│        User Browser       │
│  (Desktop / Mobile Web)   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│     Streamlit Web UI     │
│  - Mode Selection        │
│  - Video / Image Upload  │
│  - Live Camera Toggle    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   Media Processing Layer │
│  (OpenCV)                │
│  - Frame Extraction      │
│  - Image Preprocessing   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Hand Landmark Detection  │
│  (MediaPipe Hands)       │
│  - Finger Tracking       │
│  - Keypoints Extraction │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Gesture Recognition ML   │
│  - Rule / Model Based    │
│  - Sign Classification  │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Output Generation Layer  │
│  - Text Captions         │
│  - Voice (TTS)           │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  Final Output to User    │
│  - On-screen captions    │
│  - Audio playback        │
└──────────────────────────┘

🗂️ Project Structure

signbridge-ai/
│
├── app.py                  # Main Streamlit app
├── services/
│   ├── camera.py           # Live camera processing
│   ├── video.py            # Video upload processing
│   ├── image.py            # Image processing
│   └── tts.py              # Text-to-speech logic
│
├── models/                 # Gesture models / logic
├── requirements.txt        # Dependencies
├── runtime.txt             # Python runtime version
├── README.md               # Project documentation
└── .gitignore

🛠️ Tech Stack

| Layer            | Technology                |
| ---------------- | ------------------------- |
| Frontend         | Streamlit                 |
| Computer Vision  | OpenCV                    |
| Hand Tracking    | MediaPipe                 |
| Machine Learning | Python                    |
| Text-to-Speech   | pyttsx3                   |
| Deployment       | Streamlit Community Cloud |

🌐 Deployment

The application is deployed using Streamlit Community Cloud.

🔗 Live Demo:
👉 (Add your Streamlit app URL here)

🔐 Environment Variables

Create a .env file (not committed to GitHub):

GEMINI_API_KEY=your_api_key_here

API keys are securely handled and excluded from version control.

🚧 Current Limitations

Live camera disabled on cloud (browser security limitation)

Gesture vocabulary currently limited (extendable)

Model accuracy improves with more training data

🔮 Future Enhancements

✨ Full sentence-level sign recognition
✨ Multilingual speech output
✨ Mobile-optimized UI
✨ User-trained custom gestures
✨ Dedicated backend (FastAPI)
✨ Native Android/iOS apps

🏆 Use Cases

Deaf–hearing communication

Education & classrooms

Public service counters

Online meetings

Accessibility tools

👨‍💻 Team

Hariom Hatwate
B.Tech CSE | AI & ML
Hackathon Finalist 🚀

📜 License

This project is open-source and available under the MIT License.

⭐ Final Note (For Judges)

SignBridge AI is not just a project — it is a step toward inclusive communication powered by AI.