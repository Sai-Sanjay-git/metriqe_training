from openai import OpenAI
import gradio as gr
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
client=OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#step 3 - getting info from web:
url = "https://www.metriqe.com/"

response = requests.get(url,
                        headers={"user_agent": "Mozilla/5.0"},
                        timeout=10)
soup = BeautifulSoup(response.content, "html.parser")
website_context = soup.body.get_text(separator= "\n",
                                     strip = True)if soup.body else "no info found"

def get_response(HumanMessage, history):
    message = f"Context from {url}:\n{website_context}\n\n Question: {HumanMessage}\n Answer only based or context"
    response =client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role":"user","content":message}])
    
    return response.choices[0].message.content

print(get_response("What is the Metriqe’s Accounting BPO Services?", []))


