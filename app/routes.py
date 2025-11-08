from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .threat_detection import detect_failed_logins
from . import models
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/detect-threats")
def detect_threats(db: Session = Depends(get_db)):
    result = detect_failed_logins(db)
    return {"suspicious_ips": result}

@router.post("/add-log")
def add_log(ip: str, event_type: str, user_agent: str, db: Session = Depends(get_db)):
    log = models.LogEntry(ip=ip, event_type=event_type, user_agent=user_agent, timestamp=datetime.utcnow())
    db.add(log)
    db.commit()
    db.refresh(log)
    return {"message": "Log added successfully", "log_id": log.id}
