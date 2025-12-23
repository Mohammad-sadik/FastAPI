# Trade Opportunities API – Appscrip Assignment

---

## Project Overview
- FastAPI service to analyze market data
- Provides trade opportunity insights for Indian sectors
- Generates structured Markdown market analysis reports
- Designed as per Appscrip developer task requirements

---

## Core Requirement
- Single API endpoint
- Accepts a sector name as input
- Example sectors:
  - pharmaceuticals
  - technology
  - agriculture
- Returns structured Markdown analysis report
- Focused on current trade opportunities in India

---

## API Specification
- Endpoint: GET /analyze/{sector}
- Example request:
  - /analyze/pharmaceuticals
- Response format:
  - Structured Markdown report
  - Can be saved as a `.md` file

---

## Core Workflow
- Accept sector name as input
- Search for current market data and news
- Analyze collected information using AI
- Generate structured Markdown report
- Apply authentication, validation, and rate limiting

---

## Report Structure
- Executive Summary
- Key Trends
- Trade Opportunities
- Risks
- Outlook

---

## Technical Requirements Implemented
- FastAPI backend
- Proper async handling
- Input validation
- Session management using JWT
- Rate limiting per user/IP
- Secure authentication
- Graceful error handling

---

## AI & Data Sources
- Google Gemini API for market analysis
- DuckDuckGo Search for real-time market news
- No paid APIs required
- Graceful fallback if AI service is unavailable

---

## Security
- JWT-based authentication
- OAuth2 password flow
- Protected core endpoint
- Rate limiting to prevent abuse
- Input validation for sector names

---

## Storage
- In-memory storage only
- No database used
- Users and sessions stored in memory
- Complies with assignment constraints

---

## System Architecture
- Clean separation of concerns
- API layer for routing
- Service layer for data collection and AI analysis
- Authentication layer for security and rate limiting
- Configuration isolated from business logic

---

## Project Structure
- trade_api/
  - main.py – application entry point and routing
  - auth.py – authentication, session handling, rate limiting
  - services.py – market data collection and AI analysis
  - models.py – request and response models
  - config.py – environment and settings
  - requirements.txt
  - README.md

---

## Setup Instructions
- Create virtual environment:
  - py -m venv venv
  - venv\Scripts\activate
- Install dependencies:
  - pip install -r requirements.txt
- Configure environment variable (optional):
  - set GEMINI_API_KEY=your_api_key
- Run application:
  - uvicorn main:app --reload

---

## API Documentation
- Swagger UI available at:
  - http://127.0.0.1:8000/docs
- Interactive testing supported

---

## Health Check
- Endpoint: GET /health
- Used to verify service availability

---

## Error Handling
- Graceful handling of external API failures
- Clear error messages for invalid input
- Safe fallback when AI analysis is unavailable

---

## Success Criteria Coverage
- API accepts sector names and returns Markdown reports
- Reports contain relevant market information
- Security measures prevent abuse
- System handles failures gracefully
- Code is clean, modular, and well-organized

---

## Time Constraint
- Designed and implemented within 0–1 day as specified

---

## Author
- Mohammad Sadik
