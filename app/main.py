from fastapi import FastAPI

app = FastAPI(title="Demo Python Server")


@app.get("/")
async def read_root():
    """Return a simple welcome message."""
    return {"message": "Welcome to the Demo Python Server!"}


@app.get("/health")
async def health_check():
    """Basic health-check endpoint."""
    return {"status": "ok"}
