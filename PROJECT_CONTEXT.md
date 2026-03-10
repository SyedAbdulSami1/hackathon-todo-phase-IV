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
- [ ] Task 1: Write Dockerfile for backend
- [ ] Task 2: Write Dockerfile for frontend
- [ ] Task 3: Write Helm chart for backend deployment
- [ ] Task 4: Write Helm chart for frontend deployment
- [ ] Task 5: Write Minikube setup instructions
- [ ] Task 6: Test deploy on local cluster

## Active Task
Task 1: Write Dockerfile for backend

## Completed Tasks
(Phase I, II, III all complete – see HISTORY.md)

## Notes
- No manual coding – specs first, then AI generates code
- Use kubectl-ai for deploy/scale/debug commands
- Free tools only (no paid services)
