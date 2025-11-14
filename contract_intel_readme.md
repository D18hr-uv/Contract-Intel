# Contract Intelligence & Compliance Platform

An AI-powered system for automated contract ingestion, clause extraction, risk scoring, compliance deviation detection, and semantic search. This README provides onboarding instructions for new developers and a complete overview of the architecture, workflows, and setup process.

---

## 🚀 Project Overview
The Contract Intelligence & Compliance Platform enables legal, procurement, and compliance teams to:
- Upload large volumes of contracts (PDF, DOCX, scanned images)
- Automatically extract clauses and normalize key fields
- Detect legal & compliance risks
- Identify non-standard language
- Track renewal dates
- Search all contracts using semantic search

The platform is built primarily in **Python**, using **FastAPI**, **OCR**, **Hugging Face NLP models**, **FAISS**, and **PostgreSQL**.

---

## 🗂 Repository Structure
```
contract-intel/
├─ infra/                  
├─ services/
│  ├─ api/                # FastAPI application
│  ├─ ingestion/          # OCR + document ingestion
│  ├─ nlp/                # clause extraction, classification, risk
│  ├─ vector_search/      # FAISS / embeddings
│  ├─ worker/             # Celery/RQ background jobs
│  └─ webui/              # Streamlit / React interface
├─ data/
│  ├─ raw/
│  ├─ labeled/
│  └─ templates/
├─ notebooks/             # Model experiments
├─ tests/
├─ docker-compose.yml
└─ requirements.txt
```

---

## 🛠 Tech Stack
### **Backend / API**
- FastAPI
- Pydantic
- Uvicorn

### **OCR & Document Parsing**
- PyMuPDF (fitz)
- Tesseract OCR
- pdfplumber

### **NLP / ML**
- HuggingFace Transformers
- spaCy
- sentence-transformers
- scikit-learn / XGBoost

### **Vector Search**
- FAISS (local)
- Optional: Weaviate / Milvus for production

### **Storage**
- PostgreSQL
- S3-compatible bucket (local/minio or AWS S3)

### **Async Processing**
- Celery + Redis (or RQ)

### **Frontend**
- React / NextJS or Streamlit

---

## ⚙️ Setup Instructions
### 1. Clone the Repository
```
git clone https://github.com/your-org/contract-intel.git
cd contract-intel
```

### 2. Create Virtual Environment
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Start Services
```
docker-compose up -d
```
This runs:
- PostgreSQL
- Redis
- FAISS (if containerized)

### 4. Start API Server
```
cd services/api
uvicorn main:app --reload
```
Verify:
```
GET http://localhost:8000/health
```
Should return:
```
{"status": "ok"}
```

---

## 📄 Document Ingestion Workflow
1. User uploads file using `/upload` API.
2. File stored in `data/raw/` or S3.
3. Celery worker picks ingestion job.
4. If PDF contains text → extract via PyMuPDF.
5. If scanned → run page-level OCR via Tesseract.
6. Text normalized & saved.
7. Segmented into clauses.
8. NLP models classify clauses & extract key fields.
9. Risk engine scores document.
10. Data stored in DB for UI display.

---

## 🤖 Clause Extraction & NLP
### Tasks performed:
- Clause segmentation by headings
- Clause classification (e.g., Termination, Liability, Confidentiality)
- Date extraction & normalization
- Monetary field extraction
- Named entity extraction (parties, vendor names)

Models stored in `services/nlp/`.

---

## ⚠ Risk Scoring Engine
Risk is computed based on:
- Clause presence/absence
- Similarity vs standard templates
- Severity of deviations
- Monetary exposure
- Renewal terms

Output example:
```
{
  "risk_score": 74,
  "risk_level": "High",
  "reasons": [
    "Missing indemnity clause",
    "Unlimited vendor liability",
    "Auto-renewal without notice period"
  ]
}
```

---

## 🔍 Semantic Search
Uses SentenceTransformers + FAISS:
- Embeds clauses
- Stores vectors
- Supports semantic queries like:
  - "contracts with GDPR issues"
  - "unlimited liability clauses"

API endpoint:
```
GET /search?q=your_query
```

---

## 🧪 Testing
Run unit tests:
```
pytest
```
Tests include:
- OCR extraction tests
- Clause segmentation tests
- Classification correctness tests
- API integration tests

---

## 🚀 Deployment Guide
### Local
- Run all services via docker-compose
- API via uvicorn

### Production (recommended)
- Docker images deployed to Kubernetes
- Use AWS Textract for enterprise OCR
- Host FAISS behind vector search microservice
- Use AWS RDS for PostgreSQL

---

## 📅 Roadmap
### **Phase 1 — MVP**
- OCR pipeline
- Clause extractor
- Risk scoring (rule-based + simple ML)
- Basic dashboard

### **Phase 2 — Intelligence Layer**
- Compliance deviation detection
- Semantic search
- Renewal alerts

### **Phase 3 — Enterprise Layer**
- RBAC, audit trails
- SOC2 compliance
- CLM integrations (SAP Ariba, Docusign)

### **Phase 4 — Full Automation**
- Auto-redlining
- AI-assisted contract drafting
- Predictive vendor scoring

---

## 👥 Contribution Guide
- Use feature branches
- Open PRs with description + test coverage
- Run black + ruff for formatting

---

## 📞 Contact
For help or onboarding questions, contact the tech lead.

---

This README provides everything needed to start contributing to the Contract Intelligence Platform.