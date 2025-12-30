from typing import List
from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Scheme for a source used by the agent"""

    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    answer:str = Field(description="The agent´s answer to the query")
    sources:List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")



llm = ChatOpenAI(model="gpt-3.5-turbo")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job postings for an AI engineer using LangChain in Colombia on Linkedin and list the details")})
    print(result)


if __name__ == "__main__":
    main()
