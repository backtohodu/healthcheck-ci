# from fastapi import FastAPI, Response, status
# import psutil
# import logging
# import os
#
# app = FastAPI(title="HealthCheck")
#
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# VERSION = os.getenv("APP_VERSION", "1.0.0")
#
# @app.get("/health")
# def health_check(response: Response):
#     """
#     서비스 정상 여부 판단
#     """
#     try:
#         response.status_code = status.HTTP_200_OK
#         logging.info("Health Check OK")
#         return {"status": "UP"}
#     except Exception as e:
#         logging.error(f"Health Check Failed: {e}")
#         response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
#         return {"status": "DOWN"}
#
# @app.get("/metrics")
# def metrics(response: Response):
#     """
#     서비스 리소스 확인
#     """
#     cpu = psutil.cpu_percent(interval=1)
#     memory = psutil.virtual_memory().percent
#     disk = psutil.disk_usage('/').percent
#
#     logging.info(f"Metrics: - CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")
#
#     #임계치 설정
#     if cpu > 90 or memory > 90 or disk > 90:
#         response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
#     else:
#         response.status_code = status.HTTP_200_OK
#
#     return {
#         "cpu_percent": cpu,
#         "memory_percent": memory,
#         "disk_percent": disk
#     }
#
# @app.get("/version")
# def version():
#     """
#     배포 버전 확인
#     :return:
#     """
#     return {"version": VERSION}

from fastapi import FastAPI
from app.health import router as health_router
from app.metrics import router as metrics_router
from app.version import router as version_router

app = FastAPI(title="HealthCheck")

app.include_router(health_router)
app.include_router(metrics_router)
app.include_router(version_router)