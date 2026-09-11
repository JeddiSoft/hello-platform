from fastapi import FastAPI

app = FastAPI(
    title="Hello Platform",
    version="1.0.0"
)


@app.get("/")
def hello():
    return {
        "application": "hello-platform",
        "version": "1.0.0",
        "message": "pusehalo de nuevo con lali"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }