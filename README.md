```markdown
# Trade Opportunities API 📈

A high-performance FastAPI service that analyzes Indian market sectors to provide trade opportunity insights. It combines real-time web search (DuckDuckGo) with Generative AI (Google Gemini) to produce structured investment reports in Markdown format.

> **Quick Start:** `pip install -r requirements.txt && uvicorn main:app --reload`

## 🚀 Features

* **Sector Analysis:** Generates comprehensive reports on any given sector (e.g., "Pharmaceuticals", "Green Energy").
* **AI-Powered:** Uses **Google Gemini Pro** to synthesize market news into actionable insights.
* **Real-time Data:** Fetches the latest market news using **DuckDuckGo Search** (no expensive SERP APIs required).
* **Secure:** Implements **JWT Authentication** for endpoint protection.
* **Robust:** Includes **Rate Limiting** (5 requests/minute) to prevent abuse.
* **Architecture:** Clean, modular code structure separating Logic, Auth, and Routing.

---

## 🛠️ Tech Stack

* **Core Framework:** FastAPI (Async/Await)
* **Server:** Uvicorn (ASGI)
* **AI Engine:** Google Gemini Pro (via `google-generativeai`)
* **Data Source:** DuckDuckGo Search (Real-time market news)
* **Security:** OAuth2 (JWT Tokens), BCrypt (Password Hashing)
* **Performance:** SlowAPI (Rate Limiting), In-memory Caching

---

## 📂 Project Structure

```text
.
├── main.py            # Application entry point & wiring
├── config.py          # Configuration & Environment variables
├── models.py          # Pydantic models for request/response
├── auth.py            # JWT Authentication & Session handling
├── services.py        # Business logic (Search & AI analysis)
├── requirements.txt   # Project dependencies
├── .env               # API Keys & Secrets (not committed)
└── README.md          # Documentation

```

---

## ⚡ Setup & Installation

### 1. Prerequisites

* **Python 3.9+** installed on your system.
* A **Google Gemini API Key**. (Get it free [here](https://makersuite.google.com/app/apikey)).

### 2. Install Dependencies

It is recommended to use a virtual environment.

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

# Install libraries
pip install -r requirements.txt

```

### 3. Environment Configuration

You must set your API key for the application to work. You can do this via terminal command or a `.env` file.

**Option A: Command Line (Temporary)**

* **Windows:** `$env:GEMINI_API_KEY="your_api_key_here"`
* **Mac/Linux:** `export GEMINI_API_KEY="your_api_key_here"`

**Option B: .env file (Permanent)**
Create a file named `.env` in the root folder and add:

```env
GEMINI_API_KEY=your_actual_api_key_here
SECRET_KEY=your_super_secret_key_change_this

```

### 4. Run the Application

Start the development server using Uvicorn:

```bash
uvicorn main:app --reload

```

The API will be live at `http://127.0.0.1:8000`.

---

## 📖 Usage Guide

The easiest way to test the API is using the built-in Swagger UI.

### Step 1: Access the Dashboard

Open your web browser and navigate to:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

### Step 2: Authentication

The API is secured. You must log in to get an access token.

1. Click the **Authorize** button (top right).
2. Use these default credentials (for testing):
* **Username:** `admin`
* **Password:** `secret`


3. Click **Authorize** then **Close**.

### Step 3: Generate a Report

1. Scroll down to the **`GET /analyze/{sector}`** endpoint.
2. Click **Try it out**.
3. Enter a sector name (e.g., `Renewable Energy` or `Textiles`).
4. Click **Execute**.

**Response Example:**

```json
{
  "sector": "Renewable Energy",
  "timestamp": "2023-12-25 10:30:00",
  "report_markdown": "# Renewable Energy Analysis\n## Executive Summary\nThe sector is seeing a 15% growth..."
}

```

---

## 🛡️ Security & Limitations

* **Rate Limiting:** To prevent abuse, users are limited to **5 requests per minute**. Exceeding this returns a `429 Too Many Requests` error.
* **Data Sources:** Relies on DuckDuckGo. Occasional timeouts may occur if the search engine is unreachable.

```

```
