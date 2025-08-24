from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}
