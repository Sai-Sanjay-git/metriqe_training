from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import tool
from dotenv import load_dotenv
from config import model
import os
import sys
import time
import warnings
warnings.filterwarnings("ignore", message="API key must be provided when using hosted LangSmith API")

 
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
 
 
FACTS = {
    "capital of france": "Paris",
    "largest ocean": "Pacific Ocean",
    "inventor of telephone": "Alexander Graham Bell",
    "population of india": "Approximately 1.4 billion"
}

@tool
def get_fact(query: str) -> str:
    """
    Retrieves a fact from a predefined list. The query must be an exact match
    to one of the available facts.
 
    Available facts are:
    - 'capital of france'
    - 'largest ocean'
    - 'inventor of telephone'
    - 'population of india'
    """
    query = query.lower()

    for key, value in FACTS.items():
        if key in query:
            return value

    return "Fact not found."
    
 
def run_data_retrivel_agent():
    """"
     Creates an agent that can use the get_fact tool.
    """
    wait_time = 5
    print(f"Jarvis is suiting up...he will be ready after {wait_time} seconds")
    for i in range(wait_time, 0, -1):
        sys.stdout.write(f"\r PLease wait for {i}seconds....")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rJarvis is ready & running...           \n")
    try:
        llm = ChatOpenAI(model=model, openai_api_key=openai_api_key)
        tools = [get_fact]
        prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(llm,tools,prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,
                                    handle_parsing_errors=True)
        

        response = []
        
        print("\n Question 1: capital of france")
        response.append(agent_executor.invoke({"input": "What is the capital of france?"}))

        print("\n Question 2: largest ocean")
        response.append(agent_executor.invoke({"input": "What is the largest ocean in the world?"}))

        print("\n Final Answers")
        for i, response in enumerate(response, 1):
            print(f"Response {i}: {response['output']}")

    except Exception as e:
        print(f"\n Error happened: {e}")


if __name__ == "__main__":
    run_data_retrivel_agent()                                   