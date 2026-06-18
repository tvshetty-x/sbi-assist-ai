from fastapi import FastAPI

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
