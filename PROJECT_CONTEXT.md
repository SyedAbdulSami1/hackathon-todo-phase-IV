# PROJECT_CONTEXT.md – Hackathon II (Phase IV)

## CURRENT_STATUS
- **Phase:** IV (Local Kubernetes Deployment)
- **Completed:** I (Console), II (Web), III (Chatbot)
- **Goal:** Deploy Phase III on Minikube using Helm & Docker.

## ARCHITECTURE (DO NOT CHANGE)
- **Frontend:** Next.js 16+ (Phase II/III)
- **Backend:** FastAPI + OpenAI Agents SDK (Phase III)
- **DB:** Neon PostgreSQL
- **Infra:** Docker, Minikube, Helm, kubectl-ai

## FILE STRUCTURE (SOURCE OF TRUTH)
- `/frontend` → Next.js app
- `/backend` → FastAPI app
- `/specs` → All spec files (SDD Required)
- `/helm` → Helm charts (todo-app)
- `/k8s` → Raw manifests (namespace, ingress, deployments, services, secrets, PV/PVC)
- `/docs` → k8s/README.md (Setup instructions)
- `/history` → Prompt logs & Iterations

## TASK TRACKER (Phase IV)
- [x] Dockerfile (Backend/Frontend)
- [x] Helm Charts (Backend/Frontend)
- [x] K8s Manifests (Deployments, Services, Secrets)
- [x] Documentation (k8s/README.md)
- [ ] **Task: Final Deployment Validation & Pytest**

## ACTIVE TASK
**Validate Deployment & Run Pytest**
1. Ensure cluster is running (Minikube).
2. Run backend pytest suite.
3. Save report to `/reports/pytest-phase4.xml`.
4. Verify Helm release status.

## POST-PHASE RULES (CRITICAL)
1. **Pytest Requirement:** After Phase IV completion, MUST run `pytest` on backend.
2. **Report Saving:** Save test report in `/reports` folder for teacher proof.
3. **No Manual Code:** All fixes must be spec-driven.
4. **AIOps:** Use `kubectl-ai` or `kagent` for cluster checks.

## NOTES FOR AI
- Trust this file over scanning directory.
- Do not recreate existing files (check list above).
- Focus on **Deployment Stability** and **Testing Proof**.