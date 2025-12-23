```
# Trade Opportunities API 📈

A high-performance FastAPI service that analyzes Indian market sectors to provide trade opportunity insights. It combines real-time web search (DuckDuckGo) with Generative AI (Google Gemini) to produce structured investment reports in Markdown format.

## 🚀 Features

* **Sector Analysis:** Generates comprehensive reports on any given sector (e.g., "Pharmaceuticals", "Green Energy").
* **AI-Powered:** Uses **Google Gemini Pro** to synthesize market news into actionable insights.
* **Real-time Data:** Fetches the latest market news using **DuckDuckGo Search** (no expensive SERP APIs required).
* **Secure:** Implements **JWT Authentication** for endpoint protection.
* **Robust:** Includes **Rate Limiting** (5 requests/minute) to prevent abuse.
* **Architecture:** Clean, modular code structure separating Logic, Auth, and Routing.

---

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Server:** Uvicorn
* **AI Model:** Google Gemini (via `google-generativeai`)
* **Search Engine:** DuckDuckGo (`duckduckgo-search`)
* **Security:** OAuth2 with Password (Bearer), Passlib (Bcrypt), Python-Jose (JWT)
* **Rate Limiting:** SlowAPI

---

## 📂 Project Structure


```

```
```text
trade_api/
├── main.py            # Application entry point & routing
├── config.py          # Configuration management
├── models.py          # Pydantic data models
├── auth.py            # JWT Authentication & Rate limiting logic
├── services.py        # Business logic (Search & AI integration)
├── requirements.txt   # Project dependencies
└── README.md          # Documentation

```

## ⚡ Setup & Installation

### 1. Prerequisites

* Python 3.9+
* A Google Gemini API Key (Get it free [here](https://makersuite.google.com/app/apikey))

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Environment Configuration

You can set your API key as an environment variable or create a `.env` file in the root directory:

**Option A: Command Line (Linux/Mac)**

```bash
export GEMINI_API_KEY="your_actual_api_key_here"

```

**Option B: .env file**
Create a file named `.env` and add:

```env
GEMINI_API_KEY=your_actual_api_key_here
SECRET_KEY=your_super_secret_key_change_this

```

### 4. Run the Application

```bash
uvicorn main:app --reload

```

The server will start at `http://127.0.0.1:8000`.

---

## 📖 Usage Guide

The easiest way to test the API is using the interactive Swagger UI at `http://127.0.0.1:8000/docs`.

### Step 1: Authentication

This API is secured. You must obtain a token to use the analysis endpoint.

* **Endpoint:** `POST /token`
* **Default Credentials (for testing):**
* **Username:** `admin`
* **Password:** `secret`



*Response:*

```json
{
  "access_token": "eyJhbGciOi...",
  "token_type": "bearer"
}

```

### Step 2: Analyze a Sector

Use the token from Step 1 to make an authenticated request.

* **Endpoint:** `GET /analyze/{sector}`
* **Header:** `Authorization: Bearer <your_access_token>`
* **Example:** `GET /analyze/pharmaceuticals`

*Response:*

```json
{
  "sector": "pharmaceuticals",
  "timestamp": "2023-12-25 10:30:00",
  "report_markdown": "# Pharmaceutical Sector Analysis\\n## Executive Summary\\n..."
}

```

---

## 🛡️ Security & Limitations

* **Rate Limiting:** Users are limited to **5 requests per minute**. Exceeding this will return `429 Too Many Requests`.
* **Session Storage:** Currently uses in-memory storage for users and sessions (per project requirements). Restarting the server resets sessions.
* **Search Reliability:** Relies on DuckDuckGo. If their API changes or limits requests, data collection may fail temporarily.

---
