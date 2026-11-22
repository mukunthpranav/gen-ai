from fastapi import FastAPI

app = FastAPI(title="GenAI Platform — RAG + Agent API")


@app.get("/health")
def health():
    return {"status": "ok"}
