from fastapi import FastAPI
from langdetect import detect
from knowledge_base import banking_faqs, keywords, fraud_keywords
from knowledge_base import banking_faqs
from knowledge_base import (
    banking_faqs,
    keywords,
    fraud_keywords,
    follow_up_answers
)

def get_supported_language(text: str):
    try:
        language = detect(text)
    except:
        language = "en"

    if language not in ["en", "kn", "hi"]:
        language = "en"

    return language

app = FastAPI(title="SBI AssistAI")

conversation_memory = {
    "last_intent": None
}

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

    for keyword, details in fraud_keywords.items():
        if keyword in message:

            return {
                "fraud_detected": True,
                "keyword": keyword,
                "fraud_type": details["fraud_type"],
                "risk": details["risk"],
                "advice": details["advice"],
                "recommended_action": details["recommended_action"]
            }
        
        return {
            "fraud_detected": False,
            "risk": "low",
            "message": "No obvious fraud indicators detected."
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

    language = get_supported_language(question)

    question_lower = question.lower()

    for intent, words in keywords.items():

        for word in words:

            if word.lower() in question_lower:
                conversation_memory["last_intent"] = intent
                return {
                    "language": language,
                    "question": question,
                    "answer": banking_faqs[intent].get(
                        language,
                        banking_faqs[intent]["en"]
                    )
                }

@app.get("/follow-up")
def follow_up(question: str):

    language = get_supported_language(question)

    last_intent = conversation_memory["last_intent"]

    if last_intent is None:
        return {
            "message": "No previous conversation found."
        }

    if (
        "online" in question.lower()
        and last_intent in follow_up_answers
    ):
        return {
            "previous_intent": last_intent,
            "language": language,
            "answer": follow_up_answers[last_intent]["online"].get(
                language,
                follow_up_answers[last_intent]["online"]["en"]
            )
        }

    return {
        "message": "I don't understand this follow-up question yet."
    }

@app.get("/detect-language")
def detect_language(text: str):
    return {
        "language": get_supported_language(text)
    }

@app.get("/multilingual-help")
def multilingual_help(text: str):

    language = get_supported_language(text)

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