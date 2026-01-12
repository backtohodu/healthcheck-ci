from fastapi import APIRouter
import os

router = APIRouter()

VERSION = os.getenv("APP_VERSION", "1.0.0")

@router.get("/version")
def version():
    """
    배포 버전 확인
    """
    return {"version": VERSION}