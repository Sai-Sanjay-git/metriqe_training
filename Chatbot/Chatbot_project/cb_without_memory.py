#step 1 import
from openai import OpenAI
import gradio as gr
import os
from dotenv import load_dotenv
from sm import CARAMEL_AI_SPORTS_COACH_PROMPT

#step 2 -loading the secrets
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(api_key)
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
#step 3 giving the presonality for our Chatbot
SystemMessage = CARAMEL_AI_SPORTS_COACH_PROMPT
print(SystemMessage)

def get_response(HumanMessage, history):
    BaseMessage=[{"role":"system", "content": SystemMessage}]
    BaseMessage.extend(history)
    BaseMessage.append({"role": "user","content": HumanMessage})

    response = client.chat.completions.create(
        model= "gemini-2.5-flash",
        messages=BaseMessage
    )
    AIMessage= response.choices[0].message.content
    print(AIMessage)
    return AIMessage

gr.ChatInterface(
    fn=get_response,
    type="messages"
).launch(share=True)
