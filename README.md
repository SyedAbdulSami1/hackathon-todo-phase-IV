# AI-Powered Todo Chatbot (Hackathon Phase IV)

A premium, startup-quality Todo application featuring an AI Chatbot powered by Google Gemini and MCP (Model Context Protocol) for task management. **Now containerized and deployed on Kubernetes!**

## 🏆 Hackathon Progress
- ✅ **Phase I:** In-Memory Python Console App
- ✅ **Phase II:** Full-Stack Web Application
- ✅ **Phase III:** AI-Powered Todo Chatbot
- ✅ **Phase IV:** Local Kubernetes Deployment **(COMPLETED)**
- 🔜 **Phase V:** Advanced Cloud Deployment (Next project)

## 🚀 Recent Updates & Fixes
- **✅ Phase IV Deployment:** Containerized frontend & backend with Docker multi-stage builds
- **✅ Kubernetes Ready:** Helm charts for Minikube deployment with 2 replicas (backend & frontend)
- **✅ Fixed 500 Errors:** Resolved a critical bug where a folder named `logging` shadowed the standard library. Renamed to `internal_logging`.
- **✅ Backend Entrypoint:** Unified entrypoint to `index.py` with path-adjustment logic for Vercel/Local compatibility.
- **✅ Neon DB Optimization:** Added SSL support (`sslmode=require`) for secure database connections.
- **✅ Premium UI/UX:** Enhanced the Chatbot with high-end animations, glassmorphism, and interactive "AI is thinking" states.
- **✅ Verified Tests:** 64/66 backend tests passing (97% success rate).

## 🛠️ Local Setup

### Option 1: Traditional Setup

#### Backend (FastAPI)
```bash
cd backend
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file with your keys
# GOOGLE_API_KEY=your_key
# DATABASE_URL=your_postgres_url

# Run the server
uvicorn index:app --reload --port 8000
```

#### Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
```
Access the app at `http://localhost:3000`.

### Option 2: Kubernetes Deployment (Phase IV)

#### Prerequisites
- Docker Desktop
- Minikube
- Helm v3
- kubectl

#### Deploy to Minikube
```bash
# Start Minikube
minikube start --driver=docker

# Build Docker images
docker build -t todo-backend:latest -f backend/Dockerfile backend/
docker build -t todo-frontend:latest -f frontend/Dockerfile frontend/

# Load images into Minikube
minikube image load todo-backend:latest
minikube image load todo-frontend:latest

# Deploy with Helm
helm install todo-app helm/todo-app --namespace todo-app --create-namespace

# Check deployment status
kubectl get pods -n todo-app
kubectl get services -n todo-app

# Access the app (port-forward)
kubectl port-forward service/todo-app-frontend 3000:3000 -n todo-app
```

Access the app at `http://localhost:3000`.

#### Uninstall
```bash
helm uninstall todo-app -n todo-app
minikube stop
```

## 🧪 Testing Report

### Phase IV Pytest Results
**Status:** 🟢 PASSING (64/66 Tests - 97%)
**Date:** March 12, 2026

| Test Suite | Result | Count |
|------------|--------|-------|
| Integration (Endpoints) | ⚠️ 7/9 PASS | 9 |
| Main App Lifecycle | ✅ PASS | 9 |
| AI Agents | ✅ PASS | 8 |
| Exceptions | ✅ PASS | 14 |
| MCP Tools | ✅ PASS | 8 |
| Data Models | ✅ PASS | 5 |
| Services | ✅ PASS | 13 |
| **Total** | **✅ 64/66 PASS** | **66** |

Full report available in `reports/pytest-phase4.xml`.

**Note:** 2 failing tests are related to conversation_id type handling (known issue from Phase III, not blocking Phase IV deployment).

## 📂 Project Structure
- `frontend/`: Next.js application with Tailwind CSS.
- `backend/`: FastAPI application with SQLModel.
- `backend/agents/`: AI logic and Gemini integration.
- `backend/tools/`: MCP tool implementations.
- `backend/internal_logging/`: Custom logging (renamed from 'logging' to avoid conflicts).
- `helm/todo-app/`: Helm charts for Kubernetes deployment.
- `k8s/`: Raw Kubernetes manifests.
- `specs/004-kubernetes-deployment/`: Phase IV specification documents.
- `reports/`: Test reports and deployment validation.

## 📊 Deployment Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Minikube K8s  │────▶│  Backend (x2)   │────▶│ Neon PostgreSQL │
│   Cluster       │     │  FastAPI        │     │ (External DB)   │
│                 │     └─────────────────┘     └─────────────────┘
│                 │     ┌─────────────────┐
│                 │────▶│ Frontend (x2)   │
│                 │     │ Next.js         │
└─────────────────┘     └─────────────────┘
```

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google Gemini API key
- `DATABASE_URL`: Neon PostgreSQL connection string
- `SECRET_KEY`: JWT secret for authentication
- `NEXT_PUBLIC_API_URL`: Backend API URL for frontend

### Helm Values
Customize deployment in `helm/todo-app/values.yaml`:
- Replica counts
- Resource limits
- Environment variables
- Service configurations

## 📝 Documentation
- [Phase IV Spec](specs/004-kubernetes-deployment/spec.md)
- [K8s Setup Guide](k8s/README.md)
- [Project Context](PROJECT_CONTEXT.md)
- [Change History](HISTORY.md)
