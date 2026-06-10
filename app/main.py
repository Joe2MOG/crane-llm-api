from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)

from fastapi import FastAPI
from app.routes.analyze import router as analyze_router

app = FastAPI(title="Crane LLM API")

app.include_router(analyze_router)


@app.get("/health")
def health():
    return {"status": "ok"}
