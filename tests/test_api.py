import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_detect_threats():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/detect-threats")
    assert response.status_code == 200
    assert "suspicious_ips" in response.json()
