**1. Occams Advisory Chatbot**
This chatbot answers user queries about Occams Advisory, using information from their website.

**2. Core Functionality**
Website Scraping.
Information Retrieval.
Question Answering (using Google Gemini)
Basic User Interface

**3. Technical Architecture**
Frontend: HTML, JavaScript
Backend: Python (FastAPI)

**4. Setup and Installation**

Prerequisites:
Python (3.7+)
Node.js
Google API Key

**Installation Steps**
Clone (if applicable): git clone <repository_url>

Backend:

cd backend

python -m venv venv

venv\Scripts\activate (Windows) / source venv/bin/activate (macOS/Linux)

pip install fastapi uvicorn python-dotenv beautifulsoup4 requests  langchain-core langchain-community langchain-huggingface  langchain-google-genai

Frontend:

cd frontend

npm install (if applicable)

**5. Configuration**
Create .env in backend directory.

Add Google API Key:  GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

**6. Running the Application**
Starting the Backend
cd backend

Activate venv (if used)

uvicorn app:app --reload

Starting the Frontend
cd frontend

node server.js

Accessing the Chatbot
Open browser to http://localhost:3001.

**7. Code Structure**
Backend (/backend)
app.py: FastAPI application

processor.py: Text processing, embeddings

scraper.py: Website scraping

.env: Environment variables

Frontend (/frontend)
server.js: (Optional) Express server

public/index.html: Chatbot interface

**8. Dependencies**
Backend (Python): fastapi, uvicorn, python-dotenv, beautifulsoup4, requests,  langchain-core, langchain-community, langchain-huggingface, langchain-google-genai

Frontend (Node.js): express

**9. Key Implementation Details**
Web Scraping: requests, Beautiful Soup

Text Processing: Langchain

Embeddings: HuggingFace Sentence Transformer

Vector Store: Chroma

LLM: Google Gemini

CORS: CORSMiddleware

**10. Troubleshooting**
Backend: Check terminal output for errors.  Common errors:

500:  Check API key, scraping, LLM.

405:  Check CORS configuration in app.py.

NameResolutionError: Check internet, DNS, URL.

Frontend: Check browser console and network tab.  Common errors:

"Failed to fetch": Check backend, URL, headers.

**11. Further Improvements**
Improved scraping, prompting, UI.

Chat history, error handling, logging, testing, security.

**12. License**
Specify License.
