# Contract Intelligence & Compliance Platform

An AI-powered system for automated contract ingestion, clause extraction, risk scoring, compliance deviation detection, and semantic search.

---

## 🚀 Getting Started

This guide will walk you through setting up the project for local development.

### Prerequisites
- Python 3.9+
- Docker and Docker Compose

### 1. Clone the Repository
```bash
git clone https://github.com/your-org/contract-intel.git
cd contract-intel
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Backing Services
This command will start the PostgreSQL and Redis containers in the background.
```bash
docker-compose up -d
```

### 5. Run the Application Components
You will need to run each of the following components in a separate terminal.

**a. Start the API Server:**
```bash
cd services/api
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`.

**b. Start the Celery Worker:**
```bash
cd services/worker
celery -A celery_app worker --loglevel=info
```

**c. Run the Web UI:**
```bash
cd services/webui
streamlit run app.py
```
The application will be accessible at `http://localhost:8501`.

### 6. Verify the Setup
- Navigate to `http://localhost:8501` in your browser.
- Upload a PDF contract.
- You should see the risk analysis results displayed on the dashboard.

---
This README provides everything needed to start contributing to the Contract Intelligence Platform.
