from celery import Celery

# Create a Celery instance for the API to communicate with the broker
celery_app = Celery(
    "api_client",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
