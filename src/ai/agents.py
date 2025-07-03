from langgraph.prebuilt import create_react_agent
from .llms import get_openai_model
from .tools import (documents_tools)


def get_document_agent():
  openai_model = get_openai_model()

  agent = create_react_agent(
    model=openai_model,
    tools=documents_tools,
    prompt="You are a helpful assistant in managing a user's documents within this app"
  )

  return agent

