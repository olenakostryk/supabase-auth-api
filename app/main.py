from fastapi import FastAPI

app = FastAPI(
    title="Supabase Auth API",
    description="Secure API using FastAPI and Supabase Auth",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "Server is running"}

@app.get("/health")
def health():
    return {"status": "ok"}