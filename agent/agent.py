import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace


app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


hf_api = 
os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_api


# LLM Model


llm_endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.5,
    max_new_tokens=300
)

model = ChatHuggingFace(llm=llm_endpoint)




prompt = PromptTemplate(
    template="Answer the following question clearly:\n\nQuestion: {question}",
    input_variables=["question"]
)


parser = StrOutputParser()

chain = prompt | model | parser



class ChatRequest(BaseModel):
    question: str




@app.get("/")
def home():
    return {"message": "Climate AI Chatbot API running"}


@app.post("/chat")
def chat(data: ChatRequest):

    response = chain.invoke({
        "question": data.question
    })

    return {
        "answer": response
    }
    
#python -m uvicorn agent:app --port 8001 --reload