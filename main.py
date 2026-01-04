from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from schemas import AgentResponse


# Initialize tools and model
tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")

# Create agent with structured output using ToolStrategy
agent = create_agent(
    model=llm,
    tools=tools,
    response_format=ToolStrategy(AgentResponse),
    system_prompt="You are a helpful assistant that searches for information and provides structured responses with sources."
)


def main():
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": "search for 3 job postings for an ai engineer using langchain in Colombia on Linkedin and list their details"
        }]
    })
    
    # Access structured response
    if "structured_response" in result:
        print(result["structured_response"])
    else:
        print(result)


if __name__ == "__main__":
    main()
