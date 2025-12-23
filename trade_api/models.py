from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class ReportResponse(BaseModel):
    sector: str
    timestamp: str
    report_markdown: str
