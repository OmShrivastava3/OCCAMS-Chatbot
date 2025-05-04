from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_community.vectorstores import Chroma  # Updated import
from dotenv import load_dotenv
import os

load_dotenv()
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "all-mpnet-base-v2")  # Default Sentence Transformer model


def process_and_embed(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME
    )  # Initialize embedding model
    db = Chroma.from_texts(chunks, embeddings)
    return db


if __name__ == "__main__":
    dummy_text = (
        "This is some sample content about Occams Advisory. They offer various services and have a team of experts. "
        "Their mission is to help clients succeed." * 5
    )
    vector_store = process_and_embed(dummy_text)
    if vector_store:
        print("Text processed and embeddings created in ChromaDB.")
        retriever = vector_store.as_retriever(search_kwargs={"k": 3})
        query = "What services does Occams Advisory offer?"
        docs = retriever.get_relevant_documents(query)
        print("Retrieved documents:", docs)
    else:
        print("Failed to process and embed text.")