from fastapi import FastAPI
from langdetect import detect
from knowledge_base import banking_faqs, keywords, fraud_keywords
from knowledge_base import banking_faqs

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

@app.get("/fraud-check")
def fraud_check(message: str):

    message = message.lower()

    for keyword, advice in fraud_keywords.items():

        if keyword in message:

            return {
                "fraud_detected": True,
                "risk": "high",
                "keyword": keyword,
                "advice": advice
     }
        return {
    "fraud_detected": False,
    "risk": "low",
    "advice": "No obvious fraud indicators detected."
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

@app.get("/ask")
def ask(question: str):

    language = detect(question)

    question_lower = question.lower()

    for intent, words in keywords.items():

        for word in words:

            if word.lower() in question_lower:

                return {
                    "language": language,
                    "question": question,
                    "answer": banking_faqs[intent].get(
                        language,
                        banking_faqs[intent]["en"]
                    )
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