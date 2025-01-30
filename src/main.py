from fastapi import FastAPI, Depends

from src.config import get_settings, Settings

app = FastAPI()


@app.get("/health")
def pong():
    return {
        "message": "API is online!",
    }


@app.get("/status")
def status(settings: Settings = Depends(get_settings)):
    return {
        "environment": settings.environment,
        "testing": settings.testing,
    }
