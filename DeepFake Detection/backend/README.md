# DeepFake Detection Backend

This is the FastAPI backend for the DeepFake Detection web app.

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the Server

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000` by default.

## API Endpoint
- `POST /predict` — Accepts an image file and returns a placeholder prediction ("real" or "fake") with a confidence score. 