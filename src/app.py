from fastapi import FastAPI
from langdetect import detect

app = FastAPI(title="SBI AssistAI")

@app.get("/")
def home():
    return {
        "message": "Welcome to SBI AssistAI"
    }

@app.get("/health")
def health():
    return {
        "status": "running"
    }

@app.get("/fraud-tips")
def fraud_tips():
    return {
        "tips": [
            "Never share OTP with anyone.",
            "SBI will never ask for your PIN.",
            "Avoid clicking suspicious links.",
            "Verify official SBI websites before logging in."
        ]
    }

@app.get("/banking-help")
def banking_help():
    return {
        "services": [
            "Reset YONO password",
            "Check account balance",
            "Open savings account",
            "Report lost debit card"
        ]
    }

from knowledge_base import banking_faqs

@app.get("/ask")
def ask(question: str):
    answer = banking_faqs.get(
        question.lower(),
        "Sorry, I don't have information about that yet."
    )

    return {
        "question": question,
        "answer": answer
    }

@app.get("/detect-language")
def detect_language(text: str):
    return {
        "language": detect(text)
    }

@app.get("/multilingual-help")
def multilingual_help(text: str):

    language = detect(text)

    responses = {
        "en": "How can I help you with SBI banking services?",
        "kn": "ಎಸ್‌ಬಿಐ ಬ್ಯಾಂಕಿಂಗ್ ಸೇವೆಗಳಲ್ಲಿ ನಾನು ನಿಮಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು?",
        "hi": "मैं एसबीआई बैंकिंग सेवाओं में आपकी कैसे सहायता कर सकता हूँ?"
    }

    return {
        "language": language,
        "response": responses.get(
            language,
            "Language currently not supported."
        )
    }