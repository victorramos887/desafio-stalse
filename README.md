# Desafio Stalse - Mini Inbox

Projeto full stack para gerenciamento de tickets de suporte, com dashboard de metricas, API REST e interface web.

## Visao Geral

- `backend/`: API em FastAPI, banco via SQLAlchemy, migracoes com Alembic, seeds e testes com Pytest.
- `frontend/`: aplicacao web em Next.js (App Router), com listagem de tickets, detalhe e dashboard de metricas.
- `infra/`: orquestracao com Docker Compose (frontend, backend e n8n).
- `docs/`: diagramas e artefatos de documentacao.

## Telas

- `/tickets`: tabela com filtros e listagem de tickets.
- `/tickets/[ticketId]`: detalhe e atualizacao de status/prioridade.
- `/metrics`: dashboard com cards, grafico e top assuntos.

## Como Subir o Projeto

### Opcao 1 - Docker Compose (recomendado)

```bash
cd infra
docker compose up -d --build
```

Acessos:
- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`
- N8N: `http://localhost:5678`

### N8N: Fluxo Simples (um comando)

Para subir igual em qualquer maquina, basta:

```bash
cd infra
docker compose up -d --build
```

A chave de criptografia do n8n esta fixa no `compose.yml`, entao nao depende de `.env` para iniciar.

Dados do n8n ficam em `infra/n8n_data`.

Backup rapido:
```bash
cd infra
./scripts/n8n-backup.sh
```

Esse comando gera:
- `backups/n8n_data-AAAAmmdd-HHMMSS.tar.gz` (snapshot completo da pasta `n8n_data`)
- `backups/workflows-AAAAmmdd-HHMMSS.json` (workflows em JSON)
- `backups/credentials-decrypted-AAAAmmdd-HHMMSS.json` (credenciais em texto descriptografado, quando existirem)

Restore em outro PC:
```bash
cd infra
./scripts/n8n-restore.sh ./backups/n8n_data-AAAAmmdd-HHMMSS.tar.gz
```

Observacao:
- O projeto usa um unico `compose.yml` e salva dados do n8n em `infra/n8n_data`.

### Opcao 2 - Local (sem Docker)

Backend:
```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```

## Estrutura e Padroes

- Arquitetura por features no backend (`app/features/...`).
- App Router no frontend (`src/app/...`) com separacao por paginas.
- Tipagem com TypeScript no frontend e validacao de schema no backend.

## Links dos READMEs Especificos

- Backend: [`backend/README.md`](backend/README.md)
- Frontend: [`frontend/README.md`](frontend/README.md)

## Dataset

Fonte principal: Kaggle
- `suraj520/customer-support-ticket-dataset`
- https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset
