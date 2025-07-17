from openai import OpenAI
from dotenv import load_dotenv
import requests
import os
import gradio as gr

load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
client=OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


url = "https://raw.githubusercontent.com/hereandnowai/vac/refs/heads/master/prospectus-context.txt"
response= requests.get(url)

file_path = "profileof-here-and-nowai.txt"

with open(file_path, "w", encoding="utf-8") as f :
    f.write(response.text)

try:
    with open(file_path, "r", encoding="utf-8") as file:
        text_lines = file.readlines()
        text_lines = [line.strip() for line in text_lines if line.strip()]
        text_content = "\n".join(text_lines) if text_lines else "no text found"
except Exception as e:
    text_content = "Error Extracting file"


def rag_text(HumanMessage, history):
    SystemMessage = f"You are popcorn AI, please answer only from the text file \n\n{text_content}"
    BaseMessage = [{"role":"system","content": SystemMessage}]
    BaseMessage.extend(history)
    BaseMessage.append({"role":"user","content":HumanMessage})
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=BaseMessage
    )
    return response.choices[0].message.content

gr.ChatInterface(
    fn=rag_text,
    type="messages"
).launch(share=True)