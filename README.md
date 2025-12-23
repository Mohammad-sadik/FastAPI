```md
# Trade Opportunities API

FastAPI-based service that analyzes Indian market sectors and returns
AI-generated trade opportunity reports in Markdown format.

---

## Overview

- Accepts a sector name
- Fetches real-time market news
- Uses Google Gemini for analysis
- Returns structured Markdown output
- Uses JWT authentication and rate limiting
- In-memory storage only (no database)

---

## Tech Stack

- FastAPI
- Google Gemini API
- DuckDuckGo Search
- JWT (OAuth2)
- SlowAPI (Rate Limiting)
- Passlib (Password hashing)
- Pydantic

---

## Project Structure

```

trade_api/
├── main.py
├── auth.py
├── services.py
├── models.py
├── config.py
├── requirements.txt
└── README.md

```

---

## API Endpoint

```

GET /analyze/{sector}

```

Example:
```

GET /analyze/pharmaceuticals

```

Returns a Markdown report with:
- Executive Summary
- Key Trends
- Trade Opportunities
- Risks
- Outlook

---

## Authentication

```

POST /token

```

Test Credentials:
```

username: admin
password: secret

```

---

## Rate Limiting

- 5 requests per minute per user/IP

---

## Setup & Run

```

py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
set GEMINI_API_KEY=your_api_key
uvicorn main:app --reload

```

---

## Swagger UI

```

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

```

---

## Health Check

```

GET /health

```

Response:
```

{"status":"active"}

```

---

## Author

Mohammad Sadik
```

---

## ✅ 2️⃣ RUN COMMANDS (COPY–PASTE)

```bat
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
set GEMINI_API_KEY=your_gemini_api_key
uvicorn main:app --reload
```

---

## ✅ 3️⃣ TEST USING CURL (COPY–PASTE)

### Get Token

```bat
curl -X POST http://127.0.0.1:8000/token ^
 -H "Content-Type: application/x-www-form-urlencoded" ^
 -d "username=admin&password=secret"
```

### Analyze Sector

```bat
curl -X GET http://127.0.0.1:8000/analyze/pharmaceuticals ^
 -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

---

