from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class LogEntry(Base):
    __tablename__ = "log_entries"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, index=True)
    event_type = Column(String)  # e.g., "login_failed", "port_scan"
    timestamp = Column(DateTime)
    user_agent = Column(String)
