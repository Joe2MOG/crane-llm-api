from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    question: str


class AnalyzeResponse(BaseModel):
    answer: str
    input_tokens: int
    output_tokens: int
