from openai import OpenAI
import os
import requests
import numpy as np
from dotenv import load_dotenv
import PyPDF2
import faiss
import re
import pickle
import gradio as gr


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
client = OpenAI(api_key=api_key,base_url=base_url)

pdf_path = os.path.join(os.path.dirname(__file__),"Sai Sanjay PoC (Multi-tenant-react-app hosting via CDN).pdf")
vector_path = os.path.join(os.path.dirname(__file__),"vector_store1.pkl")

def read_pdf(pdf_path):
    text =""
    with open (pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader (f)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()
    return text  

def split_text_semanticaly(text, chunk_size = 1000):
    sentences = re.split(r'(?<=[.!?])\s+',text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def get_embeddings(text):
    response = client.embeddings.create(
        input= text, model= "embedding-001")
    embedding = response.data[0].embedding
    return np.array(embedding)



def load_or_create_vector_store():
    if os.path.exists(vector_path):
        with open(vector_path, "rb") as f:
            return pickle.load(f)


    text = read_pdf(pdf_path=pdf_path)
    chunks = split_text_semanticaly(text, chunk_size=1000)

    embeddings = np.array([get_embeddings(chunk) for chunk in chunks]).astype("float32")


    embeddings /= np.linalg.norm(embeddings, axis=1, keepdims=True)


    index = faiss.IndexFlatIP(embeddings.shape[1]) 

    index.add(embeddings)
    with open (vector_path, "wb") as f :

        pickle.dump((chunks, index),f)

        return chunks, index

def search_similar_chunk(query, chunks, index, Top_k=3):

    query_embedding = get_embeddings(query).astype("float32")

    Distance,Index = index.search(np.expand_dims(query_embedding,axis=0),Top_k)
    return[chunks[index] for index in Index[0]]
    
def get_response(query, history):
    context = "\n\n".join(search_similar_chunk(query,chunks,index,Top_k=3))
    prompt = f"context: {context}\n\n question: {query} \n\n answer based on the context."

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages= [{"role": "user","content":prompt}])
    return response.choices[0].message.content
    
chunks, index = load_or_create_vector_store()

gr.ChatInterface(
    fn = get_response,
    title= "rag from vector",
    type= "messages"
).launch()

    