import os
from config import PDFS_DIR, VECTOR_STORE_DIR,COLLECTION_NAME
import chromadb
from llm_utils import embeddings
from langchain_chroma import Chroma
import app
import gradio as gr
import shutil

vector_store_instance = None

def get_pdf_list():
    """return a list of pdf available in the PDFs directory"""
    return [f for f in os.listdir(PDFS_DIR) if f.endswith(".pdf")]

# list vector store

def get_vector_store_instance():
    global vector_store_instance

    if vector_store_instance is None:
        try:
            client = chromadb.PersistentClient(path=VECTOR_STORE_DIR)
            vector_store_instance = Chroma(
                client = client,
                collection_name = COLLECTION_NAME,
                embeddings_function = embeddings)
        except Exception as e :
            print(f"error in getting the vector store :{e}")
            return None
        return vector_store_instance
    

def add_to_vector_store(files):
    """adds new, non duplicate pdfto the vector store.
       checks for existing filenames to prevent duplication
    """

    global vector_store_instance
    new_pdf_paths = []
    skipped_files = []
    for file in files :
        dest_path = os.path.join(PDFS_DIR, os.path.basename(file.name))
        if os.path.exists(dest_path):
            skipped_files.append(os.path.basename(file.name))
            continue
        shutil.copy(file.name,dest_path)
        new_pdf_paths.append(dest_path)

    if not new_pdf_paths:
        status = "status: all files are already available in the knowledge base"
        if skipped_files:
            status += f" skipped : {', '.join(skipped_files)}"
        return status, gr.update(choices=get_pdf_list())

    