from openai import OpenAI
import gradio as gr
import requests
import os
import PyPDF2
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
client=OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

url = "https://raw.githubusercontent.com/hereandnowai/rag-workshop/main/pdfs/About_HERE_AND_NOW_AI.pdf"
response = requests.get(url)

pdf_file_name = "profile-of-hereandnowai.pdf"
pdf_path = os.path.join(os.path.dirname(__file__),pdf_file_name)

with open (pdf_path, "wb") as f:
    f.write(response.content)

# extract that pdf
try:
    with open (pdf_path,"rb") as file:
        reader = PyPDF2.PdfReader(file)
        pdf_text_chunks = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                pdf_text_chunks.append(page_text.strip())
        pdf_context = "\n".join(pdf_text_chunks )if pdf_text_chunks else "no text found"
except Exception as e :
    print(f"Erroe reading pdf : {e}")
    pdf_context = "error extracting text from the pdf"


def get_response(HumanMessage,history):
    message = f"context from {pdf_path}:\n {pdf_context}\n\n Question : {HumanMessage}\n\n Anwser only based on the context"
    response =client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role":"user","content":message}])
    
    return response.choices[0].message.content
gr.ChatInterface(
    fn = get_response,
    type= "messages"
).launch(share= True)
if __name__ =="__main__":
   print(get_response("who is the cto of the here and now ai ?",[]))