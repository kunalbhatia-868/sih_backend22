from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import authentication, students

from app.config.database import Base, engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)

app.include_router(students.router)
app.include_router(authentication.router)
