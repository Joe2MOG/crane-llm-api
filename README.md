# crane-llm-api

FastAPI skeleton for learning LLM integration with Clean Architecture.

## Structure

```
app/
  main.py              # FastAPI app entry point
  routes/
    analyze.py         # POST /analyze endpoint
  use_cases/
    analyze_fault.py   # Business logic + system prompt
  services/
    llm_service.py     # Anthropic SDK wrapper
  models/
    schemas.py         # Pydantic request/response models
```

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# edit .env and set ANTHROPIC_API_KEY
```

## Run

```bash
uvicorn app.main:app --reload
```

## Endpoints

- `GET /health` — liveness check
- `POST /analyze` — ask a crane fault question

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"question": "What does fault code E47 mean?"}'
```
