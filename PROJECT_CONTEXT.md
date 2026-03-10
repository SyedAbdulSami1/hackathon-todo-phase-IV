# PROJECT_CONTEXT.md

## Project
Todo App – Hackathon II (Spec-Driven Development)

## Current Phase
CURRENT_PHASE: IV – Local Kubernetes Deployment
COMPLETED_PHASES: I (Console App), II (Full-Stack Web), III (AI Chatbot)

## Phase IV Goal
Deploy Phase III chatbot on local Kubernetes using:
- Docker Desktop + Minikube
- Helm charts
- kubectl-ai / kagent for AIOps

## Architecture (Do NOT change)
- Frontend: Next.js (from Phase II/III)
- Backend: FastAPI (from Phase II/III)
- AI: OpenAI Agents SDK + MCP tools (from Phase III)
- DB: Neon PostgreSQL
- Chat: OpenAI ChatKit

## Important Files
- /frontend → Next.js app
- /backend → FastAPI app
- /specs → All spec files
- /HISTORY.md → Change log
- /QWEN.md → Qwen instructions

## Phase IV Tasks (micro tasks)
- [X] Task 1: Write Dockerfile for backend (already exists)
- [X] Task 2: Write Dockerfile for frontend (already exists)
- [X] Task 3: Write Helm chart for backend deployment (helm/todo-app exists)
- [X] Task 4: Write Helm chart for frontend deployment (helm/todo-app exists)
- [X] Task 5: Write Minikube setup instructions (k8s/README.md)
- [ ] Task 6: Test deploy on local cluster

## Active Task
Task 6: Test deploy on local cluster

## Completed Tasks (Phase IV)
- Kubernetes manifests created in k8s/ directory:
  - namespace.yaml, ingress.yaml
  - frontend/deployment.yaml, frontend/service.yaml
  - backend/deployment.yaml, backend/service.yaml, backend/secret.yaml
  - database/persistent-volume.yaml, database/persistent-volume-claim.yaml, database/secret.yaml
- Deployment documentation: k8s/README.md
- PHR created: history/prompts/kubernetes-deployment/014-kubernetes-manifests-implementation.green.prompt.md

## Completed Tasks
(Phase I, II, III all complete – see HISTORY.md)

## Notes
- No manual coding – specs first, then AI generates code
- Use kubectl-ai for deploy/scale/debug commands
- Free tools only (no paid services)
