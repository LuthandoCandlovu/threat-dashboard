from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routes import router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Threat Detection API")

# Include routes
app.include_router(router)
