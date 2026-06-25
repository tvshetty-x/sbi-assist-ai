keywords = {
    "password": [
        "password",
        "forgot password",
        "ಪಾಸ್‌ವರ್ಡ್",
        "पासवर्ड",
        "password reset",
        "reset madbeku",
        "password marethu",
        "nange password"
    ],

    "balance": [
        "balance",
        "account balance",
        "ಬ್ಯಾಲೆನ್ಸ್",
        "बैलेंस",
        "balance check",
        "balance nodbeku",
        "nanna balance"
    ]
}

keywords["debit card"] = [
    "debit card",
    "block card",
    "lost card",
    "card missing",
    "card block",
    "card help",
    "card kaledhoythu",
    "nanna card sigtilla"
]

fraud_keywords = {
    "otp": {
        "fraud_type": "OTP Scam",
        "risk": "critical",
        "advice": "SBI never asks for OTP over phone calls, SMS, or email.",
        "recommended_action": "Do not share your OTP. End the conversation immediately and contact SBI through official channels."
    },

    "pin": {
        "fraud_type": "PIN Theft",
        "risk": "critical",
        "advice": "Never share your ATM PIN with anyone.",
        "recommended_action": "Keep your PIN confidential. If you shared it, change it immediately."
    },

    "link": {
        "fraud_type": "Phishing",
        "risk": "high",
        "advice": "Avoid clicking suspicious links claiming to be from SBI.",
        "recommended_action": "Visit only the official SBI website or YONO SBI app."
    },

    "customer care": {
        "fraud_type": "Fake Customer Care",
        "risk": "high",
        "advice": "Fraudsters often impersonate bank officials.",
        "recommended_action": "Contact SBI using only the official customer care number."
    },

    "upi": {
        "fraud_type": "UPI Scam",
        "risk": "critical",
        "advice": "Receiving money never requires entering your UPI PIN.",
        "recommended_action": "Reject suspicious collect requests and never enter your UPI PIN to receive money."
    },

    "kyc": {
        "fraud_type": "Fake KYC",
        "risk": "critical",
        "advice": "Update your KYC only through official SBI branches or YONO SBI.",
        "recommended_action": "Ignore unsolicited KYC update messages and verify directly with SBI."
    },

    "atm": {
        "fraud_type": "Card Skimming",
        "risk": "medium",
        "advice": "Inspect ATMs before using them.",
        "recommended_action": "Cover the keypad while entering your PIN and avoid damaged ATMs."
    }
}

banking_faqs = {
    "password": {
        "en": "Open YONO SBI and select Forgot Password.",
        "kn": "YONO SBI ತೆರೆಯಿರಿ ಮತ್ತು Forgot Password ಆಯ್ಕೆಮಾಡಿ.",
        "hi": "YONO SBI खोलें और Forgot Password चुनें।"
    },

    "balance": {
        "en": "You can check balance using YONO SBI, ATM, SMS Banking, or Internet Banking.",
        "kn": "ನೀವು YONO SBI, ATM, SMS Banking ಅಥವಾ Internet Banking ಮೂಲಕ ಬ್ಯಾಲೆನ್ಸ್ ಪರಿಶೀಲಿಸಬಹುದು.",
        "hi": "आप YONO SBI, ATM, SMS Banking या Internet Banking से बैलेंस देख सकते हैं।"
    }
}

banking_faqs["debit card"] = {
    "en": "You can block your debit card through YONO SBI or Internet Banking.",
    "kn": "ನೀವು YONO SBI ಅಥವಾ Internet Banking ಮೂಲಕ ನಿಮ್ಮ ಡೆಬಿಟ್ ಕಾರ್ಡ್ ಅನ್ನು ಬ್ಲಾಕ್ ಮಾಡಬಹುದು.",
    "hi": "आप YONO SBI या Internet Banking के माध्यम से अपना डेबिट कार्ड ब्लॉक कर सकते हैं।"
}

follow_up_answers = {
    "password": {
        "online": {
            "en": "Yes. You can reset your password completely through the YONO SBI app.",
            "kn": "ಹೌದು. YONO SBI ಅಪ್ಲಿಕೇಶನ್ ಮೂಲಕ ಪಾಸ್‌ವರ್ಡ್ ಮರುಹೊಂದಿಸಬಹುದು.",
            "hi": "हाँ, आप YONO SBI ऐप से पासवर्ड रीसेट कर सकते हैं।"
        }
    }
}