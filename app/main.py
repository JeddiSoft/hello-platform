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
        "message": "Hello from GitOps"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }