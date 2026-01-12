from fastapi import APIRouter, Response, status
import psutil
import logging

router = APIRouter()

@router.get("/metrics")
def metrics(response: Response):
    """
    서비스 리소스 확인
    """
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    logging.info(f"Metrics: - CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")

    #임계치 설정
    if cpu > 90 or memory > 90 or disk > 90:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    else:
        response.status_code = status.HTTP_200_OK

    return {
        "cpu_percent": cpu,
        "memory_percent": memory,
        "disk_percent": disk
    }