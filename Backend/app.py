# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from langchain.chains import RetrievalQA
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import os
# from scraper import scrape_website
# from processor import process_and_embed

# load_dotenv()
# OCCAMS_ADVISORY_URL = os.getenv("OCCAMS_ADVISORY_URL", "https://www.occamsadvisory.com/")
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Ensure you have your Google API key in .env


# app = FastAPI()
# vector_store = None


# @app.on_event("startup")
# async def startup_event():
#     global vector_store
#     print("Loading website content...")
#     website_content = scrape_website(OCCAMS_ADVISORY_URL)
#     if website_content:
#         print("Website content loaded")
#         print("Processing and embedding...")
#         vector_store = process_and_embed(website_content)
#         if vector_store:
#             print("Embeddings created.")
#         else:
#             print("Failed to create embeddings during startup.")
#     else:
#         print("Failed to load website content during startup.")


# class Query(BaseModel):
#     query: str


# @app.post("/ask/")
# async def ask_question(query_data: Query):
#     global vector_store
#     if vector_store is None:
#         raise HTTPException(status_code=500, detail="Vector store not initialized.")

#     if not GOOGLE_API_KEY:
#         raise HTTPException(
#             status_code=500, detail="Google API key not found. Please set it in your .env file."
#         )

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-pro", google_api_key=GOOGLE_API_KEY
#     )  # Initialize Gemini
#     qa_chain = RetrievalQA.from_llm(
#         llm, vector_store.as_retriever(search_kwargs={"k": 3}), return_source_documents=False
#     )

#     try:
#         result = await qa_chain({"query": query_data.query})
#         return {"answer": result["result"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error processing query: {e}")


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from scraper import scrape_website
from processor import process_and_embed
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware

load_dotenv()
OCCAMS_ADVISORY_URL = os.getenv("OCCAMS_ADVISORY_URL", "https://www.occamsadvisory.com/")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Ensure you have your Google API key in .env

app = FastAPI()

# Add CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # Allow requests from your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (including POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

vector_store = None


@app.on_event("startup")
async def startup_event():
    global vector_store
    print("Loading website content...")
    website_content = scrape_website(OCCAMS_ADVISORY_URL)
    if website_content:
        print("Website content loaded")
        print("Processing and embedding...")
        vector_store = process_and_embed(website_content)
        if vector_store:
            print("Embeddings created.")
        else:
            print("Failed to create embeddings during startup.")
    else:
        print("Failed to load website content during startup.")


class Query(BaseModel):
    query: str


@app.post("/ask/")
async def ask_question(query_data: Query):
    global vector_store
    if vector_store is None:
        raise HTTPException(status_code=500, detail="Vector store not initialized.")

    if not GOOGLE_API_KEY:
        raise HTTPException(
            status_code=500, detail="Google API key not found. Please set it in your .env file."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro", google_api_key=GOOGLE_API_KEY
    )  # Initialize Gemini
    qa_chain = RetrievalQA.from_llm(
        llm, vector_store.as_retriever(search_kwargs={"k": 3}), return_source_documents=False
    )

    try:
        result = await qa_chain({"query": query_data.query})
        return {"answer": result["result"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)