from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from auth import router as auth_router
from courses import router as course_router   # If you have courses.py

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Authentication API"
)

# CORS Configuration
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth_router)
app.include_router(course_router)   # Remove this line if courses.py doesn't exist yet

@app.get("/")
def home():
    return {"message": "Authentication API is running successfully!"}