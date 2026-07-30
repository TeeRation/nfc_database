from fastapi import FastAPI


app = FastAPI(
    title="NFC Database API",
    description=(
        "API для работы с NFC-метками, сотрудниками, "
        "устройствами и задачами"
    ),
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "NFC Database API работает!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}