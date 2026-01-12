from fastapi import APIRouter, Response, status
import logging

router = APIRouter()

@router.get("/health")
def health_check(response: Response):
    """
    서비스 정상 여부 판단
    """

    try:
        response.status_code = status.HTTP_200_OK
        logging.info("이상 없음")
        return {"status": "UP"}

    except Exception as e:
        logging.error(f"Health check failed: {e}")
        response.status_code = status.HTTP_500_SERVICE_UNAVAILABLE
        return {"status": "DOWN"}