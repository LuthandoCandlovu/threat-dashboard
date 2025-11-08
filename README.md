# 🛡️ Threat Intelligence Dashboard

A modern, real-time threat intelligence dashboard built with FastAPI, SQLAlchemy, and Python. Monitor and analyze security threats with an intuitive web interface.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 📸 Dashboard Preview

### Main Dashboard Interface
<img width="1816" height="858" alt="Threat Dashboard Main Interface" src="https://github.com/user-attachments/assets/ac39883c-2a42-4b45-bce2-29e09bd6b293" />

### Threat Analysis View
<img width="1876" height="927" alt="Threat Analysis Dashboard" src="https://github.com/user-attachments/assets/97c56add-868b-4c6d-841a-9027b7a96dd9" />

## ✨ Features

### 🎯 Core Capabilities
- **Real-time Threat Monitoring** - Live tracking of security threats with instant alerts
- **Interactive Dashboard** - Clean, modern web interface with real-time updates
- **RESTful API** - Full CRUD operations for threat data management
- **Automated Threat Detection** - Intelligent threat analysis and pattern recognition
- **Database Integration** - SQLite with SQLAlchemy ORM for robust data storage

### 📊 Analytics & Reporting
- **Threat Visualization** - Graphical representation of threat data
- **Risk Assessment** - Automated risk scoring and prioritization
- **Historical Analysis** - Trend analysis and threat pattern identification
- **Export Capabilities** - Generate reports in multiple formats

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/LuthandoCandlovu/threat-dashboard.git
   cd threat-dashboard
Create virtual environment

bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Initialize database

bash
python seed_data.py
Run the application

bash
uvicorn app.main:app --reload
Access the dashboard

🌐 Main Application: http://localhost:8000

📚 API Documentation: http://localhost:8000/docs

🔍 Alternative Docs: http://localhost:8000/redoc

🏗️ Architecture
<img width="927" height="547" alt="Image" src="https://github.com/user-attachments/assets/d8d60079-992f-4cca-b321-a6b1ff573c28" />

# Get all threats
response = requests.get("http://localhost:8000/threats")
threats = response.json()

# Create new threat
new_threat = {
    "name": "Malware Attack",
    "severity": "high",
    "type": "malware",
    "description": "Ransomware detected in network"
}
response = requests.post("http://localhost:8000/threats", json=new_threat)
🗃️ Data Models
Threat Model
python
class Threat(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    severity = Column(String)  # low, medium, high, critical
    type = Column(String)      # malware, phishing, ddos, etc.
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String)    # active, resolved, investigating
🧪 Testing
Run the complete test suite:

bash
# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=app tests/

# Run specific test file
pytest tests/test_routes.py -v
🐳 Docker Support
Deploy using Docker Compose:

bash
# Build and run with Docker
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f
🔧 Configuration
Environment variables supported:

bash
DATABASE_URL=sqlite:///./threat.db
DEBUG=True
HOST=0.0.0.0
PORT=8000
🤝 Contributing
We welcome contributions! Please see our contributing guidelines:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Development Setup
bash
# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov

# Run tests before committing
pytest

# Format code
black app/ tests/
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👥 Authors
Luthando Candlovu

GitHub: @LuthandoCandlovu

Project Repository: threat-dashboard

🙏 Acknowledgments
FastAPI team for the excellent web framework

SQLAlchemy for robust ORM capabilities

Uvicorn for high-performance ASGI server

Pandas for data analysis capabilities

Pytest for testing framework

📞 Support
If you have any questions or need help with setup:

Open an Issue

Check the API Documentation when running locally

<div align="center">
⭐ Don't forget to star this repo if you find it useful!
Built with ❤️ for the security community

</div> ```

