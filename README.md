# Trade Opportunities API

An AI-powered FastAPI service that analyzes Indian market sectors and returns
structured trade opportunity reports in Markdown format.

---

## 📌 Overview

This application provides a secure and rate-limited API that:
- Accepts a sector name (e.g., pharmaceuticals, technology, agriculture)
- Collects real-time market data using web search
- Uses Google Gemini to generate AI-driven market analysis
- Returns a structured Markdown report suitable for saving as a `.md` file

The project follows clean architecture principles with a clear separation of
routing, authentication, business logic, and configuration.

---

## 🛠️ Tech Stack

- FastAPI – Backend framework
- Google Gemini API – AI-based market analysis
- DuckDuckGo Search – Real-time market news
- JWT (OAuth2) – Authentication & session management
- SlowAPI – Rate limiting
- Passlib – Secure password hashing
- Pydantic – Data validation
- In-memory storage – No database used

---

## 📂 Project Structure



trade_api/
├── main.py        # Application entry point & routes
├── auth.py        # Authentication & rate limiting
├── services.py    # Data collection & AI analysis
├── models.py      # Request/response schemas
├── config.py      # Environment & settings
├── requirements.txt
└── README.md



## 🚀 API Endpoint

### Analyze Sector

GET /analyze/{sector}


### Example Request


GET /analyze/pharmaceuticals
Authorization: Bearer <access_token>



### Response
Returns a structured Markdown report with:
- Executive Summary
- Key Trends
- Trade Opportunities
- Risks
- Outlook


## 🔐 Authentication

The API uses OAuth2 with JWT Bearer tokens.

### Test Credentials


Username: admin
Password: secret



### Get Access Token


POST /token



Use the returned token in the `Authorization` header.



## ⏱️ Rate Limiting

- 5 requests per minute per user/IP
- Implemented using SlowAPI
- Prevents API abuse

---

## ⚠️ Error Handling

- Graceful handling of external API failures
- Clear validation errors for invalid input
- Fallback behavior if AI service is unavailable

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment


py -m venv venv
venv\Scripts\activate

```

### 2. Install Dependencies
```

pip install -r requirements.txt

```

### 3. Configure Environment Variable
```

set GEMINI_API_KEY=your_gemini_api_key

```

*(Optional: Without this key, the API still returns raw market data.)*

### 4. Run the Server
```

uvicorn main:app --reload

```

---

## 📖 API Documentation

Open Swagger UI at:
```

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

```

---

## ✅ Health Check

```

GET /health

````

Response:
```json
{
  "status": "active"
}
````

---

## 📝 Notes

* All data is stored in-memory as per assignment requirements
* No database is used
* Designed for clarity, security, and production readiness

---

## 👤 Author

Mohammad Sadik

```

---

If you want, I can also:
- Make a **shorter GitHub-style README**
- Customize it exactly to the **Appscrip assignment wording**
- Add **screenshots + demo steps**
- Help you explain this README in an interview

Just tell me 👌
```
