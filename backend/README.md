# Backend - Mini Inbox API

API REST para tickets e metricas, com FastAPI + SQLAlchemy + Alembic.

## Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- Alembic
- Ruff (formatacao/lint)
- Pytest
- Uvicorn
- UV (gerenciamento de ambiente/dependencias)

## Estrutura

- `app/main.py`: bootstrap da API.
- `app/core/`: configuracoes e conexao de banco.
- `app/features/tickets/`: dominio de tickets (api, schemas, service, repository, models).
- `app/features/metrics/`: pipeline e endpoint de metricas.
- `seeds/`: carga inicial de dados.
- `migrations/`: historico de migracoes Alembic.
- `tests/`: testes automatizados.

## Como Rodar

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API: `http://localhost:8000`

## Seeds

```bash
cd backend
uv run python -m app.seeds.seed
```

## Migracoes (Alembic)

Criar migracao:
```bash
cd backend
uv run alembic revision --autogenerate -m "descricao_da_mudanca"
```

Aplicar migracoes:
```bash
cd backend
uv run alembic upgrade head
```

## Formatacao e Qualidade

Formatar com Ruff:
```bash
cd backend
uv run ruff format .
```

Lint com Ruff:
```bash
cd backend
uv run ruff check .
```

Rodar testes:
```bash
cd backend
uv run pytest
```

## Como Adicionar Nova Feature

1. Criar pasta em `app/features/nome_feature/`.
2. Separar camadas: `api/`, `schemas/`, `service/`, `repository/`, `models/`.
3. Registrar rotas no `main.py` (ou modulo de roteamento atual).
4. Criar/ajustar model e gerar migracao Alembic.
5. Adicionar testes de API e regra de negocio em `tests/`.

## Manutencao Recomendada

- Sempre rodar `ruff format` e `ruff check` antes de commit.
- Sempre criar migracao quando houver mudanca de schema.
- Garantir cobertura minima de testes para endpoint novo.
- Manter seeds atualizados para ambiente local de desenvolvimento.
