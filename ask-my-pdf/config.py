import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
model = "gpt-4"
if not API_KEY or API_KEY == "":
    raise ValueError("OPENAI_API_KEY not found or not set. Please get a key from https://aistudio.google.com/app/apikey and set it in the .env file.")

PDF_DIRS = "PDFs"
VECTOR_STORE_DIR = "vector_store"
COLLECTION_NAME = "ask-my-invoices"

os.makedirs(PDF_DIRS, exist_ok=True)
os.makedirs(VECTOR_STORE_DIR, exist_ok=True)