from openai import OpenAI
import gradio as gr
import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

client = OpenAI(base_url=base_url,api_key=api_key )

def get_response(image_path):
    if image_path is None:
        return "Please upload the image file "
    
    with open (image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role":"user","content":[
            {"type":"text","text":"Describe about the picture in  detail"},
            {
                "type":"image_url",
                "image_url":{"url":f"data:image/jpeg;base64,{base64_image}"}
             
             }

            ]
            }
        ]
    )
    return response

gr.Interface(
    fn=get_response,
    inputs= gr.Image(type ="filepath",label="upload a image"),
    outputs=gr.Textbox(label="image Description"),
    title= "AI image reader"

).launch(share= True)