import pandas as pd
from sqlalchemy.orm import Session
from . import models

def detect_failed_logins(db: Session, threshold=5):
    logs = db.query(models.LogEntry).filter(models.LogEntry.event_type == "login_failed").all()
    
    if not logs:
        return []

    df = pd.DataFrame([{
        'ip': log.ip,
        'timestamp': log.timestamp,
        'user_agent': log.user_agent
    } for log in logs])
    
    suspicious_ips = df['ip'].value_counts()[df['ip'].value_counts() > threshold].index.tolist()
    return suspicious_ips
