from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
 
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
 
def hello_langchain():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)
    response = llm.invoke("Please share some love quotes I can say to someone special.")
    print(response.content)  # Use .content instead of .context
 
if __name__ == "__main__":
    hello_langchain()