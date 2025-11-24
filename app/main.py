from fastapi import FastAPI
from router.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

load_dotenv()

Frontend_URL = os.getenv("FRONTEND_URL")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[Frontend_URL, "http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}
