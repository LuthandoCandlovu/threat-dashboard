from app.database import SessionLocal, engine
from app.models import LogEntry
from datetime import datetime

# Create sample logs
sample_logs = [
    {'ip': '192.168.1.10', 'event_type': 'login_failed', 'user_agent': 'Mozilla/5.0'},
    {'ip': '192.168.1.10', 'event_type': 'login_failed', 'user_agent': 'Mozilla/5.0'},
    {'ip': '192.168.1.10', 'event_type': 'login_failed', 'user_agent': 'Mozilla/5.0'},
    {'ip': '192.168.1.10', 'event_type': 'login_failed', 'user_agent': 'Mozilla/5.0'},
    {'ip': '192.168.1.10', 'event_type': 'login_failed', 'user_agent': 'Mozilla/5.0'},
    {'ip': '192.168.1.11', 'event_type': 'port_scan', 'user_agent': 'Nmap'},
]

db = SessionLocal()
for log in sample_logs:
    entry = LogEntry(ip=log['ip'], event_type=log['event_type'], user_agent=log['user_agent'], timestamp=datetime.utcnow())
    db.add(entry)
db.commit()
print("Sample data inserted.")
