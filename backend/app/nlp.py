import os
import fitz  # PyMuPDF
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from typing import List

def extract_text_from_pdf(filepath: str) -> str:
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def answer_question(filepath: str, question: str) -> str:
    text = extract_text_from_pdf(filepath)
    text_chunks = chunk_text(text)

    model_name = "deepset/roberta-base-squad2" 
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    
    qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
    
    best_answer = None
    best_score = 0
    for chunk in text_chunks:
        result = qa_pipeline(question=question, context=chunk)
        if result['score'] > best_score:
            best_score = result['score']
            best_answer = result['answer']
    
    return best_answer


