from fastapi import FastAPI, File, UploadFile, Form, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.storage import save_file
from app.nlp import answer_question

app = FastAPI()

origins = [
    "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    filepath: str
    question: str

@app.post("/upload/")
async def upload_document(title: str = Form(...), file: UploadFile = File(...)):
    filepath = save_file(file)
    return {"title": title, "filepath": filepath}

@app.post("/ask/")
async def ask_question(request: AskRequest):
    answer = answer_question(request.filepath, request.question)
    return {"question": request.question, "answer": answer}


@app.get("/")
async def read_root():
    return {"message": "Welcome to the PDF QA API"}

import logging
logging.basicConfig(level=logging.INFO)
logging.info("Application startup complete.")
