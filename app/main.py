from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import equipment,experiment,authentication, students,institute,lab,slot

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
app.include_router(institute.router)
app.include_router(equipment.router)
app.include_router(experiment.router)
app.include_router(lab.router)
app.include_router(slot.router)
