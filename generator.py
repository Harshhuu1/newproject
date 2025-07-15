from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import pandas as pd
import os
from dotenv import  load_dotenv
load_dotenv()

# ✅ Set your Hugging Face API key

# ✅ Create HuggingFace LLM
hf_llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    temperature=0.7
)

# ✅ LangChain Chat Wrapper
llm = ChatHuggingFace(llm=hf_llm)

# ✅ Prompt template
prompt = PromptTemplate(
    input_variables=["title", "description", "revenue", "cashflow"],
    template="""
You're an M&A analyst. Write a 2-sentence acquisition pitch.

Title: {title}
Revenue: {revenue}
Cash Flow: {cashflow}
Description: {description}

Pitch:
"""
)

chain = prompt | llm  # New LangChain Runnable

def generate_pitches(df):
    pitches = []
    for _, row in df.iterrows():
        input_data = {
            "title": row["title"],
            "description": row["description"],
            "revenue": row["revenue"],
            "cashflow": row["cashflow"]
        }
        pitch = chain.invoke(input_data)
        pitches.append(pitch.strip() if isinstance(pitch, str) else str(pitch))
    df["pitch"] = pitches
    return df
