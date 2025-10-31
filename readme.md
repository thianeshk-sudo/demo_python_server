# Demo Python Server

This repository contains a starter [FastAPI](https://fastapi.tiangolo.com/) application with a couple of basic endpoints.

## Getting Started

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Visit `http://127.0.0.1:8000` to see the welcome message.

A health-check endpoint is also available at `http://127.0.0.1:8000/health`.
