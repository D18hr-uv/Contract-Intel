from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os
from services.worker.tasks import process_document
from .celery_client import celery_app
from celery.result import AsyncResult

app = FastAPI()

# Define the directory to store uploaded files
UPLOAD_DIRECTORY = "../../data/raw"

class HealthResponse(BaseModel):
    status: str

@app.get("/health", response_model=HealthResponse)
def health_check():
    """
    Health check endpoint to verify that the API is running.
    """
    return {"status": "ok"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Endpoint to upload a contract file.
    The file will be stored in the data/raw directory and a Celery task
    will be triggered to process it.
    """
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)

    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Trigger the Celery task
    task = process_document.delay(file_path)

    return {"filename": file.filename, "task_id": task.id}

@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    """
    Endpoint to check the status of a Celery task.
    """
    task_result = AsyncResult(task_id, app=celery_app)
    result = {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result
    }
    return result
