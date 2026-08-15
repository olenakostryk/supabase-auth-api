from fastapi import FastAPI

from app.routes.auth import router as auth_router
from app.routes.protected import router as protected_router
from app.routes.public import router as public_router


app = FastAPI(
    title="Supabase Auth API",
    description="Secure API using FastAPI and Supabase Auth",
    version="1.0.0",
)


app.include_router(auth_router)
app.include_router(public_router)
app.include_router(protected_router)


@app.get("/")
def root():
    return {"message": "Server is running"}


@app.get("/health")
def health():
    return {"status": "ok"}