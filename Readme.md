# 🤖 Aivora — AI Assistant

> A modern AI-powered conversational assistant built with Python, Flask, Groq API, HTML, Tailwind CSS, and JavaScript.

Aivora is a web-based AI assistant designed to provide an interactive and user-friendly conversational experience. It uses a Flask backend to communicate with the Groq API and a modern frontend to provide a smooth chat interface.

---

## Deployment

Aivora is live at - https://aivora-2.onrender.com/

---

## ✨ Features

- 💬 Interactive AI conversation
- 🤖 Powered by Groq API
- 🧠 Maintains conversation context during the session
- 🌐 Modern and responsive web interface
- 🌙 Dark / Light mode
- ⌨️ Enter-to-send messaging
- ⏳ AI typing indicator
- 📋 Copy AI responses
- 🗑️ Clear conversation
- 📱 Responsive design for different screen sizes
- 🔐 Secure API key management using environment variables
- ⚡ Fast AI responses through Groq

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- Tailwind CSS
- JavaScript
- Font Awesome

### Backend
- Python
- Flask
- 

### AI
- Groq API
- `openai/gpt-oss-20b`

### Development & Deployment
- Python Virtual Environment
- python-dotenv
- Gunicorn
- Git
- GitHub
- Render

---

## Project Structure

AI Assistant/
│
├── main.py              
├── requirements.txt     
├── .gitignore           
├── README.md            
├── templates/
│   └── index.html       
└── .env                 

---
## ⚙️ Getting Started
Follow the steps below to run Aivora locally.
## 1. Clone the repository
git clone https://github.com/Aryan-018008/AIVORA.git

## 2. Move into the project directory:
cd AI Assistant

## 3. Create a virtual environment
python -m venv env

## 4. Activate it on Windows:
env\Scripts\activate

You should see:
(env)

in your terminal.
## 1. Install dependencies
pip install -r requirements.txt

## 2. Configure the API key
Create a file named:
.env

in the project root.
Add:
GROQ_API_KEY=your_groq_api_key

Replace your_groq_api_key with your actual Groq API key.

--- 

## ⚠️ Security
Never commit your .env file to GitHub.
Your .gitignore should contain:
env/
__pycache__/
.env

## ▶️ Run Aivora
Start the Flask application:
## python main.py

You should see something similar to:
* Running on http://127.0.0.1:5000

Open your browser and visit:
http://127.0.0.1:5000

Aivora should now be running locally. 🚀

## 💬 How It Works
When the user sends a message:
User
  ↓
Aivora Frontend
  ↓
JavaScript fetch()
  ↓
Flask /chat endpoint
  ↓
Groq API
  ↓
AI Model
  ↓
Flask
  ↓
Aivora Frontend
  ↓
AI Response




## The conversation messages are maintained by the backend during the application's runtime.
### 🔑 Environment Variables
Variable	Description
GROQ_API_KEY	API key used to access the Groq API


Example:
GROQ_API_KEY=xxxxxxxxxxxxxxxx

## 🚀 Future Enhancements
Aivora is designed to evolve beyond a basic conversational assistant.
Planned improvements include:
- 📚 Retrieval-Augmented Generation (RAG)
- 📄 PDF and document analysis
- 🔍 Semantic search
- 🧠 Vector database integration
- 💾 Persistent conversation history
- 👤 User authentication
- 📂 Document upload
- 📊 Chat history management
- ⚡ Streaming AI responses
- 🧩 Multiple AI models
- ☁️ Cloud deployment
## 🧠 Future RAG Architecture
The planned RAG version of Aivora will follow an architecture similar to:
                 Documents
                    │
                    ▼
              Document Loader
                    │
                    ▼
               Text Splitter
                    │
                    ▼
                Embeddings
                    │
                    ▼
              Vector Database
                    │
                    ▼
User Question ──► Retriever
                    │
                    ▼
              Relevant Context
                    │
                    ▼
                 Groq LLM
                    │
                    ▼
                AI Response




## 🔐 Security Considerations
- Never expose your Groq API key in frontend JavaScript.
- Store API keys in environment variables.
- Never commit .env to GitHub.
- Do not expose secret credentials in source code.
- Use production environment variables when deploying.

---

## 📌 Current Status
🟢 AI Chat Interface       Completed
🟢 Flask Backend           Completed
🟢 Groq Integration        Completed
🟢 Environment Variables   Completed
🟢 Responsive UI           Completed
🟢 Dark Mode               Completed
🟡 RAG Integration         Planned
🟡 Vector Database         Planned
🟡 Document Q&A            Planned

---

## 👨‍💻 Author
Aryan Bharadwaj

---

## 📄 License
This project is created for learning and educational purposes.


