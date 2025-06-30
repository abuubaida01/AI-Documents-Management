from langchain.llms import HuggingFacePipeline
from transformers import pipeline

# Load a local model from Hugging Face
hf_pipeline = pipeline("text-generation", model="gpt2")

# Wrap it in LangChain
llm = HuggingFacePipeline(pipeline=hf_pipeline)

response = llm("What is LangChain?")
print(response)
