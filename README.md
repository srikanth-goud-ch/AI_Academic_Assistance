📘 AI Academic Assistant (RAG-Based Chatbot)

An intelligent AI-powered academic assistant built using Retrieval-Augmented Generation (RAG) that helps students interact with academic content like PDFs, notes, and study materials in a conversational way.

This system allows users to upload documents and ask questions, and the chatbot responds with context-aware, accurate answers along with source references.

🚀 Key Features
📄 Document Upload (PDF Support)
Upload academic materials and instantly make them searchable.
🤖 Context-Aware Chatbot
Uses RAG to generate answers strictly based on uploaded content.
🔍 Semantic Search (Vector DB)
Retrieves the most relevant document chunks using embeddings.
📚 Source Attribution
Displays sources used to generate answers for transparency.
⚡ Fast API Backend
Built with FastAPI for high performance and scalability.
🧠 LLM Integration (Groq + LLaMA3)
Generates intelligent and natural responses.
🎯 Extensible Filters (Course / Year)
Ready for structured academic filtering.
🌐 Modern Frontend (React + Vite)
Simple and responsive chat interface.
🏗️ Tech Stack

Backend:

FastAPI
LangChain
ChromaDB (Vector Store)
Hugging Face Embeddings
Groq API (LLaMA3)

Frontend:

React (Vite)
Axios
🧠 How It Works
User uploads a PDF document
Text is extracted and split into chunks
Chunks are converted into embeddings
Stored in ChromaDB vector database
User asks a question
Relevant chunks are retrieved via similarity search
LLM generates an answer using retrieved context
Response is returned with sources
📂 Project Structure
backend/ → FastAPI + RAG pipeline
frontend/ → React chat interface
▶️ Getting Started
Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
Frontend
cd frontend
npm install
npm run dev
🔥 Future Improvements
Chat memory (conversation context)
Advanced filtering (course, semester, subject)
Reranking for better accuracy
Authentication system
UI enhancements (Tailwind dashboard)
Docker deployment
🎯 Use Cases
College/University digital assistants
Study material Q&A systems
Exam preparation tools
Institutional knowledge bots
🤝 Contributing

Contributions, issues, and feature requests are welcome!
