import asyncio
import logging

import google.generativeai as genai
from duckduckgo_search import DDGS

from config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)


class MarketAnalyzerService:
    def __init__(self):
        self.ddgs = DDGS()
        self.model = None

        if settings.GEMINI_API_KEY:
            self.model = genai.GenerativeModel("gemini-pro")

    async def get_sector_news(self, sector: str) -> str:
        query = (
            f"latest market trends trade opportunities "
            f"{sector} sector India investment news"
        )

        try:
            loop = asyncio.get_running_loop()
            results = await loop.run_in_executor(
                None,
                lambda: list(
                    self.ddgs.text(
                        query, region="in-en", timelimit="w", max_results=5
                    )
                ),
            )

            if not results:
                return "No relevant market news found."

            context = ""
            for res in results:
                context += (
                    f"- **{res['title']}**\n"
                    f"  {res['body']}\n"
                    f"  Source: {res['href']}\n\n"
                )

            return context

        except Exception as e:
            logger.error(f"Search error: {e}")
            return "Market data could not be retrieved at this time."

    async def analyze_opportunity(self, sector: str, market_data: str) -> str:
        if not self.model:
            return (
                f"# {sector.title()} Sector Analysis\n\n"
                "⚠️ **AI service unavailable.**\n\n"
                "## Collected Market Data\n"
                f"{market_data}"
            )

        prompt = f"""
You are a financial analyst specializing in Indian markets.

Analyze the following information for the "{sector}" sector and produce
a professional investment analysis.

### Input Data
{market_data}

### Instructions
- Output strictly in Markdown
- Use the following sections:
  - Executive Summary
  - Key Trends
  - Trade Opportunities
  - Risks
  - Outlook
- Be factual and avoid hallucinated statistics
"""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Gemini error: {e}")
            return (
                "## Analysis Error\n"
                "AI analysis could not be completed at this time."
            )
