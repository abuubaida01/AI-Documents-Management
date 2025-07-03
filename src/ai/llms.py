from django.conf import settings
from langchain_openai import ChatOpenAI
import os 

api_key = os.environ.get('savior_ai_token')

print("\n\n api_key", api_key)

def get_openai_model(model="gpt-4o-mini"):
  return ChatOpenAI(
    model=model,
    temperature=0.5,
    max_retries=2,
    api_key=api_key
  )