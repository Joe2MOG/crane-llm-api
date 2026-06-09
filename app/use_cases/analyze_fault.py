from app.models.schemas import AnalyzeResponse
from app.services.llm_service import LLMService

SYSTEM_PROMPT = (
    "You are an expert industrial crane technician. "
    "Answer questions about crane fault codes, maintenance procedures, and safety."
)


class AnalyzeFaultUseCase:
    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def execute(self, question: str) -> AnalyzeResponse:
        result = self.llm_service.ask(question, SYSTEM_PROMPT)
        return AnalyzeResponse(**result)
