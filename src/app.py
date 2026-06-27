from fastapi import FastAPI
from langdetect import detect
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

follow_up_keywords = {
    "online": [
        "online",
        "website",
        "app",
        "yono",
        "internet",
        "digital"
    ],
    "branch": [
        "branch",
        "office",
        "visit",
        "offline"
    ],
    "mobile": [
        "mobile",
        "phone",
        "registered number",
        "otp"
    ],
    "documents": [
        "document",
        "documents",
        "proof",
        "required",
        "papers",
        "kyc"
    ],
    "eligibility": [
        "eligible",
        "eligibility",
        "qualify",
        "can i apply",
        "who can apply"
    ],
    "locked_account": [
        "locked",
        "account locked",
        "unlock",
        "blocked"
    ],
    "atm": [
        "atm"
    ],
    "sms": [
        "sms",
        "missed call",
        "message"
    ],
    "statement": [
        "statement",
        "mini statement",
        "transactions",
        "passbook"
    ],
    "block": [
        "block",
        "lost",
        "stolen"
    ],
    "replace": [
        "replace",
        "replacement",
        "new card",
        "damaged",
        "expired"
    ],
    "international_usage": [
        "international",
        "abroad",
        "foreign",
        "overseas"
    ],
    "pin_generation": [
        "pin",
        "generate pin",
        "green pin",
        "reset pin"
    ],
    "delivery": [
        "delivery",
        "delivered",
        "receive",
        "received",
        "not received"
    ],
    "zero_balance": [
        "zero balance",
        "no balance"
    ],
    "minimum_balance": [
        "minimum balance",
        "balance requirement",
        "maintain balance"
    ],
    "online_opening": [
        "open online",
        "online opening",
        "open in app",
        "yono opening"
    ],
    "create": [
        "create",
        "setup",
        "set up",
        "activate",
        "register"
    ],
    "limit": [
        "limit",
        "maximum",
        "daily limit",
        "transaction limit"
    ],
    "reset_pin": [
        "reset pin",
        "forgot pin",
        "change pin",
        "upi pin"
    ],
    "transaction_failed": [
        "failed",
        "transaction failed",
        "payment failed",
        "deducted"
    ],
    "payment_pending": [
        "pending",
        "stuck",
        "processing"
    ],
    "refund": [
        "refund",
        "reversal",
        "money back"
    ],
    "interest": [
        "interest",
        "rate",
        "roi"
    ],
    "tenure": [
        "tenure",
        "duration",
        "years",
        "period"
    ],
    "emi": [
        "emi",
        "monthly payment",
        "installment",
        "instalment"
    ],
    "processing_time": [
        "processing time",
        "how long",
        "approval time",
        "time taken"
    ],
    "annual_fee": [
        "annual fee",
        "fee",
        "charges",
        "yearly charge"
    ],
    "credit_limit": [
        "credit limit",
        "card limit",
        "limit increase"
    ],
    "billing_cycle": [
        "billing cycle",
        "bill date",
        "due date",
        "statement date"
    ],
    "reward_points": [
        "reward",
        "rewards",
        "points",
        "cashback"
    ],
    "minimum_amount": [
        "minimum amount",
        "minimum deposit",
        "least amount"
    ],
    "premature_withdrawal": [
        "premature",
        "withdraw early",
        "break fd",
        "close fd"
    ],
    "tax": [
        "tax",
        "tds",
        "tax saving"
    ],
    "renewal": [
        "renew",
        "renewal",
        "auto renew"
    ],
    "apply": [
        "apply",
        "request",
        "order"
    ],
    "tracking": [
        "track",
        "tracking",
        "status"
    ],
    "stop_payment": [
        "stop payment",
        "stop cheque",
        "cancel cheque"
    ],
    "register": [
        "register",
        "registration",
        "new user"
    ],
    "registration": [
        "register",
        "registration",
        "new user"
    ],
    "forgot_password": [
        "forgot password",
        "reset password",
        "password"
    ],
    "forgot_username": [
        "forgot username",
        "forgot user id",
        "username",
        "user id"
    ],
    "unlock_account": [
        "unlock",
        "locked",
        "account locked"
    ],
    "activation": [
        "activate",
        "activation",
        "enable"
    ],
    "transaction_rights": [
        "transaction rights",
        "full rights",
        "view rights"
    ]
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

    message_lower = message.lower()
    detected_threats = []

    for keyword, details in fraud_keywords.items():
        if keyword in message_lower:
            detected_threats.append({
                "keyword": keyword,
                "fraud_type": details["fraud_type"],
                "risk": details["risk"],
                "advice": details["advice"],
                "recommended_action": details["recommended_action"]
            })

    if detected_threats:
        detected_risks = [threat["risk"] for threat in detected_threats]

        if "critical" in detected_risks:
            overall_risk = "critical"
        elif "high" in detected_risks:
            overall_risk = "high"
        elif "medium" in detected_risks:
            overall_risk = "medium"
        else:
            overall_risk = "low"

        return {
            "fraud_detected": True,
            "overall_risk": overall_risk,
            "detected_threats": detected_threats
        }

    return {
        "fraud_detected": False,
        "overall_risk": "low",
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
    question_lower = question.lower()

    last_intent = conversation_memory["last_intent"]

    if last_intent is None:
        return {
            "message": "No previous conversation found."
        }

    if last_intent in follow_up_answers:
        available_follow_ups = follow_up_answers[last_intent]

        for follow_up_type, answers in available_follow_ups.items():
            matching_keywords = follow_up_keywords.get(
                follow_up_type,
                follow_up_type.replace("_", " ").split()
            )

            for keyword in matching_keywords:
                if keyword in question_lower:
                    return {
                        "previous_intent": last_intent,
                        "follow_up": follow_up_type,
                        "language": language,
                        "answer": answers.get(
                            language,
                            answers["en"]
                        )
                    }

        return {
            "message": "I don't have information for that follow-up question yet."
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
