from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.database import Base, engine
from app import models
from app.routes import router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Threat Detection API")

# Include routes
app.include_router(router)

# Root route
@app.get("/")
def root():
    return {"message": "Threat Detection API is running. Go to /docs for API documentation."}

# Optional: Redirect to Swagger UI
@app.get("/home")
def redirect_to_docs():
    return RedirectResponse(url="/docs")
