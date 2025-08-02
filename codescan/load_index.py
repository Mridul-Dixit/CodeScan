from codescan.loader import load_repo, load_documents_from_repo
from codescan.helper import split_documents, load_embeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
import os
import shutil

load_dotenv()

def clear_vector_store():
    """
    Clear the existing vector store by removing the persistence directory.
    """
    persistence_directory = "./db"
    if os.path.exists(persistence_directory):
        shutil.rmtree(persistence_directory)
        print(f"Cleared vector store at {persistence_directory}")
    else:
        print("No existing vector store to clear.")

def main(repo_url, repo_path="./repo"):
    """
    Main function to load a Git repository, split documents, and load embeddings.

    :param repo_path: Path to the Git repository.
    """
    try:
        clear_vector_store()  # Clear existing vector store if any
        repo = load_repo(repo_url, repo_path)
        documents = load_documents_from_repo(repo_path)
        chunks = split_documents(documents)
        embeddings = load_embeddings()
        vector_store = Chroma.from_documents(chunks, embeddings, persist_directory="./db")
        vector_store.persist()  
        return vector_store

    except RuntimeError as e:
        print(f"Error: {e}")