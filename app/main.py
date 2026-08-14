from fastapi import FastAPI

from app.admin import setup_admin
from app.routers.locations import router as locations_router
from app.routers.tasks import router as tasks_router

app = FastAPI(
    title="NFC Database API",
    description=(
        "API для работы с NFC-метками, сотрудниками, "
        "устройствами и задачами"
    ),
    version="1.0.0",
)

setup_admin(app)
app.include_router(locations_router)
app.include_router(tasks_router)


@app.get("/")
def root():
    return {"message": "NFC Database API работает!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}