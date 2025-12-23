import time
from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

from auth import (
    limiter,
    verify_password,
    create_access_token,
    get_current_user,
    FAKE_USERS_DB,
)
from config import settings
from models import Token, ReportResponse
from services import MarketAnalyzerService

app = FastAPI(
    title="Trade Opportunities API",
    description="AI-powered market analysis for Indian sectors",
    version="1.0.0",
)

# Rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

analyzer = MarketAnalyzerService()


@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = FAKE_USERS_DB.get(form_data.username)

    if not user or not verify_password(
        form_data.password, user["password_hash"]
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        {"sub": user["username"]},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return {"access_token": token, "token_type": "bearer"}


@app.get("/analyze/{sector}", response_model=ReportResponse)
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,
    sector: str,
    current_user: dict = Depends(get_current_user),
):
    if not sector.isalpha() or len(sector) < 3:
        raise HTTPException(
            status_code=400,
            detail="Sector must be alphabetic and at least 3 characters long.",
        )

    market_data = await analyzer.get_sector_news(sector)
    report = await analyzer.analyze_opportunity(sector, market_data)

    return {
        "sector": sector.lower(),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "report_markdown": report,
    }


@app.get("/health")
def health():
    return {"status": "active"}
