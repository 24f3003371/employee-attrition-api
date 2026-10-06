from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Employee Attrition API is running"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": False
    }