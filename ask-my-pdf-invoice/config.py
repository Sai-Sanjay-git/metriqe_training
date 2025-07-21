import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key or api_key == "":
    raise ValueError ("Google api key is not found")

PDFS_DIR = "PDFs"
VECTOR_STORE_DIR = "vector_store"
COLLECTION_NAME = "ask_my_pdf_invoices"

os.makedirs(PDFS_DIR,exist_ok=True)
os.makedirs(VECTOR_STORE_DIR,exist_ok=True)