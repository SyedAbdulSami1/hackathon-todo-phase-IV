from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.post("/api/auth/login")
def login():
    return {"message": "Dummy login success"}
