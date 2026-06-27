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
keywords["account opening"] = [
    "account opening",
    "open account",
    "open bank account",
    "open savings account",
    "open sbi account",
    "new account",
    "new bank account",
    "new savings account",
    "create account",
    "create bank account",
    "start account",
    "bank account",
    "savings account",
    "sbi account",
    "sbi savings account",
    "zero balance account",
    "basic savings account",
    "salary account",
    "student account",
    "minor account",
    "joint account",
    "account application",
    "apply for account",
    "apply savings account",
    "online account opening",
    "open account online",
    "digital account opening",
    "yono account opening",
    "open account in yono",
    "sbi online account",
    "instant account opening",
    "account documents",
    "documents for account",
    "account eligibility",
    "eligibility for account",
    "kyc for account",
    "account kyc",
    "branch account opening",
    "nearest branch account",
    "how to open account",
    "how can i open account",
    "i want to open account",
    "need new account",
    "account open madbeku",
    "new bank account madbeku",
    "hosa account",
    "account beku",
    "savings account beku",
    "bank account beku",
    "sbi account beku",
    "account madbeku",
    "khata open madbeku",
    "khate tereyabeku",
    "nanna account open",
    "nanage account beku"
]

keywords["upi"] = [
    "upi",
    "upi id",
    "upi pin",
    "upi payment",
    "upi transfer",
    "upi transaction",
    "upi registration",
    "upi setup",
    "upi not working",
    "upi problem",
    "upi issue",
    "upi failed",
    "upi pending",
    "upi refund",
    "upi limit",
    "daily upi limit",
    "upi transaction limit",
    "create upi",
    "create upi id",
    "set upi pin",
    "reset upi pin",
    "change upi pin",
    "forgot upi pin",
    "link bank account",
    "add bank account",
    "check upi balance",
    "google pay",
    "gpay",
    "gpay problem",
    "gpay not working",
    "phonepe",
    "phonepe problem",
    "phonepe not working",
    "paytm",
    "paytm problem",
    "bhim",
    "bhim upi",
    "yono upi",
    "sbi upi",
    "scan qr",
    "qr code",
    "qr payment",
    "pay by qr",
    "scan and pay",
    "send money",
    "receive money",
    "transfer money",
    "money transfer",
    "instant transfer",
    "bank transfer",
    "mobile payment",
    "collect request",
    "payment request",
    "upi collect",
    "money not received",
    "payment failed",
    "transaction failed",
    "transaction pending",
    "amount debited",
    "amount deducted",
    "payment stuck",
    "nanna upi",
    "upi madbeku",
    "upi work agtilla",
    "upi kelasa agtilla",
    "upi problem ide",
    "gpay problem ide",
    "phonepe problem ide",
    "money barlilla",
    "payment aglilla",
    "transaction fail aytu",
    "upi pin marethu",
    "upi pin reset madbeku"
]

keywords["home loan"] = [
    "home loan",
    "housing loan",
    "house loan",
    "sbi home loan",
    "apply home loan",
    "apply for home loan",
    "home loan application",
    "housing loan application",
    "loan for house",
    "buy house",
    "buy house loan",
    "buy flat",
    "buy flat loan",
    "own house loan",
    "property loan",
    "home finance",
    "house finance",
    "home loan eligibility",
    "housing loan eligibility",
    "home loan documents",
    "documents for home loan",
    "property documents",
    "home loan interest",
    "home loan interest rate",
    "housing loan interest",
    "home loan emi",
    "emi for home loan",
    "home loan calculator",
    "loan tenure",
    "loan amount",
    "salary home loan",
    "self employed home loan",
    "joint home loan",
    "balance transfer home loan",
    "top up home loan",
    "pre approved home loan",
    "home loan status",
    "home loan branch",
    "home loan approval",
    "home loan processing fee",
    "home loan subsidy",
    "pmay home loan",
    "loan beku",
    "home loan madbeku",
    "mane loan",
    "manege loan",
    "mane kharidi loan",
    "house loan beku",
    "property loan beku",
    "own house loan beku",
    "home loan interest eshtu",
    "home loan emi eshtu",
    "loan documents beku"
]

banking_faqs["account opening"] = {
    "en": "You can open an SBI savings account online through YONO SBI or by visiting a nearby SBI branch.",
    "kn": "ನೀವು YONO SBI ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅಥವಾ ಸಮೀಪದ SBI ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಿ ಉಳಿತಾಯ ಖಾತೆ ತೆರೆಯಬಹುದು.",
    "hi": "आप YONO SBI के माध्यम से ऑनलाइन या नजदीकी SBI शाखा में जाकर बचत खाता खोल सकते हैं।"
}

banking_faqs["upi"] = {
    "en": "You can use SBI UPI through YONO SBI or supported UPI apps to send, receive, and scan payments.",
    "kn": "ನೀವು YONO SBI ಅಥವಾ ಬೆಂಬಲಿತ UPI ಆ್ಯಪ್‌ಗಳ ಮೂಲಕ ಹಣ ಕಳುಹಿಸಲು, ಸ್ವೀಕರಿಸಲು ಮತ್ತು QR ಪಾವತಿ ಮಾಡಲು SBI UPI ಬಳಸಬಹುದು.",
    "hi": "आप YONO SBI या समर्थित UPI ऐप्स से पैसे भेजने, प्राप्त करने और QR भुगतान करने के लिए SBI UPI का उपयोग कर सकते हैं।"
}

banking_faqs["home loan"] = {
    "en": "You can apply for an SBI home loan online or at an SBI branch with income and property documents.",
    "kn": "ಆದಾಯ ಮತ್ತು ಆಸ್ತಿ ದಾಖಲೆಗಳೊಂದಿಗೆ ನೀವು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅಥವಾ SBI ಶಾಖೆಯಲ್ಲಿ SBI ಗೃಹ ಸಾಲಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.",
    "hi": "आप आय और संपत्ति दस्तावेजों के साथ ऑनलाइन या SBI शाखा में SBI होम लोन के लिए आवेदन कर सकते हैं।"
}

follow_up_answers["account opening"] = {
    "documents": {
        "en": "You usually need identity proof, address proof, PAN, photographs, and KYC details.",
        "kn": "ಸಾಮಾನ್ಯವಾಗಿ ಗುರುತಿನ ದಾಖಲೆ, ವಿಳಾಸದ ದಾಖಲೆ, PAN, ಫೋಟೋಗಳು ಮತ್ತು KYC ವಿವರಗಳು ಬೇಕಾಗುತ್ತವೆ.",
        "hi": "आम तौर पर पहचान प्रमाण, पता प्रमाण, PAN, फोटो और KYC विवरण की जरूरत होती है।"
    },
    "eligibility": {
        "en": "Resident individuals with valid KYC documents can usually open an SBI savings account.",
        "kn": "ಮಾನ್ಯ KYC ದಾಖಲೆಗಳಿರುವ ನಿವಾಸಿ ವ್ಯಕ್ತಿಗಳು ಸಾಮಾನ್ಯವಾಗಿ SBI ಉಳಿತಾಯ ಖಾತೆ ತೆರೆಯಬಹುದು.",
        "hi": "वैध KYC दस्तावेजों वाले निवासी व्यक्ति आम तौर पर SBI बचत खाता खोल सकते हैं।"
    },
    "online": {
        "en": "Yes. You can start savings account opening online through YONO SBI, subject to KYC verification.",
        "kn": "ಹೌದು. KYC ಪರಿಶೀಲನೆಗೆ ಒಳಪಟ್ಟು YONO SBI ಮೂಲಕ ಉಳಿತಾಯ ಖಾತೆ ತೆರೆಯುವಿಕೆಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪ್ರಾರಂಭಿಸಬಹುದು.",
        "hi": "हाँ। KYC सत्यापन के अधीन आप YONO SBI से बचत खाता खोलने की प्रक्रिया ऑनलाइन शुरू कर सकते हैं।"
    }
}

follow_up_answers["upi"] = {
    "create": {
        "en": "Open YONO SBI or a UPI app, select your SBI account, verify your mobile number, and set a UPI PIN.",
        "kn": "YONO SBI ಅಥವಾ UPI ಆ್ಯಪ್ ತೆರೆಯಿರಿ, ನಿಮ್ಮ SBI ಖಾತೆ ಆಯ್ಕೆಮಾಡಿ, ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಪರಿಶೀಲಿಸಿ ಮತ್ತು UPI PIN ಹೊಂದಿಸಿ.",
        "hi": "YONO SBI या UPI ऐप खोलें, अपना SBI खाता चुनें, मोबाइल नंबर सत्यापित करें और UPI PIN सेट करें।"
    },
    "limit": {
        "en": "UPI limits may vary by bank, app, and transaction type. Check YONO SBI or official SBI channels for current limits.",
        "kn": "UPI ಮಿತಿಗಳು ಬ್ಯಾಂಕ್, ಆ್ಯಪ್ ಮತ್ತು ವ್ಯವಹಾರದ ಪ್ರಕಾರ ಬದಲಾಗಬಹುದು. ಪ್ರಸ್ತುತ ಮಿತಿಗಳಿಗೆ YONO SBI ಅಥವಾ ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "hi": "UPI सीमा बैंक, ऐप और लेनदेन प्रकार के अनुसार बदल सकती है। वर्तमान सीमा के लिए YONO SBI या आधिकारिक SBI चैनल देखें।"
    },
    "failed": {
        "en": "If money is debited but not received, wait for reversal and raise a complaint through the app or SBI support if needed.",
        "kn": "ಹಣ ಕಡಿತವಾಗಿ ಸ್ವೀಕರಿಸದಿದ್ದರೆ, ರಿವರ್ಸಲ್‌ಗಾಗಿ ಕಾಯಿರಿ ಮತ್ತು ಅಗತ್ಯವಿದ್ದರೆ ಆ್ಯಪ್ ಅಥವಾ SBI ಸಹಾಯದ ಮೂಲಕ ದೂರು ನೀಡಿ.",
        "hi": "यदि पैसा कट गया है लेकिन प्राप्त नहीं हुआ, तो रिवर्सल की प्रतीक्षा करें और जरूरत हो तो ऐप या SBI सहायता से शिकायत दर्ज करें।"
    },
    "online": {
        "en": "Yes. SBI UPI can be created and used online through YONO SBI or supported UPI apps.",
        "kn": "ಹೌದು. SBI UPI ಅನ್ನು YONO SBI ಅಥವಾ ಬೆಂಬಲಿತ UPI ಆ್ಯಪ್‌ಗಳ ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ರಚಿಸಿ ಬಳಸಬಹುದು.",
        "hi": "हाँ। SBI UPI को YONO SBI या समर्थित UPI ऐप्स के माध्यम से ऑनलाइन बनाया और उपयोग किया जा सकता है।"
    }
}

follow_up_answers["home loan"] = {
    "documents": {
        "en": "You usually need identity proof, address proof, income proof, bank statements, and property documents.",
        "kn": "ಸಾಮಾನ್ಯವಾಗಿ ಗುರುತಿನ ದಾಖಲೆ, ವಿಳಾಸದ ದಾಖಲೆ, ಆದಾಯದ ದಾಖಲೆ, ಬ್ಯಾಂಕ್ ಸ್ಟೇಟ್ಮೆಂಟ್‌ಗಳು ಮತ್ತು ಆಸ್ತಿ ದಾಖಲೆಗಳು ಬೇಕಾಗುತ್ತವೆ.",
        "hi": "आम तौर पर पहचान प्रमाण, पता प्रमाण, आय प्रमाण, बैंक स्टेटमेंट और संपत्ति दस्तावेजों की जरूरत होती है।"
    },
    "interest": {
        "en": "Home loan interest rates can change. Please check the official SBI website or branch for the latest rate.",
        "kn": "ಗೃಹ ಸಾಲದ ಬಡ್ಡಿದರಗಳು ಬದಲಾಗಬಹುದು. ಇತ್ತೀಚಿನ ದರಕ್ಕಾಗಿ ಅಧಿಕೃತ SBI ವೆಬ್‌ಸೈಟ್ ಅಥವಾ ಶಾಖೆಯನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "hi": "होम लोन ब्याज दरें बदल सकती हैं। नवीनतम दर के लिए आधिकारिक SBI वेबसाइट या शाखा से जांच करें।"
    },
    "eligibility": {
        "en": "Eligibility depends on income, repayment capacity, credit profile, age, and property details.",
        "kn": "ಅರ್ಹತೆ ಆದಾಯ, ಮರುಪಾವತಿ ಸಾಮರ್ಥ್ಯ, ಕ್ರೆಡಿಟ್ ಪ್ರೊಫೈಲ್, ವಯಸ್ಸು ಮತ್ತು ಆಸ್ತಿ ವಿವರಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ.",
        "hi": "पात्रता आय, पुनर्भुगतान क्षमता, क्रेडिट प्रोफाइल, आयु और संपत्ति विवरण पर निर्भर करती है।"
    },
    "online": {
        "en": "Yes. You can start an SBI home loan application online or visit an SBI branch for assistance.",
        "kn": "ಹೌದು. SBI ಗೃಹ ಸಾಲ ಅರ್ಜಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪ್ರಾರಂಭಿಸಬಹುದು ಅಥವಾ ಸಹಾಯಕ್ಕಾಗಿ SBI ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಬಹುದು.",
        "hi": "हाँ। आप SBI होम लोन आवेदन ऑनलाइन शुरू कर सकते हैं या सहायता के लिए SBI शाखा जा सकते हैं।"
    }
}
keywords["credit card"] = [
    "credit card",
    "cc",
    "sbi credit card",
    "apply credit card",
    "apply for credit card",
    "new credit card",
    "credit card application",
    "card application",
    "credit limit",
    "card limit",
    "increase credit limit",
    "credit card eligibility",
    "credit card documents",
    "credit card bill",
    "card bill",
    "billing cycle",
    "credit card statement",
    "card statement",
    "annual fee",
    "card annual fee",
    "card charges",
    "reward points",
    "sbi card",
    "sbi cards",
    "credit card status",
    "track credit card",
    "credit card payment",
    "pay card bill",
    "card due date",
    "minimum due",
    "card madbeku",
    "credit card beku",
    "cc beku",
    "card apply madbeku",
    "credit limit eshtu",
    "card bill bandide",
    "card payment madbeku"
]

keywords["fixed deposit"] = [
    "fixed deposit",
    "fd",
    "sbi fd",
    "open fd",
    "create fd",
    "book fd",
    "fd account",
    "fixed deposit account",
    "term deposit",
    "sbi term deposit",
    "deposit scheme",
    "fd interest",
    "fd interest rate",
    "fixed deposit interest",
    "fd rates",
    "fd tenure",
    "deposit tenure",
    "fd maturity",
    "maturity amount",
    "fd minimum amount",
    "minimum fd amount",
    "fd renewal",
    "renew fd",
    "break fd",
    "close fd",
    "premature withdrawal",
    "premature fd",
    "tax saving fd",
    "senior citizen fd",
    "fd certificate",
    "fd receipt",
    "fd status",
    "fd madbeku",
    "deposit madbeku",
    "hana deposit madbeku",
    "fd interest eshtu",
    "fd close madbeku",
    "fd maturity yavaga"
]

keywords["cheque book"] = [
    "cheque book",
    "check book",
    "sbi cheque book",
    "sbi check book",
    "apply cheque book",
    "apply check book",
    "request cheque book",
    "request check book",
    "new cheque book",
    "new check book",
    "cheque book request",
    "check book request",
    "cheque leaves",
    "check leaves",
    "cheque leaf",
    "check leaf",
    "cheque book delivery",
    "check book delivery",
    "cheque book status",
    "check book status",
    "track cheque book",
    "track check book",
    "cheque book charges",
    "check book charges",
    "cheque book fee",
    "stop cheque",
    "cancel cheque",
    "cancelled cheque",
    "cheque issue",
    "cheque not received",
    "check not received",
    "cheque book madbeku",
    "check book madbeku",
    "cheque beku",
    "check beku",
    "cheque leaf beku",
    "cheque book barlilla"
]

keywords["net banking"] = [
    "net banking",
    "internet banking",
    "online banking",
    "sbi net banking",
    "sbi internet banking",
    "onlinesbi",
    "online sbi",
    "net banking login",
    "internet banking login",
    "login net banking",
    "netbanking",
    "ibanking",
    "personal banking login",
    "retail banking login",
    "register net banking",
    "net banking registration",
    "internet banking registration",
    "activate net banking",
    "net banking activate",
    "net banking username",
    "forgot username",
    "forgot user id",
    "forgot password",
    "reset net banking password",
    "profile password",
    "transaction password",
    "unlock account",
    "account locked",
    "login problem",
    "net banking not working",
    "internet banking not working",
    "online banking problem",
    "net banking madbeku",
    "internet banking beku",
    "login agtilla",
    "password marethu",
    "username marethu",
    "account lock agide"
]

banking_faqs["credit card"] = {
    "en": "You can apply for an SBI credit card through official SBI Card channels or by visiting an SBI branch.",
    "kn": "ನೀವು ಅಧಿಕೃತ SBI Card ಚಾನೆಲ್‌ಗಳ ಮೂಲಕ ಅಥವಾ SBI ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಿ SBI ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್‌ಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.",
    "hi": "आप आधिकारिक SBI Card चैनलों या SBI शाखा में जाकर SBI क्रेडिट कार्ड के लिए आवेदन कर सकते हैं।"
}

banking_faqs["fixed deposit"] = {
    "en": "You can open an SBI fixed deposit through YONO SBI, Internet Banking, or an SBI branch.",
    "kn": "ನೀವು YONO SBI, Internet Banking ಅಥವಾ SBI ಶಾಖೆಯ ಮೂಲಕ SBI ಸ್ಥಿರ ಠೇವಣಿ ತೆರೆಯಬಹುದು.",
    "hi": "आप YONO SBI, इंटरनेट बैंकिंग या SBI शाखा के माध्यम से SBI फिक्स्ड डिपॉजिट खोल सकते हैं।"
}

banking_faqs["cheque book"] = {
    "en": "You can request an SBI cheque book through YONO SBI, Internet Banking, ATM, or your home branch.",
    "kn": "ನೀವು YONO SBI, Internet Banking, ATM ಅಥವಾ ನಿಮ್ಮ ಹೋಮ್ ಶಾಖೆಯ ಮೂಲಕ SBI ಚೆಕ್ ಪುಸ್ತಕವನ್ನು ವಿನಂತಿಸಬಹುದು.",
    "hi": "आप YONO SBI, इंटरनेट बैंकिंग, ATM या अपनी होम शाखा के माध्यम से SBI चेक बुक का अनुरोध कर सकते हैं।"
}

banking_faqs["net banking"] = {
    "en": "You can register for SBI Internet Banking through the official OnlineSBI portal or by contacting your SBI branch.",
    "kn": "ನೀವು ಅಧಿಕೃತ OnlineSBI ಪೋರ್ಟಲ್ ಮೂಲಕ ಅಥವಾ SBI ಶಾಖೆಯನ್ನು ಸಂಪರ್ಕಿಸಿ SBI Internet Banking ಗೆ ನೋಂದಾಯಿಸಬಹುದು.",
    "hi": "आप आधिकारिक OnlineSBI पोर्टल या SBI शाखा से संपर्क करके SBI इंटरनेट बैंकिंग के लिए पंजीकरण कर सकते हैं।"
}

follow_up_answers["credit card"] = {
    "eligibility": {
        "en": "Eligibility depends on income, credit profile, employment type, age, and SBI Card policy.",
        "kn": "ಅರ್ಹತೆ ಆದಾಯ, ಕ್ರೆಡಿಟ್ ಪ್ರೊಫೈಲ್, ಉದ್ಯೋಗ ಪ್ರಕಾರ, ವಯಸ್ಸು ಮತ್ತು SBI Card ನೀತಿಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ.",
        "hi": "पात्रता आय, क्रेडिट प्रोफाइल, रोजगार प्रकार, आयु और SBI Card नीति पर निर्भर करती है।"
    },
    "documents": {
        "en": "You may need identity proof, address proof, income proof, PAN, and a recent photograph.",
        "kn": "ಗುರುತಿನ ದಾಖಲೆ, ವಿಳಾಸದ ದಾಖಲೆ, ಆದಾಯದ ದಾಖಲೆ, PAN ಮತ್ತು ಇತ್ತೀಚಿನ ಫೋಟೋ ಬೇಕಾಗಬಹುದು.",
        "hi": "आपको पहचान प्रमाण, पता प्रमाण, आय प्रमाण, PAN और हाल की फोटो की जरूरत हो सकती है।"
    },
    "annual_fee": {
        "en": "Annual fees vary by card type. Please check official SBI Card details before applying.",
        "kn": "ವಾರ್ಷಿಕ ಶುಲ್ಕ ಕಾರ್ಡ್ ಪ್ರಕಾರದಂತೆ ಬದಲಾಗುತ್ತದೆ. ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು ಅಧಿಕೃತ SBI Card ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "hi": "वार्षिक शुल्क कार्ड प्रकार के अनुसार अलग होता है। आवेदन से पहले आधिकारिक SBI Card विवरण देखें।"
    },
    "credit_limit": {
        "en": "Credit limit is assigned based on eligibility, income, repayment history, and SBI Card policy.",
        "kn": "ಕ್ರೆಡಿಟ್ ಮಿತಿ ಅರ್ಹತೆ, ಆದಾಯ, ಮರುಪಾವತಿ ಇತಿಹಾಸ ಮತ್ತು SBI Card ನೀತಿಯ ಆಧಾರದ ಮೇಲೆ ನೀಡಲಾಗುತ್ತದೆ.",
        "hi": "क्रेडिट लिमिट पात्रता, आय, पुनर्भुगतान इतिहास और SBI Card नीति के आधार पर दी जाती है।"
    },
    "billing_cycle": {
        "en": "Your billing cycle and due date are shown in your SBI Card statement and mobile app.",
        "kn": "ನಿಮ್ಮ ಬಿಲ್ಲಿಂಗ್ ಸೈಕಲ್ ಮತ್ತು ಪಾವತಿ ದಿನಾಂಕವು SBI Card ಸ್ಟೇಟ್ಮೆಂಟ್ ಮತ್ತು ಮೊಬೈಲ್ ಆ್ಯಪ್‌ನಲ್ಲಿ ಕಾಣುತ್ತದೆ.",
        "hi": "आपका बिलिंग साइकिल और देय तिथि SBI Card स्टेटमेंट और मोबाइल ऐप में दिखाई देती है।"
    }
}

follow_up_answers["fixed deposit"] = {
    "interest": {
        "en": "FD interest rates can change. Please check official SBI channels for the latest applicable rate.",
        "kn": "FD ಬಡ್ಡಿದರಗಳು ಬದಲಾಗಬಹುದು. ಇತ್ತೀಚಿನ ಅನ್ವಯಿಸುವ ದರಕ್ಕಾಗಿ ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "hi": "FD ब्याज दरें बदल सकती हैं। नवीनतम लागू दर के लिए आधिकारिक SBI चैनल देखें।"
    },
    "tenure": {
        "en": "SBI fixed deposits are available for different tenures. Choose a tenure through official SBI channels.",
        "kn": "SBI ಸ್ಥಿರ ಠೇವಣಿಗಳು ವಿವಿಧ ಅವಧಿಗಳಿಗೆ ಲಭ್ಯವಿವೆ. ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳ ಮೂಲಕ ಅವಧಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "hi": "SBI फिक्स्ड डिपॉजिट अलग-अलग अवधियों के लिए उपलब्ध हैं। आधिकारिक SBI चैनलों से अवधि चुनें।"
    },
    "minimum_amount": {
        "en": "Minimum deposit amount may vary by FD type. Please confirm through YONO SBI, Internet Banking, or a branch.",
        "kn": "ಕನಿಷ್ಠ ಠೇವಣಿ ಮೊತ್ತ FD ಪ್ರಕಾರದಂತೆ ಬದಲಾಗಬಹುದು. YONO SBI, Internet Banking ಅಥವಾ ಶಾಖೆಯಲ್ಲಿ ದೃಢಪಡಿಸಿ.",
        "hi": "न्यूनतम जमा राशि FD प्रकार के अनुसार बदल सकती है। YONO SBI, इंटरनेट बैंकिंग या शाखा से पुष्टि करें।"
    },
    "premature_withdrawal": {
        "en": "Premature withdrawal may be allowed as per SBI rules and may affect interest. Check official terms first.",
        "kn": "SBI ನಿಯಮಗಳ ಪ್ರಕಾರ ಮುಂಗಡ ಹಿಂಪಡೆಯುವಿಕೆ ಸಾಧ್ಯವಾಗಬಹುದು ಮತ್ತು ಬಡ್ಡಿಗೆ ಪರಿಣಾಮ ಬೀರಬಹುದು. ಮೊದಲು ಅಧಿಕೃತ ನಿಯಮಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "hi": "SBI नियमों के अनुसार समय से पहले निकासी संभव हो सकती है और ब्याज पर असर पड़ सकता है। पहले आधिकारिक शर्तें देखें।"
    }
}

follow_up_answers["cheque book"] = {
    "apply": {
        "en": "You can apply for a cheque book through YONO SBI, Internet Banking, ATM, or your SBI branch.",
        "kn": "ನೀವು YONO SBI, Internet Banking, ATM ಅಥವಾ SBI ಶಾಖೆಯ ಮೂಲಕ ಚೆಕ್ ಪುಸ್ತಕಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.",
        "hi": "आप YONO SBI, इंटरनेट बैंकिंग, ATM या SBI शाखा के माध्यम से चेक बुक के लिए आवेदन कर सकते हैं।"
    },
    "delivery": {
        "en": "Cheque books are usually delivered to the registered address. Track status through official SBI channels.",
        "kn": "ಚೆಕ್ ಪುಸ್ತಕಗಳು ಸಾಮಾನ್ಯವಾಗಿ ನೋಂದಾಯಿತ ವಿಳಾಸಕ್ಕೆ ತಲುಪಿಸಲಾಗುತ್ತವೆ. ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳ ಮೂಲಕ ಸ್ಥಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "hi": "चेक बुक आमतौर पर पंजीकृत पते पर भेजी जाती है। आधिकारिक SBI चैनलों से स्थिति जांचें।"
    },
    "charges": {
        "en": "Cheque book charges may depend on account type and usage. Please check the latest SBI service charges.",
        "kn": "ಚೆಕ್ ಪುಸ್ತಕ ಶುಲ್ಕ ಖಾತೆ ಪ್ರಕಾರ ಮತ್ತು ಬಳಕೆಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರಬಹುದು. ಇತ್ತೀಚಿನ SBI ಸೇವಾ ಶುಲ್ಕಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "hi": "चेक बुक शुल्क खाते के प्रकार और उपयोग पर निर्भर कर सकता है। नवीनतम SBI सेवा शुल्क देखें।"
    }
}

follow_up_answers["net banking"] = {
    "register": {
        "en": "Register through the official OnlineSBI portal using your account details, ATM card, and registered mobile number.",
        "kn": "ನಿಮ್ಮ ಖಾತೆ ವಿವರಗಳು, ATM ಕಾರ್ಡ್ ಮತ್ತು ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ಬಳಸಿ ಅಧಿಕೃತ OnlineSBI ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನೋಂದಾಯಿಸಿ.",
        "hi": "अपने खाते के विवरण, ATM कार्ड और पंजीकृत मोबाइल नंबर से आधिकारिक OnlineSBI पोर्टल पर पंजीकरण करें।"
    },
    "forgot_password": {
        "en": "Use the Forgot Login Password option on OnlineSBI or contact your SBI branch for help.",
        "kn": "OnlineSBI ಯ Forgot Login Password ಆಯ್ಕೆಯನ್ನು ಬಳಸಿ ಅಥವಾ ಸಹಾಯಕ್ಕಾಗಿ SBI ಶಾಖೆಯನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "hi": "OnlineSBI पर Forgot Login Password विकल्प का उपयोग करें या सहायता के लिए SBI शाखा से संपर्क करें।"
    },
    "forgot_username": {
        "en": "Use the Forgot Username option on OnlineSBI and verify with your registered details.",
        "kn": "OnlineSBI ಯ Forgot Username ಆಯ್ಕೆಯನ್ನು ಬಳಸಿ ಮತ್ತು ನಿಮ್ಮ ನೋಂದಾಯಿತ ವಿವರಗಳೊಂದಿಗೆ ಪರಿಶೀಲಿಸಿ.",
        "hi": "OnlineSBI पर Forgot Username विकल्प का उपयोग करें और अपने पंजीकृत विवरण से सत्यापन करें।"
    },
    "unlock_account": {
        "en": "Use the unlock option on OnlineSBI or contact SBI support if your Internet Banking access is locked.",
        "kn": "ನಿಮ್ಮ Internet Banking ಪ್ರವೇಶ ಲಾಕ್ ಆಗಿದ್ದರೆ OnlineSBI ಯ unlock ಆಯ್ಕೆಯನ್ನು ಬಳಸಿ ಅಥವಾ SBI ಸಹಾಯವನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "hi": "यदि आपका इंटरनेट बैंकिंग एक्सेस लॉक है, तो OnlineSBI पर unlock विकल्प का उपयोग करें या SBI सहायता से संपर्क करें।"
    }
}
keywords["password"] = list(dict.fromkeys(keywords["password"] + [
    "i forgot my password",
    "forgot login password",
    "forgot yono password",
    "forgot internet banking password",
    "reset my password",
    "reset login password",
    "change password",
    "password change",
    "can't login",
    "cannot login",
    "login issue",
    "login problem",
    "login failed",
    "account locked",
    "locked account",
    "unlock login",
    "yono login issue",
    "net banking password",
    "profile password",
    "transaction password",
    "password not working",
    "password marethu hogide",
    "nange password reset madbeku",
    "login agtilla",
    "password reset madbeku",
    "mera password bhul gaya",
    "password bhool gaya",
    "login nahi ho raha",
    "password reset karna hai"
]))

keywords["balance"] = list(dict.fromkeys(keywords["balance"] + [
    "check my balance",
    "check bank balance",
    "show account balance",
    "how much money is in my account",
    "available balance",
    "current balance",
    "savings balance",
    "mini statement",
    "account statement",
    "balance enquiry",
    "balance inquiry",
    "sms balance",
    "missed call balance",
    "yono balance",
    "atm balance",
    "internet banking balance",
    "passbook balance",
    "balance not showing",
    "balance update",
    "nanna balance eshtu",
    "balance nodbeku",
    "balance check madbeku",
    "account alli eshtu ide",
    "mera balance kitna hai",
    "balance dekhna hai",
    "khate ka balance",
    "paise kitne hai"
]))

keywords["debit card"] = list(dict.fromkeys(keywords["debit card"] + [
    "atm card",
    "sbi debit card",
    "sbi atm card",
    "block debit card",
    "block atm card",
    "lost debit card",
    "lost atm card",
    "stolen card",
    "card stolen",
    "replace debit card",
    "new debit card",
    "apply debit card",
    "debit card delivery",
    "atm card delivery",
    "card not received",
    "card pin",
    "generate atm pin",
    "pin generation",
    "green pin",
    "debit card limit",
    "international debit card",
    "enable international usage",
    "online transaction enable",
    "card declined",
    "card not working",
    "card kaledhoythu",
    "atm card kaledhoythu",
    "card block madbeku",
    "hosa card beku",
    "mera card kho gaya",
    "card band nahi hua"
]))

keywords["account opening"] = list(dict.fromkeys(keywords["account opening"] + [
    "open an account",
    "open sbi savings account",
    "create savings account",
    "start new bank account",
    "sbi account open karna hai",
    "bank account kholna hai",
    "savings account kholna hai",
    "account opening form",
    "account opening online",
    "digital savings account",
    "insta savings account",
    "regular savings account",
    "basic savings bank account",
    "zero balance savings account",
    "minimum balance account",
    "student savings account",
    "senior citizen account",
    "joint savings account",
    "minor savings account",
    "kyc account opening",
    "pan required account",
    "aadhaar account opening",
    "account open madbeku",
    "hosa account madbeku",
    "savings account beku",
    "bank account tereyabeku",
    "new account madbeku",
    "nanage account beku",
    "khata kholna hai"
]))

keywords["upi"] = list(dict.fromkeys(keywords["upi"] + [
    "upi not working",
    "upi payment failed",
    "upi transaction failed",
    "upi payment pending",
    "upi money debited",
    "upi money not received",
    "amount debited but not received",
    "upi refund pending",
    "raise upi complaint",
    "upi dispute",
    "upi collect request",
    "payment request",
    "receive payment request",
    "upi pin forgot",
    "reset my upi pin",
    "change my upi pin",
    "create new upi id",
    "activate upi",
    "deactivate upi",
    "link sbi account to upi",
    "remove bank account from upi",
    "qr code payment",
    "scan and pay not working",
    "gpay payment failed",
    "phonepe transaction failed",
    "paytm upi issue",
    "nanna upi work agtilla",
    "upi madbeku",
    "upi pin marethu",
    "payment agilla",
    "paisa nahi aaya",
    "upi nahi chal raha"
]))

keywords["home loan"] = list(dict.fromkeys(keywords["home loan"] + [
    "apply for housing loan",
    "home loan apply online",
    "sbi housing loan",
    "loan to buy house",
    "loan to buy flat",
    "home loan emi calculator",
    "emi amount",
    "loan repayment",
    "home loan tenure",
    "home loan processing time",
    "home loan processing fee",
    "home loan sanction",
    "loan approval status",
    "property verification",
    "home loan documents required",
    "salary slip home loan",
    "itr home loan",
    "cibil home loan",
    "home loan subsidy",
    "home loan balance transfer",
    "top up loan",
    "home loan prepayment",
    "loan foreclosure",
    "mane loan madbeku",
    "mane kharidi loan",
    "home loan beku",
    "emi eshtu barutte",
    "ghar ke liye loan",
    "home loan lena hai",
    "ghar ka loan chahiye"
]))

keywords["credit card"] = list(dict.fromkeys(keywords["credit card"] + [
    "apply sbi credit card",
    "sbi card apply",
    "credit card apply online",
    "credit card approval",
    "credit card rejected",
    "credit card limit increase",
    "increase card limit",
    "temporary credit limit",
    "credit card outstanding",
    "total amount due",
    "minimum amount due",
    "card payment failed",
    "credit card due date",
    "statement date",
    "billing date",
    "card rewards",
    "reward points redeem",
    "cashback card",
    "card annual charges",
    "card renewal fee",
    "block credit card",
    "lost credit card",
    "replace credit card",
    "credit card pin",
    "card madbeku",
    "credit card apply madbeku",
    "cc limit eshtu",
    "card bill pay madbeku",
    "credit card chahiye",
    "card ka bill"
]))

keywords["fixed deposit"] = list(dict.fromkeys(keywords["fixed deposit"] + [
    "open fixed deposit",
    "make fd",
    "start fd",
    "online fd",
    "yono fd",
    "internet banking fd",
    "fd booking",
    "fd deposit",
    "term deposit receipt",
    "tdr",
    "stdr",
    "fd calculator",
    "monthly interest fd",
    "quarterly interest fd",
    "cumulative fd",
    "non cumulative fd",
    "fd maturity date",
    "fd maturity value",
    "auto renewal fd",
    "fd lien",
    "loan against fd",
    "close fixed deposit",
    "break fixed deposit",
    "tax saver deposit",
    "fd madbeku",
    "fd open madbeku",
    "deposit beku",
    "fd eshtu interest",
    "fd kholna hai",
    "fixed deposit karna hai"
]))

keywords["cheque book"] = list(dict.fromkeys(keywords["cheque book"] + [
    "chequebook",
    "checkbook",
    "issue cheque book",
    "order cheque book",
    "cheque book apply online",
    "cheque book through yono",
    "cheque book internet banking",
    "cheque book request status",
    "cheque book dispatch",
    "cheque book tracking",
    "cheque book not delivered",
    "cheque book address",
    "cheque book pages",
    "25 leaves cheque book",
    "50 leaves cheque book",
    "cheque leaf request",
    "new cheque leaves",
    "personalized cheque book",
    "non personalized cheque book",
    "cheque stop payment",
    "stop cheque payment",
    "cheque return",
    "cheque bounce",
    "cheque book madbeku",
    "cheque leaves beku",
    "check book beku",
    "cheque book yavaga barutte",
    "cheque book chahiye",
    "check book mangwana hai"
]))

keywords["net banking"] = list(dict.fromkeys(keywords["net banking"] + [
    "internet banking activate karna hai",
    "online sbi login",
    "onlinesbi login",
    "retail internet banking",
    "corporate internet banking",
    "new user registration",
    "first time login",
    "login password reset",
    "profile password reset",
    "forgot profile password",
    "forgot transaction password",
    "change username",
    "user id forgot",
    "username not working",
    "invalid username",
    "invalid password",
    "captcha issue",
    "otp not received login",
    "net banking locked",
    "unlock internet banking",
    "enable transaction rights",
    "view rights",
    "full transaction rights",
    "net banking madbeku",
    "online banking madbeku",
    "login password marethu",
    "user id marethu",
    "net banking nahi chal raha",
    "internet banking password bhul gaya"
]))

banking_faqs["password"] = {
    "en": "You can reset your SBI login password through YONO SBI or the official OnlineSBI portal. Use only official SBI channels.",
    "kn": "YONO SBI ಅಥವಾ ಅಧಿಕೃತ OnlineSBI ಪೋರ್ಟಲ್ ಮೂಲಕ ನಿಮ್ಮ SBI ಲಾಗಿನ್ ಪಾಸ್ವರ್ಡ್ ಮರುಹೊಂದಿಸಬಹುದು. ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳನ್ನು ಮಾತ್ರ ಬಳಸಿ.",
    "hi": "आप YONO SBI या आधिकारिक OnlineSBI पोर्टल से अपना SBI लॉगिन पासवर्ड रीसेट कर सकते हैं। केवल आधिकारिक SBI चैनलों का उपयोग करें।"
}

banking_faqs["balance"] = {
    "en": "You can check your SBI account balance through YONO SBI, ATM, Internet Banking, SMS Banking, or passbook update.",
    "kn": "YONO SBI, ATM, Internet Banking, SMS Banking ಅಥವಾ ಪಾಸ್ಬುಕ್ ಅಪ್‌ಡೇಟ್ ಮೂಲಕ ನಿಮ್ಮ SBI ಖಾತೆ ಬ್ಯಾಲೆನ್ಸ್ ಪರಿಶೀಲಿಸಬಹುದು.",
    "hi": "आप YONO SBI, ATM, इंटरनेट बैंकिंग, SMS बैंकिंग या पासबुक अपडेट से अपना SBI खाता बैलेंस देख सकते हैं।"
}

banking_faqs["debit card"] = {
    "en": "You can manage, block, replace, or generate a PIN for your SBI debit card through YONO SBI, Internet Banking, ATM, or an SBI branch.",
    "kn": "YONO SBI, Internet Banking, ATM ಅಥವಾ SBI ಶಾಖೆಯ ಮೂಲಕ ನಿಮ್ಮ SBI ಡೆಬಿಟ್ ಕಾರ್ಡ್ ನಿರ್ವಹಣೆ, ಬ್ಲಾಕ್, ಬದಲಾವಣೆ ಅಥವಾ PIN ರಚನೆ ಮಾಡಬಹುದು.",
    "hi": "आप YONO SBI, इंटरनेट बैंकिंग, ATM या SBI शाखा से अपना SBI डेबिट कार्ड मैनेज, ब्लॉक, बदल या PIN जनरेट कर सकते हैं।"
}

banking_faqs["account opening"] = {
    "en": "You can start SBI account opening through YONO SBI or visit a nearby SBI branch with valid KYC documents.",
    "kn": "ಮಾನ್ಯ KYC ದಾಖಲೆಗಳೊಂದಿಗೆ YONO SBI ಮೂಲಕ SBI ಖಾತೆ ತೆರೆಯುವಿಕೆಯನ್ನು ಪ್ರಾರಂಭಿಸಬಹುದು ಅಥವಾ ಸಮೀಪದ SBI ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಬಹುದು.",
    "hi": "आप वैध KYC दस्तावेजों के साथ YONO SBI से खाता खोलना शुरू कर सकते हैं या नजदीकी SBI शाखा जा सकते हैं।"
}

banking_faqs["upi"] = {
    "en": "You can use SBI UPI through YONO SBI or supported UPI apps for secure payments, transfers, and QR transactions.",
    "kn": "ಸುರಕ್ಷಿತ ಪಾವತಿ, ವರ್ಗಾವಣೆ ಮತ್ತು QR ವ್ಯವಹಾರಗಳಿಗಾಗಿ YONO SBI ಅಥವಾ ಬೆಂಬಲಿತ UPI ಆ್ಯಪ್‌ಗಳ ಮೂಲಕ SBI UPI ಬಳಸಬಹುದು.",
    "hi": "आप सुरक्षित भुगतान, ट्रांसफर और QR लेनदेन के लिए YONO SBI या समर्थित UPI ऐप्स से SBI UPI का उपयोग कर सकते हैं।"
}

banking_faqs["home loan"] = {
    "en": "You can apply for an SBI home loan online or at an SBI branch. Keep income, identity, and property documents ready.",
    "kn": "SBI ಗೃಹ ಸಾಲಕ್ಕೆ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅಥವಾ SBI ಶಾಖೆಯಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು. ಆದಾಯ, ಗುರುತು ಮತ್ತು ಆಸ್ತಿ ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ.",
    "hi": "आप SBI होम लोन के लिए ऑनलाइन या SBI शाखा में आवेदन कर सकते हैं। आय, पहचान और संपत्ति दस्तावेज तैयार रखें।"
}

banking_faqs["credit card"] = {
    "en": "You can apply for an SBI credit card through official SBI Card channels. Eligibility, fees, and limits depend on the selected card.",
    "kn": "ಅಧಿಕೃತ SBI Card ಚಾನೆಲ್‌ಗಳ ಮೂಲಕ SBI ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್‌ಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು. ಅರ್ಹತೆ, ಶುಲ್ಕ ಮತ್ತು ಮಿತಿಗಳು ಆಯ್ಕೆ ಮಾಡಿದ ಕಾರ್ಡ್ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತವೆ.",
    "hi": "आप आधिकारिक SBI Card चैनलों से SBI क्रेडिट कार्ड के लिए आवेदन कर सकते हैं। पात्रता, शुल्क और सीमा चुने गए कार्ड पर निर्भर करती है।"
}

banking_faqs["fixed deposit"] = {
    "en": "You can open an SBI fixed deposit through YONO SBI, Internet Banking, or an SBI branch. Check official rates before booking.",
    "kn": "YONO SBI, Internet Banking ಅಥವಾ SBI ಶಾಖೆಯ ಮೂಲಕ SBI ಸ್ಥಿರ ಠೇವಣಿ ತೆರೆಯಬಹುದು. ಬುಕ್ ಮಾಡುವ ಮೊದಲು ಅಧಿಕೃತ ದರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
    "hi": "आप YONO SBI, इंटरनेट बैंकिंग या SBI शाखा से SBI फिक्स्ड डिपॉजिट खोल सकते हैं। बुक करने से पहले आधिकारिक दरें देखें।"
}

banking_faqs["cheque book"] = {
    "en": "You can request an SBI cheque book through YONO SBI, Internet Banking, ATM, or your home branch.",
    "kn": "YONO SBI, Internet Banking, ATM ಅಥವಾ ನಿಮ್ಮ ಹೋಮ್ ಶಾಖೆಯ ಮೂಲಕ SBI ಚೆಕ್ ಪುಸ್ತಕವನ್ನು ವಿನಂತಿಸಬಹುದು.",
    "hi": "आप YONO SBI, इंटरनेट बैंकिंग, ATM या अपनी होम शाखा से SBI चेक बुक का अनुरोध कर सकते हैं।"
}

banking_faqs["net banking"] = {
    "en": "You can register, reset credentials, or unlock SBI Internet Banking through the official OnlineSBI portal or your SBI branch.",
    "kn": "ಅಧಿಕೃತ OnlineSBI ಪೋರ್ಟಲ್ ಅಥವಾ SBI ಶಾಖೆಯ ಮೂಲಕ SBI Internet Banking ನೋಂದಣಿ, ಪಾಸ್ವರ್ಡ್ ಮರುಹೊಂದಿಕೆ ಅಥವಾ ಅನ್‌ಲಾಕ್ ಮಾಡಬಹುದು.",
    "hi": "आप आधिकारिक OnlineSBI पोर्टल या SBI शाखा से SBI इंटरनेट बैंकिंग रजिस्टर, रीसेट या अनलॉक कर सकते हैं।"
}

follow_up_answers["password"] = {
    **follow_up_answers.get("password", {}),
    "branch": {
        "en": "Visit your SBI branch with identity proof if online reset is not working.",
        "kn": "ಆನ್‌ಲೈನ್ ಮರುಹೊಂದಿಕೆ ಕೆಲಸ ಮಾಡದಿದ್ದರೆ ಗುರುತಿನ ದಾಖಲೆ ಜೊತೆಗೆ SBI ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಿ.",
        "hi": "यदि ऑनलाइन रीसेट काम नहीं कर रहा है, तो पहचान प्रमाण के साथ SBI शाखा जाएं।"
    },
    "mobile": {
        "en": "You can reset many passwords through YONO SBI using your registered mobile number.",
        "kn": "ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ಬಳಸಿ YONO SBI ಮೂಲಕ ಹಲವು ಪಾಸ್ವರ್ಡ್‌ಗಳನ್ನು ಮರುಹೊಂದಿಸಬಹುದು.",
        "hi": "आप अपने पंजीकृत मोबाइल नंबर से YONO SBI पर कई पासवर्ड रीसेट कर सकते हैं।"
    },
    "documents": {
        "en": "For branch help, carry identity proof, account details, and your registered mobile number.",
        "kn": "ಶಾಖೆ ಸಹಾಯಕ್ಕಾಗಿ ಗುರುತಿನ ದಾಖಲೆ, ಖಾತೆ ವಿವರಗಳು ಮತ್ತು ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ತೆಗೆದುಕೊಂಡು ಹೋಗಿ.",
        "hi": "शाखा सहायता के लिए पहचान प्रमाण, खाता विवरण और पंजीकृत मोबाइल नंबर साथ रखें।"
    },
    "locked_account": {
        "en": "Use the unlock option on the official portal or contact SBI if your login is locked.",
        "kn": "ಲಾಗಿನ್ ಲಾಕ್ ಆಗಿದ್ದರೆ ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ನ unlock ಆಯ್ಕೆಯನ್ನು ಬಳಸಿ ಅಥವಾ SBI ಸಂಪರ್ಕಿಸಿ.",
        "hi": "लॉगिन लॉक होने पर आधिकारिक पोर्टल पर unlock विकल्प उपयोग करें या SBI से संपर्क करें।"
    }
}

follow_up_answers["balance"] = {
    **follow_up_answers.get("balance", {}),
    "online": {
        "en": "Yes. You can check balance online through YONO SBI or Internet Banking.",
        "kn": "ಹೌದು. YONO SBI ಅಥವಾ Internet Banking ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಬ್ಯಾಲೆನ್ಸ್ ಪರಿಶೀಲಿಸಬಹುದು.",
        "hi": "हाँ। आप YONO SBI या इंटरनेट बैंकिंग से ऑनलाइन बैलेंस देख सकते हैं।"
    },
    "atm": {
        "en": "Use any SBI ATM balance enquiry option with your debit card and PIN.",
        "kn": "ನಿಮ್ಮ ಡೆಬಿಟ್ ಕಾರ್ಡ್ ಮತ್ತು PIN ಬಳಸಿ SBI ATM ನಲ್ಲಿ balance enquiry ಆಯ್ಕೆಮಾಡಿ.",
        "hi": "अपने डेबिट कार्ड और PIN से SBI ATM पर balance enquiry विकल्प चुनें।"
    },
    "sms": {
        "en": "SMS or missed-call balance services require your mobile number to be registered with SBI.",
        "kn": "SMS ಅಥವಾ missed-call ಬ್ಯಾಲೆನ್ಸ್ ಸೇವೆಗೆ ನಿಮ್ಮ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ SBI ನಲ್ಲಿ ನೋಂದಾಯಿತವಾಗಿರಬೇಕು.",
        "hi": "SMS या missed-call बैलेंस सेवा के लिए आपका मोबाइल नंबर SBI में पंजीकृत होना चाहिए।"
    },
    "statement": {
        "en": "For detailed transactions, use mini statement, account statement, passbook, or Internet Banking.",
        "kn": "ವಿವರವಾದ ವ್ಯವಹಾರಗಳಿಗೆ mini statement, account statement, passbook ಅಥವಾ Internet Banking ಬಳಸಿ.",
        "hi": "विस्तृत लेनदेन के लिए mini statement, account statement, passbook या इंटरनेट बैंकिंग उपयोग करें।"
    }
}

follow_up_answers["debit card"] = {
    **follow_up_answers.get("debit card", {}),
    "block": {
        "en": "Block a lost debit card immediately through YONO SBI, Internet Banking, customer care, or an SBI branch.",
        "kn": "ಕಳೆದುಹೋದ ಡೆಬಿಟ್ ಕಾರ್ಡ್ ಅನ್ನು YONO SBI, Internet Banking, customer care ಅಥವಾ SBI ಶಾಖೆಯ ಮೂಲಕ ತಕ್ಷಣ ಬ್ಲಾಕ್ ಮಾಡಿ.",
        "hi": "खोया हुआ डेबिट कार्ड YONO SBI, इंटरनेट बैंकिंग, customer care या SBI शाखा से तुरंत ब्लॉक करें।"
    },
    "replace": {
        "en": "You can request a replacement debit card through official SBI channels after blocking or expiry.",
        "kn": "ಬ್ಲಾಕ್ ಅಥವಾ ಅವಧಿ ಮುಗಿದ ನಂತರ ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳ ಮೂಲಕ ಬದಲಾವಣೆ ಡೆಬಿಟ್ ಕಾರ್ಡ್ ವಿನಂತಿಸಬಹುದು.",
        "hi": "ब्लॉक या expiry के बाद आप आधिकारिक SBI चैनलों से replacement debit card मांग सकते हैं।"
    },
    "international_usage": {
        "en": "International usage can be managed through YONO SBI or Internet Banking if available for your card.",
        "kn": "ನಿಮ್ಮ ಕಾರ್ಡ್‌ಗೆ ಲಭ್ಯವಿದ್ದರೆ YONO SBI ಅಥವಾ Internet Banking ಮೂಲಕ international usage ನಿರ್ವಹಿಸಬಹುದು.",
        "hi": "आपके कार्ड के लिए उपलब्ध होने पर international usage YONO SBI या इंटरनेट बैंकिंग से मैनेज किया जा सकता है।"
    },
    "pin_generation": {
        "en": "Generate or reset your ATM PIN through SBI ATM, YONO SBI, or other official SBI options.",
        "kn": "SBI ATM, YONO SBI ಅಥವಾ ಇತರ ಅಧಿಕೃತ SBI ಆಯ್ಕೆಗಳ ಮೂಲಕ ATM PIN ರಚಿಸಿ ಅಥವಾ ಮರುಹೊಂದಿಸಿ.",
        "hi": "SBI ATM, YONO SBI या अन्य आधिकारिक SBI विकल्पों से ATM PIN बनाएं या रीसेट करें।"
    },
    "delivery": {
        "en": "Debit card delivery status can be checked through official SBI channels or your home branch.",
        "kn": "ಡೆಬಿಟ್ ಕಾರ್ಡ್ ವಿತರಣಾ ಸ್ಥಿತಿಯನ್ನು ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳು ಅಥವಾ ಹೋಮ್ ಶಾಖೆಯ ಮೂಲಕ ಪರಿಶೀಲಿಸಬಹುದು.",
        "hi": "डेबिट कार्ड delivery status आधिकारिक SBI चैनलों या home branch से जांचा जा सकता है।"
    }
}

follow_up_answers["account opening"] = {
    **follow_up_answers.get("account opening", {}),
    "zero_balance": {
        "en": "Some account types may have relaxed balance requirements. Confirm the current rules through official SBI channels.",
        "kn": "ಕೆಲವು ಖಾತೆ ಪ್ರಕಾರಗಳಲ್ಲಿ ಕಡಿಮೆ ಬ್ಯಾಲೆನ್ಸ್ ನಿಯಮಗಳು ಇರಬಹುದು. ಪ್ರಸ್ತುತ ನಿಯಮಗಳನ್ನು ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳಿಂದ ದೃಢಪಡಿಸಿ.",
        "hi": "कुछ खाता प्रकारों में कम balance requirements हो सकती हैं। वर्तमान नियम आधिकारिक SBI चैनलों से確認 करें।"
    },
    "minimum_balance": {
        "en": "Minimum balance rules depend on account type and location. Please check official SBI service terms.",
        "kn": "ಕನಿಷ್ಠ ಬ್ಯಾಲೆನ್ಸ್ ನಿಯಮಗಳು ಖಾತೆ ಪ್ರಕಾರ ಮತ್ತು ಸ್ಥಳದ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತವೆ. ಅಧಿಕೃತ SBI ನಿಯಮಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "hi": "Minimum balance नियम खाता प्रकार और स्थान पर निर्भर करते हैं। आधिकारिक SBI सेवा शर्तें देखें।"
    },
    "online_opening": {
        "en": "You can start account opening online through YONO SBI where available, subject to KYC verification.",
        "kn": "ಲಭ್ಯವಿರುವಲ್ಲಿ KYC ಪರಿಶೀಲನೆಗೆ ಒಳಪಟ್ಟು YONO SBI ಮೂಲಕ ಆನ್‌ಲೈನ್ ಖಾತೆ ತೆರೆಯುವಿಕೆಯನ್ನು ಪ್ರಾರಂಭಿಸಬಹುದು.",
        "hi": "जहां उपलब्ध हो, KYC verification के अधीन YONO SBI से online account opening शुरू कर सकते हैं।"
    }
}

follow_up_answers["upi"] = {
    **follow_up_answers.get("upi", {}),
    "reset_pin": {
        "en": "Reset your UPI PIN only inside YONO SBI or a trusted UPI app using official verification steps.",
        "kn": "ಅಧಿಕೃತ ಪರಿಶೀಲನಾ ಹಂತಗಳನ್ನು ಬಳಸಿ YONO SBI ಅಥವಾ ವಿಶ್ವಾಸಾರ್ಹ UPI ಆ್ಯಪ್‌ನಲ್ಲೇ UPI PIN ಮರುಹೊಂದಿಸಿ.",
        "hi": "UPI PIN केवल YONO SBI या trusted UPI app में official verification steps से रीसेट करें।"
    },
    "transaction_failed": {
        "en": "If a UPI transaction fails, check status in the app and wait for reversal before raising a complaint.",
        "kn": "UPI ವ್ಯವಹಾರ ವಿಫಲವಾದರೆ ಆ್ಯಪ್‌ನಲ್ಲಿ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಿ ಮತ್ತು ದೂರು ನೀಡುವ ಮೊದಲು reversal ಗಾಗಿ ಕಾಯಿರಿ.",
        "hi": "UPI transaction fail होने पर app में status देखें और complaint से पहले reversal का इंतजार करें।"
    },
    "payment_pending": {
        "en": "Pending UPI payments may take time to update. Track status through the app or official SBI support.",
        "kn": "Pending UPI ಪಾವತಿಗಳು update ಆಗಲು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳಬಹುದು. ಆ್ಯಪ್ ಅಥವಾ ಅಧಿಕೃತ SBI support ಮೂಲಕ ಸ್ಥಿತಿ ನೋಡಿ.",
        "hi": "Pending UPI payments update होने में समय लग सकता है। app या official SBI support से status देखें।"
    },
    "refund": {
        "en": "Refund timelines depend on the transaction status and UPI app. Use official complaint options if delayed.",
        "kn": "Refund ಸಮಯ ವ್ಯವಹಾರ ಸ್ಥಿತಿ ಮತ್ತು UPI ಆ್ಯಪ್ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ. ವಿಳಂಬವಾದರೆ ಅಧಿಕೃತ complaint ಆಯ್ಕೆಯನ್ನು ಬಳಸಿ.",
        "hi": "Refund समय transaction status और UPI app पर निर्भर करता है। देरी होने पर official complaint option उपयोग करें।"
    }
}

follow_up_answers["home loan"] = {
    **follow_up_answers.get("home loan", {}),
    "tenure": {
        "en": "Home loan tenure depends on eligibility, age, repayment capacity, and SBI policy.",
        "kn": "ಗೃಹ ಸಾಲ ಅವಧಿ ಅರ್ಹತೆ, ವಯಸ್ಸು, ಮರುಪಾವತಿ ಸಾಮರ್ಥ್ಯ ಮತ್ತು SBI ನೀತಿಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ.",
        "hi": "Home loan tenure पात्रता, आयु, repayment capacity और SBI policy पर निर्भर करता है।"
    },
    "emi": {
        "en": "EMI depends on loan amount, rate, and tenure. Use SBI's official calculator for an estimate.",
        "kn": "EMI ಸಾಲ ಮೊತ್ತ, ದರ ಮತ್ತು ಅವಧಿಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ. ಅಂದಾಜಿಗೆ SBI ಅಧಿಕೃತ calculator ಬಳಸಿ.",
        "hi": "EMI loan amount, rate और tenure पर निर्भर करती है। estimate के लिए SBI का official calculator उपयोग करें।"
    },
    "processing_time": {
        "en": "Processing time depends on document verification, eligibility checks, and property review.",
        "kn": "ಪ್ರಕ್ರಿಯೆ ಸಮಯ ದಾಖಲೆ ಪರಿಶೀಲನೆ, ಅರ್ಹತೆ ಪರಿಶೀಲನೆ ಮತ್ತು ಆಸ್ತಿ ಪರಿಶೀಲನೆಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ.",
        "hi": "Processing time document verification, eligibility checks और property review पर निर्भर करता है।"
    }
}
follow_up_answers["fixed deposit"] = {
    **follow_up_answers.get("fixed deposit", {}),
    "tax": {
        "en": "Tax treatment can depend on deposit type and customer profile. Please check official SBI details or consult a tax professional.",
        "kn": "ತೆರಿಗೆ ನಿಯಮಗಳು ಠೇವಣಿ ಪ್ರಕಾರ ಮತ್ತು ಗ್ರಾಹಕರ ವಿವರಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರಬಹುದು. ಅಧಿಕೃತ SBI ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಅಥವಾ ತೆರಿಗೆ ತಜ್ಞರನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "hi": "Tax treatment deposit type और customer profile पर निर्भर हो सकता है। official SBI details देखें या tax professional से सलाह लें।"
    }
}

follow_up_answers["cheque book"] = {
    **follow_up_answers.get("cheque book", {}),
    "tracking": {
        "en": "Track cheque book status through YONO SBI, Internet Banking, or your home branch.",
        "kn": "YONO SBI, Internet Banking ಅಥವಾ ನಿಮ್ಮ ಹೋಮ್ ಶಾಖೆಯ ಮೂಲಕ cheque book status ಪರಿಶೀಲಿಸಿ.",
        "hi": "Cheque book status YONO SBI, इंटरनेट बैंकिंग या home branch से track करें।"
    }
}

follow_up_answers["net banking"] = {
    **follow_up_answers.get("net banking", {}),
    "registration": {
        "en": "Register through the official OnlineSBI portal using your account details, ATM card, and registered mobile number.",
        "kn": "ಖಾತೆ ವಿವರಗಳು, ATM ಕಾರ್ಡ್ ಮತ್ತು ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯೊಂದಿಗೆ ಅಧಿಕೃತ OnlineSBI ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನೋಂದಾಯಿಸಿ.",
        "hi": "Account details, ATM card और registered mobile number से official OnlineSBI portal पर registration करें।"
    },
    "activation": {
        "en": "Activate Internet Banking only through OnlineSBI or your SBI branch after completing verification.",
        "kn": "ಪರಿಶೀಲನೆ ಪೂರ್ಣಗೊಂಡ ನಂತರ OnlineSBI ಅಥವಾ SBI ಶಾಖೆಯ ಮೂಲಕ ಮಾತ್ರ Internet Banking ಸಕ್ರಿಯಗೊಳಿಸಿ.",
        "hi": "Verification पूरा करने के बाद Internet Banking केवल OnlineSBI या SBI branch से activate करें।"
    }
}
def _add_keywords(intent, new_keywords):
    keywords[intent] = list(dict.fromkeys(keywords.get(intent, []) + new_keywords))


_add_keywords("password", [
    "how do i reset my sbi password",
    "yono password forgot",
    "internet banking password forgot",
    "unable to login yono",
    "my sbi login is locked",
    "need help with login password",
    "password tappagide",
    "password gothilla",
    "login madakke agtilla",
    "password yaad nahi hai",
    "sbi login nahi khul raha",
    "password galat bata raha hai"
])

_add_keywords("balance", [
    "how to check sbi balance",
    "can you show my balance",
    "need account balance",
    "bank balance check karna hai",
    "balance enquiry number",
    "registered mobile balance check",
    "passbook update balance",
    "balance gothagbeku",
    "balance nodoke help madi",
    "khate mein kitna paisa hai",
    "mera account balance batao"
])

_add_keywords("debit card", [
    "how to block my debit card",
    "atm card block karna hai",
    "debit card replacement request",
    "debit card pin reset",
    "atm pin bhul gaya",
    "enable online transaction debit card",
    "disable debit card usage",
    "card lost help",
    "atm card sigtilla",
    "card pin marethu",
    "atm card block madbeku",
    "mera atm card kho gaya"
])

_add_keywords("account opening", [
    "how do i open sbi account",
    "can i open account online",
    "sbi account opening documents",
    "minimum balance for sbi account",
    "zero balance account sbi",
    "open account without visiting branch",
    "savings account application status",
    "account tereyodu hege",
    "hosa savings account beku",
    "account kholne ke documents",
    "online khata kholna hai"
])

_add_keywords("upi", [
    "how to create upi in sbi",
    "upi id create karna hai",
    "upi pin reset karna hai",
    "payment deducted but not received",
    "upi complaint raise karna hai",
    "qr scan payment failed",
    "collect request fraud",
    "upi limit kitna hai",
    "upi setup madbeku",
    "upi payment pending ide",
    "gpay alli sbi account link madbeku",
    "upi paisa atak gaya"
])

_add_keywords("home loan", [
    "how to apply sbi home loan",
    "home loan documents required",
    "home loan eligibility check",
    "home loan emi estimate",
    "home loan processing status",
    "property loan documents",
    "housing loan interest rate",
    "home loan branch appointment",
    "mane loan eligibility",
    "mane loan documents",
    "ghar loan ke documents",
    "home loan ka emi"
])

_add_keywords("credit card", [
    "how to apply sbi credit card",
    "credit card eligibility check",
    "credit card documents required",
    "credit card bill payment",
    "credit card statement download",
    "credit card rewards redeem",
    "increase sbi card limit",
    "credit card annual charges",
    "sbi card bill bharna hai",
    "credit card limit kitna hai",
    "credit card apply madbeku",
    "card reward points hege"
])

_add_keywords("fixed deposit", [
    "how to open sbi fd",
    "fd interest rate today",
    "fd maturity details",
    "fd premature closure",
    "tax saver fd",
    "senior citizen fixed deposit",
    "fd renewal online",
    "fd receipt download",
    "fd open madbeku",
    "fd interest gothagbeku",
    "fd kholna hai online",
    "fd todna hai"
])

_add_keywords("cheque book", [
    "how to apply cheque book",
    "cheque book request online",
    "cheque book delivery status",
    "track my cheque book",
    "cheque book charges sbi",
    "stop cheque payment",
    "cheque book not received",
    "new cheque leaves request",
    "cheque book apply madbeku",
    "cheque book status nodbeku",
    "check book chahiye",
    "cheque stop karna hai"
])

_add_keywords("net banking", [
    "how to register sbi net banking",
    "online sbi new user registration",
    "net banking activation",
    "forgot net banking username",
    "forgot net banking password",
    "unlock online sbi account",
    "transaction rights enable",
    "profile password reset online",
    "net banking login agtilla",
    "online sbi password marethu",
    "net banking register karna hai",
    "user id bhul gaya"
])

banking_faqs["password"] = {
    "en": "You can reset your SBI password through YONO SBI or the official OnlineSBI portal. Use only official SBI channels.",
    "kn": "YONO SBI ಅಥವಾ ಅಧಿಕೃತ OnlineSBI ಪೋರ್ಟಲ್ ಮೂಲಕ ನಿಮ್ಮ SBI ಪಾಸ್ವರ್ಡ್ ಮರುಹೊಂದಿಸಬಹುದು. ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳನ್ನು ಮಾತ್ರ ಬಳಸಿ.",
    "hi": "आप YONO SBI या आधिकारिक OnlineSBI पोर्टल से अपना SBI पासवर्ड रीसेट कर सकते हैं। केवल आधिकारिक SBI चैनलों का उपयोग करें।"
}

banking_faqs["balance"] = {
    "en": "You can check your SBI balance using YONO SBI, ATM, Internet Banking, SMS Banking, or your passbook.",
    "kn": "YONO SBI, ATM, Internet Banking, SMS Banking ಅಥವಾ ಪಾಸ್ಬುಕ್ ಮೂಲಕ ನಿಮ್ಮ SBI ಬ್ಯಾಲೆನ್ಸ್ ಪರಿಶೀಲಿಸಬಹುದು.",
    "hi": "आप YONO SBI, ATM, इंटरनेट बैंकिंग, SMS बैंकिंग या पासबुक से अपना SBI बैलेंस देख सकते हैं।"
}

banking_faqs["debit card"] = {
    "en": "You can block, replace, manage, or generate a PIN for your SBI debit card through YONO SBI, Internet Banking, ATM, or a branch.",
    "kn": "YONO SBI, Internet Banking, ATM ಅಥವಾ ಶಾಖೆಯ ಮೂಲಕ ನಿಮ್ಮ SBI ಡೆಬಿಟ್ ಕಾರ್ಡ್ ಬ್ಲಾಕ್, ಬದಲಾವಣೆ, ನಿರ್ವಹಣೆ ಅಥವಾ PIN ರಚಿಸಬಹುದು.",
    "hi": "आप YONO SBI, इंटरनेट बैंकिंग, ATM या शाखा से अपना SBI डेबिट कार्ड ब्लॉक, बदल, मैनेज या PIN जनरेट कर सकते हैं।"
}

banking_faqs["account opening"] = {
    "en": "You can start opening an SBI account through YONO SBI or visit an SBI branch with valid KYC documents.",
    "kn": "ಮಾನ್ಯ KYC ದಾಖಲೆಗಳೊಂದಿಗೆ YONO SBI ಮೂಲಕ SBI ಖಾತೆ ತೆರೆಯುವಿಕೆಯನ್ನು ಪ್ರಾರಂಭಿಸಬಹುದು ಅಥವಾ SBI ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಬಹುದು.",
    "hi": "आप वैध KYC दस्तावेजों के साथ YONO SBI से SBI खाता खोलना शुरू कर सकते हैं या SBI शाखा जा सकते हैं।"
}

banking_faqs["upi"] = {
    "en": "You can use SBI UPI through YONO SBI or trusted UPI apps for payments, transfers, QR scans, and collect requests.",
    "kn": "ಪಾವತಿ, ವರ್ಗಾವಣೆ, QR ಸ್ಕ್ಯಾನ್ ಮತ್ತು collect request ಗಳಿಗೆ YONO SBI ಅಥವಾ ವಿಶ್ವಾಸಾರ್ಹ UPI ಆ್ಯಪ್‌ಗಳ ಮೂಲಕ SBI UPI ಬಳಸಬಹುದು.",
    "hi": "आप भुगतान, ट्रांसफर, QR scan और collect request के लिए YONO SBI या trusted UPI apps से SBI UPI उपयोग कर सकते हैं।"
}

banking_faqs["home loan"] = {
    "en": "You can apply for an SBI home loan online or at a branch. Keep income, identity, and property documents ready.",
    "kn": "SBI ಗೃಹ ಸಾಲಕ್ಕೆ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅಥವಾ ಶಾಖೆಯಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು. ಆದಾಯ, ಗುರುತು ಮತ್ತು ಆಸ್ತಿ ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ.",
    "hi": "आप SBI होम लोन के लिए ऑनलाइन या शाखा में आवेदन कर सकते हैं। आय, पहचान और संपत्ति दस्तावेज तैयार रखें।"
}

banking_faqs["credit card"] = {
    "en": "You can apply for an SBI credit card through official SBI Card channels. Fees, limits, and eligibility depend on the card type.",
    "kn": "ಅಧಿಕೃತ SBI Card ಚಾನೆಲ್‌ಗಳ ಮೂಲಕ SBI ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್‌ಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು. ಶುಲ್ಕ, ಮಿತಿ ಮತ್ತು ಅರ್ಹತೆ ಕಾರ್ಡ್ ಪ್ರಕಾರದ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತವೆ.",
    "hi": "आप आधिकारिक SBI Card चैनलों से SBI क्रेडिट कार्ड के लिए आवेदन कर सकते हैं। शुल्क, सीमा और पात्रता कार्ड प्रकार पर निर्भर करती है।"
}

banking_faqs["fixed deposit"] = {
    "en": "You can open or manage an SBI fixed deposit through YONO SBI, Internet Banking, or a branch. Check official rates before booking.",
    "kn": "YONO SBI, Internet Banking ಅಥವಾ ಶಾಖೆಯ ಮೂಲಕ SBI ಸ್ಥಿರ ಠೇವಣಿ ತೆರೆಯಬಹುದು ಅಥವಾ ನಿರ್ವಹಿಸಬಹುದು. ಬುಕ್ ಮಾಡುವ ಮೊದಲು ಅಧಿಕೃತ ದರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
    "hi": "आप YONO SBI, इंटरनेट बैंकिंग या शाखा से SBI fixed deposit खोल या मैनेज कर सकते हैं। बुक करने से पहले आधिकारिक दरें देखें।"
}

banking_faqs["cheque book"] = {
    "en": "You can request or track an SBI cheque book through YONO SBI, Internet Banking, ATM, or your home branch.",
    "kn": "YONO SBI, Internet Banking, ATM ಅಥವಾ ಹೋಮ್ ಶಾಖೆಯ ಮೂಲಕ SBI ಚೆಕ್ ಪುಸ್ತಕವನ್ನು ವಿನಂತಿಸಬಹುದು ಅಥವಾ ಟ್ರ್ಯಾಕ್ ಮಾಡಬಹುದು.",
    "hi": "आप YONO SBI, इंटरनेट बैंकिंग, ATM या home branch से SBI cheque book request या track कर सकते हैं।"
}

banking_faqs["net banking"] = {
    "en": "You can register, activate, reset, or unlock SBI Internet Banking through the official OnlineSBI portal or an SBI branch.",
    "kn": "ಅಧಿಕೃತ OnlineSBI ಪೋರ್ಟಲ್ ಅಥವಾ SBI ಶಾಖೆಯ ಮೂಲಕ SBI Internet Banking ನೋಂದಣಿ, ಸಕ್ರಿಯಗೊಳಿಸುವಿಕೆ, ಮರುಹೊಂದಿಕೆ ಅಥವಾ unlock ಮಾಡಬಹುದು.",
    "hi": "आप आधिकारिक OnlineSBI portal या SBI branch से SBI Internet Banking register, activate, reset या unlock कर सकते हैं।"
}

follow_up_answers["password"] = {
    **follow_up_answers.get("password", {}),
    "online": {
        "en": "Yes. Use YONO SBI or OnlineSBI to reset your password online with registered verification details.",
        "kn": "ಹೌದು. ನೋಂದಾಯಿತ ಪರಿಶೀಲನಾ ವಿವರಗಳೊಂದಿಗೆ YONO SBI ಅಥವಾ OnlineSBI ಮೂಲಕ ಪಾಸ್ವರ್ಡ್ ಮರುಹೊಂದಿಸಿ.",
        "hi": "हाँ। registered verification details के साथ YONO SBI या OnlineSBI से password reset करें।"
    },
    "branch": {
        "en": "Visit your SBI branch with identity proof if online reset is not working.",
        "kn": "ಆನ್‌ಲೈನ್ ಮರುಹೊಂದಿಕೆ ಕೆಲಸ ಮಾಡದಿದ್ದರೆ ಗುರುತಿನ ದಾಖಲೆ ಜೊತೆಗೆ SBI ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಿ.",
        "hi": "अगर online reset काम नहीं कर रहा है, तो identity proof के साथ SBI branch जाएं।"
    },
    "mobile": {
        "en": "Your registered mobile number is usually required for OTP verification during password reset.",
        "kn": "ಪಾಸ್ವರ್ಡ್ ಮರುಹೊಂದಿಸುವಾಗ OTP ಪರಿಶೀಲನೆಗೆ ಸಾಮಾನ್ಯವಾಗಿ ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಬೇಕಾಗುತ್ತದೆ.",
        "hi": "Password reset के दौरान OTP verification के लिए registered mobile number आमतौर पर जरूरी होता है।"
    },
    "documents": {
        "en": "For branch support, carry identity proof, account details, and your registered mobile number.",
        "kn": "ಶಾಖೆ ಸಹಾಯಕ್ಕಾಗಿ ಗುರುತಿನ ದಾಖಲೆ, ಖಾತೆ ವಿವರಗಳು ಮತ್ತು ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ತೆಗೆದುಕೊಂಡು ಹೋಗಿ.",
        "hi": "Branch support के लिए identity proof, account details और registered mobile number साथ रखें।"
    },
    "locked_account": {
        "en": "Use the unlock option on OnlineSBI or contact SBI support if your login is locked.",
        "kn": "ಲಾಗಿನ್ ಲಾಕ್ ಆಗಿದ್ದರೆ OnlineSBI ಯ unlock ಆಯ್ಕೆಯನ್ನು ಬಳಸಿ ಅಥವಾ SBI support ಸಂಪರ್ಕಿಸಿ.",
        "hi": "Login locked होने पर OnlineSBI का unlock option उपयोग करें या SBI support से संपर्क करें।"
    }
}

follow_up_answers["balance"] = {
    **follow_up_answers.get("balance", {}),
    "online": {
        "en": "Yes. You can check balance online through YONO SBI or Internet Banking.",
        "kn": "ಹೌದು. YONO SBI ಅಥವಾ Internet Banking ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಬ್ಯಾಲೆನ್ಸ್ ಪರಿಶೀಲಿಸಬಹುದು.",
        "hi": "हाँ। आप YONO SBI या Internet Banking से online balance देख सकते हैं।"
    },
    "atm": {
        "en": "Use the balance enquiry option at an SBI ATM with your debit card and PIN.",
        "kn": "ಡೆಬಿಟ್ ಕಾರ್ಡ್ ಮತ್ತು PIN ಬಳಸಿ SBI ATM ನಲ್ಲಿ balance enquiry ಆಯ್ಕೆಯನ್ನು ಬಳಸಿ.",
        "hi": "Debit card और PIN से SBI ATM पर balance enquiry option उपयोग करें।"
    },
    "sms": {
        "en": "SMS and missed-call balance services work only with your registered mobile number.",
        "kn": "SMS ಮತ್ತು missed-call ಬ್ಯಾಲೆನ್ಸ್ ಸೇವೆಗಳು ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯೊಂದಿಗೆ ಮಾತ್ರ ಕೆಲಸ ಮಾಡುತ್ತವೆ.",
        "hi": "SMS और missed-call balance services केवल registered mobile number से काम करती हैं।"
    },
    "statement": {
        "en": "For transaction details, use mini statement, account statement, passbook, or Internet Banking.",
        "kn": "ವ್ಯವಹಾರ ವಿವರಗಳಿಗೆ mini statement, account statement, passbook ಅಥವಾ Internet Banking ಬಳಸಿ.",
        "hi": "Transaction details के लिए mini statement, account statement, passbook या Internet Banking उपयोग करें।"
    },
    "branch": {
        "en": "You can also visit your SBI branch with account details for balance-related help.",
        "kn": "ಬ್ಯಾಲೆನ್ಸ್ ಸಹಾಯಕ್ಕಾಗಿ ಖಾತೆ ವಿವರಗಳೊಂದಿಗೆ SBI ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಬಹುದು.",
        "hi": "Balance help के लिए account details के साथ SBI branch भी जा सकते हैं।"
    }
}

follow_up_answers["debit card"] = {
    **follow_up_answers.get("debit card", {}),
    "block": {
        "en": "Block a lost or stolen debit card immediately through YONO SBI, Internet Banking, customer care, or a branch.",
        "kn": "ಕಳೆದುಹೋದ ಅಥವಾ ಕಳವಾದ ಡೆಬಿಟ್ ಕಾರ್ಡ್ ಅನ್ನು YONO SBI, Internet Banking, customer care ಅಥವಾ ಶಾಖೆಯ ಮೂಲಕ ತಕ್ಷಣ ಬ್ಲಾಕ್ ಮಾಡಿ.",
        "hi": "खोया या चोरी हुआ debit card YONO SBI, Internet Banking, customer care या branch से तुरंत block करें।"
    },
    "replace": {
        "en": "Request a replacement card through official SBI channels after blocking, damage, or expiry.",
        "kn": "ಬ್ಲಾಕ್, ಹಾನಿ ಅಥವಾ ಅವಧಿ ಮುಗಿದ ನಂತರ ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳ ಮೂಲಕ ಬದಲಾವಣೆ ಕಾರ್ಡ್ ವಿನಂತಿಸಿ.",
        "hi": "Block, damage या expiry के बाद official SBI channels से replacement card request करें।"
    },
    "international_usage": {
        "en": "International usage can be managed through official SBI card controls where available.",
        "kn": "ಲಭ್ಯವಿರುವಲ್ಲಿ ಅಧಿಕೃತ SBI card controls ಮೂಲಕ international usage ನಿರ್ವಹಿಸಬಹುದು.",
        "hi": "जहां उपलब्ध हो, international usage official SBI card controls से manage किया जा सकता है।"
    },
    "pin_generation": {
        "en": "Generate or reset your ATM PIN through SBI ATM, YONO SBI, or other official SBI options.",
        "kn": "SBI ATM, YONO SBI ಅಥವಾ ಇತರ ಅಧಿಕೃತ SBI ಆಯ್ಕೆಗಳ ಮೂಲಕ ATM PIN ರಚಿಸಿ ಅಥವಾ ಮರುಹೊಂದಿಸಿ.",
        "hi": "SBI ATM, YONO SBI या अन्य official SBI options से ATM PIN generate या reset करें।"
    },
    "delivery": {
        "en": "Debit card delivery status can be checked through official SBI channels or your home branch.",
        "kn": "ಡೆಬಿಟ್ ಕಾರ್ಡ್ ವಿತರಣಾ ಸ್ಥಿತಿಯನ್ನು ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳು ಅಥವಾ ಹೋಮ್ ಶಾಖೆಯ ಮೂಲಕ ಪರಿಶೀಲಿಸಬಹುದು.",
        "hi": "Debit card delivery status official SBI channels या home branch से check किया जा सकता है।"
    }
}

follow_up_answers["account opening"] = {
    **follow_up_answers.get("account opening", {}),
    "documents": {
        "en": "You usually need identity proof, address proof, PAN, photograph, and KYC details.",
        "kn": "ಸಾಮಾನ್ಯವಾಗಿ ಗುರುತಿನ ದಾಖಲೆ, ವಿಳಾಸದ ದಾಖಲೆ, PAN, ಫೋಟೋ ಮತ್ತು KYC ವಿವರಗಳು ಬೇಕಾಗುತ್ತವೆ.",
        "hi": "आम तौर पर identity proof, address proof, PAN, photo और KYC details की जरूरत होती है।"
    },
    "eligibility": {
        "en": "Eligibility depends on account type, KYC status, age, and SBI rules.",
        "kn": "ಅರ್ಹತೆ ಖಾತೆ ಪ್ರಕಾರ, KYC ಸ್ಥಿತಿ, ವಯಸ್ಸು ಮತ್ತು SBI ನಿಯಮಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ.",
        "hi": "Eligibility account type, KYC status, age और SBI rules पर निर्भर करती है।"
    },
    "zero_balance": {
        "en": "Some account types may have relaxed balance rules. Confirm current details through official SBI channels.",
        "kn": "ಕೆಲವು ಖಾತೆ ಪ್ರಕಾರಗಳಲ್ಲಿ ಸಡಿಲ ಬ್ಯಾಲೆನ್ಸ್ ನಿಯಮಗಳು ಇರಬಹುದು. ಪ್ರಸ್ತುತ ವಿವರಗಳನ್ನು ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳಿಂದ ದೃಢಪಡಿಸಿ.",
        "hi": "कुछ account types में relaxed balance rules हो सकते हैं। Current details official SBI channels से confirm करें।"
    },
    "minimum_balance": {
        "en": "Minimum balance requirements depend on account type and location.",
        "kn": "ಕನಿಷ್ಠ ಬ್ಯಾಲೆನ್ಸ್ ಅಗತ್ಯಗಳು ಖಾತೆ ಪ್ರಕಾರ ಮತ್ತು ಸ್ಥಳದ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತವೆ.",
        "hi": "Minimum balance requirements account type और location पर निर्भर करते हैं।"
    },
    "online_opening": {
        "en": "You can start account opening online through YONO SBI where available, subject to KYC verification.",
        "kn": "ಲಭ್ಯವಿರುವಲ್ಲಿ KYC ಪರಿಶೀಲನೆಗೆ ಒಳಪಟ್ಟು YONO SBI ಮೂಲಕ ಖಾತೆ ತೆರೆಯುವಿಕೆಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪ್ರಾರಂಭಿಸಬಹುದು.",
        "hi": "जहां उपलब्ध हो, KYC verification के अधीन YONO SBI से online account opening शुरू कर सकते हैं।"
    }
}

follow_up_answers["upi"] = {
    **follow_up_answers.get("upi", {}),
    "create": {
        "en": "Open YONO SBI or a trusted UPI app, select your SBI account, verify mobile number, and set a UPI PIN.",
        "kn": "YONO SBI ಅಥವಾ ವಿಶ್ವಾಸಾರ್ಹ UPI ಆ್ಯಪ್ ತೆರೆಯಿರಿ, SBI ಖಾತೆ ಆಯ್ಕೆಮಾಡಿ, ಮೊಬೈಲ್ ಪರಿಶೀಲಿಸಿ ಮತ್ತು UPI PIN ಹೊಂದಿಸಿ.",
        "hi": "YONO SBI या trusted UPI app खोलें, SBI account चुनें, mobile verify करें और UPI PIN set करें।"
    },
    "limit": {
        "en": "UPI limits vary by app, bank rules, and transaction type. Check official SBI or app limits.",
        "kn": "UPI ಮಿತಿಗಳು ಆ್ಯಪ್, ಬ್ಯಾಂಕ್ ನಿಯಮಗಳು ಮತ್ತು ವ್ಯವಹಾರ ಪ್ರಕಾರದಂತೆ ಬದಲಾಗುತ್ತವೆ. ಅಧಿಕೃತ SBI ಅಥವಾ ಆ್ಯಪ್ ಮಿತಿಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "hi": "UPI limits app, bank rules और transaction type के अनुसार बदलते हैं। official SBI या app limits देखें।"
    },
    "reset_pin": {
        "en": "Reset your UPI PIN only inside YONO SBI or a trusted UPI app using official verification.",
        "kn": "ಅಧಿಕೃತ ಪರಿಶೀಲನೆ ಬಳಸಿ YONO SBI ಅಥವಾ ವಿಶ್ವಾಸಾರ್ಹ UPI ಆ್ಯಪ್‌ನಲ್ಲೇ UPI PIN ಮರುಹೊಂದಿಸಿ.",
        "hi": "UPI PIN केवल YONO SBI या trusted UPI app में official verification से reset करें।"
    },
    "transaction_failed": {
        "en": "If a UPI transaction fails, check the app status and wait for reversal before raising a complaint.",
        "kn": "UPI ವ್ಯವಹಾರ ವಿಫಲವಾದರೆ ಆ್ಯಪ್ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಿ ಮತ್ತು ದೂರು ನೀಡುವ ಮೊದಲು reversal ಗಾಗಿ ಕಾಯಿರಿ.",
        "hi": "UPI transaction fail होने पर app status देखें और complaint से पहले reversal का इंतजार करें।"
    },
    "payment_pending": {
        "en": "Pending payments may take time to update. Track them through the UPI app or official SBI support.",
        "kn": "Pending ಪಾವತಿಗಳು update ಆಗಲು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳಬಹುದು. UPI ಆ್ಯಪ್ ಅಥವಾ ಅಧಿಕೃತ SBI support ಮೂಲಕ ಟ್ರ್ಯಾಕ್ ಮಾಡಿ.",
        "hi": "Pending payments update होने में समय लग सकता है। UPI app या official SBI support से track करें।"
    },
    "refund": {
        "en": "Refund timelines depend on transaction status and UPI app rules. Use official complaint options if delayed.",
        "kn": "Refund ಸಮಯ ವ್ಯವಹಾರ ಸ್ಥಿತಿ ಮತ್ತು UPI ಆ್ಯಪ್ ನಿಯಮಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ. ವಿಳಂಬವಾದರೆ ಅಧಿಕೃತ complaint ಆಯ್ಕೆ ಬಳಸಿ.",
        "hi": "Refund timeline transaction status और UPI app rules पर निर्भर करती है। Delay होने पर official complaint option उपयोग करें।"
    }
}

follow_up_answers["home loan"] = {
    **follow_up_answers.get("home loan", {}),
    "documents": {
        "en": "You usually need identity proof, address proof, income proof, bank statements, and property documents.",
        "kn": "ಸಾಮಾನ್ಯವಾಗಿ ಗುರುತಿನ ದಾಖಲೆ, ವಿಳಾಸದ ದಾಖಲೆ, ಆದಾಯದ ದಾಖಲೆ, ಬ್ಯಾಂಕ್ ಸ್ಟೇಟ್ಮೆಂಟ್‌ಗಳು ಮತ್ತು ಆಸ್ತಿ ದಾಖಲೆಗಳು ಬೇಕಾಗುತ್ತವೆ.",
        "hi": "आमतौर पर identity proof, address proof, income proof, bank statements और property documents चाहिए होते हैं।"
    },
    "eligibility": {
        "en": "Eligibility depends on income, age, repayment capacity, credit profile, and property details.",
        "kn": "ಅರ್ಹತೆ ಆದಾಯ, ವಯಸ್ಸು, ಮರುಪಾವತಿ ಸಾಮರ್ಥ್ಯ, ಕ್ರೆಡಿಟ್ ಪ್ರೊಫೈಲ್ ಮತ್ತು ಆಸ್ತಿ ವಿವರಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ.",
        "hi": "Eligibility income, age, repayment capacity, credit profile और property details पर निर्भर करती है।"
    },
    "interest": {
        "en": "Interest rates can change. Please check official SBI channels for the latest home loan rate.",
        "kn": "ಬಡ್ಡಿದರಗಳು ಬದಲಾಗಬಹುದು. ಇತ್ತೀಚಿನ ಗೃಹ ಸಾಲದ ದರಕ್ಕಾಗಿ ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "hi": "Interest rates बदल सकते हैं। Latest home loan rate के लिए official SBI channels देखें।"
    },
    "tenure": {
        "en": "Tenure depends on eligibility, age, repayment capacity, and SBI policy.",
        "kn": "ಅವಧಿ ಅರ್ಹತೆ, ವಯಸ್ಸು, ಮರುಪಾವತಿ ಸಾಮರ್ಥ್ಯ ಮತ್ತು SBI ನೀತಿಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ.",
        "hi": "Tenure eligibility, age, repayment capacity और SBI policy पर निर्भर करता है।"
    },
    "emi": {
        "en": "EMI depends on loan amount, rate, and tenure. Use SBI's official calculator for an estimate.",
        "kn": "EMI ಸಾಲ ಮೊತ್ತ, ದರ ಮತ್ತು ಅವಧಿಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ. ಅಂದಾಜಿಗೆ SBI ಅಧಿಕೃತ calculator ಬಳಸಿ.",
        "hi": "EMI loan amount, rate और tenure पर निर्भर करती है। Estimate के लिए SBI official calculator उपयोग करें।"
    },
    "processing_time": {
        "en": "Processing time depends on document verification, eligibility checks, and property review.",
        "kn": "ಪ್ರಕ್ರಿಯೆ ಸಮಯ ದಾಖಲೆ ಪರಿಶೀಲನೆ, ಅರ್ಹತೆ ಪರಿಶೀಲನೆ ಮತ್ತು ಆಸ್ತಿ ಪರಿಶೀಲನೆಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ.",
        "hi": "Processing time document verification, eligibility checks और property review पर निर्भर करता है।"
    }
}

follow_up_answers["credit card"] = {
    **follow_up_answers.get("credit card", {}),
    "reward_points": {
        "en": "Reward points depend on the card type and eligible transactions. Check official SBI Card details.",
        "kn": "Reward points ಕಾರ್ಡ್ ಪ್ರಕಾರ ಮತ್ತು ಅರ್ಹ ವ್ಯವಹಾರಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತವೆ. ಅಧಿಕೃತ SBI Card ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "hi": "Reward points card type और eligible transactions पर निर्भर करते हैं। Official SBI Card details देखें।"
    }
}

follow_up_answers["fixed deposit"] = {
    **follow_up_answers.get("fixed deposit", {}),
    "renewal": {
        "en": "FD renewal options depend on your deposit instructions. Check or update them through official SBI channels.",
        "kn": "FD renewal ಆಯ್ಕೆಗಳು ನಿಮ್ಮ ಠೇವಣಿ ಸೂಚನೆಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತವೆ. ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳ ಮೂಲಕ ಪರಿಶೀಲಿಸಿ ಅಥವಾ update ಮಾಡಿ.",
        "hi": "FD renewal options आपकी deposit instructions पर निर्भर करते हैं। Official SBI channels से check या update करें।"
    }
}

follow_up_answers["cheque book"] = {
    **follow_up_answers.get("cheque book", {}),
    "stop_payment": {
        "en": "Use official SBI channels to request stop payment for a cheque, subject to applicable rules and charges.",
        "kn": "ಅನ್ವಯಿಸುವ ನಿಯಮಗಳು ಮತ್ತು ಶುಲ್ಕಗಳಿಗೆ ಒಳಪಟ್ಟು cheque stop payment ಗಾಗಿ ಅಧಿಕೃತ SBI ಚಾನೆಲ್‌ಗಳನ್ನು ಬಳಸಿ.",
        "hi": "Applicable rules और charges के अनुसार cheque stop payment के लिए official SBI channels उपयोग करें।"
    }
}

follow_up_answers["net banking"] = {
    **follow_up_answers.get("net banking", {}),
    "transaction_rights": {
        "en": "Transaction rights can be enabled through official OnlineSBI options or your SBI branch after verification.",
        "kn": "ಪರಿಶೀಲನೆಯ ನಂತರ ಅಧಿಕೃತ OnlineSBI ಆಯ್ಕೆಗಳು ಅಥವಾ SBI ಶಾಖೆಯ ಮೂಲಕ transaction rights ಸಕ್ರಿಯಗೊಳಿಸಬಹುದು.",
        "hi": "Verification के बाद transaction rights official OnlineSBI options या SBI branch से enable किए जा सकते हैं।"
    }
}
