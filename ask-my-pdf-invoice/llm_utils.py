from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from config import api_key


try:
    llm = ChatGoogleGenerativeAI(model="model/gemini-2.5-flash-lite-preview-06-17",GOOGLE_API_KEY = api_key, temparture = 0,)
    embeddings = GoogleGenerativeAIEmbeddings(model="model/embedding-001", google_api_key= api_key)
except Exception as e:
    raise RuntimeError("error calling api error : {e}")

print(llm.invoke("hi"))