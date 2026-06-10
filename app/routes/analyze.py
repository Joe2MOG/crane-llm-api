from fastapi import APIRouter, HTTPException
from app.models.schemas import AnalyzeRequest, AnalyzeResponse
from app.services.llm_service import LLMService
from app.use_cases.analyze_fault import AnalyzeFaultUseCase
import logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    use_case = AnalyzeFaultUseCase(llm_service=LLMService())
    try:
        return use_case.execute(request.question)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.error("LLM request failed: %s", str(e))
        raise HTTPException(status_code=500, detail="LLM request failed")
