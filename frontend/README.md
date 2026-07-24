# Frontend - Mini Inbox Web

Interface web em Next.js para operacao de tickets e visualizacao de metricas.

## Stack

- Next.js 16 (App Router)
- React 19
- TypeScript
- CSS Modules
- Recharts (graficos)
- Lucide React (icones)

## Estrutura

- `src/app/`: paginas e rotas.
  - `tickets/page.tsx`: lista de tickets.
  - `tickets/[ticketId]/page.tsx`: detalhe do ticket.
  - `metrics/page.tsx`: dashboard de metricas.
- `src/components/`: componentes reutilizaveis (header, tabela etc).
- `src/services/`: comunicacao com API.
- `src/utils/`: utilitarios (datas, urls).
- `src/types/`: tipos TypeScript.

## Como Rodar

```bash
cd frontend
npm install
npm run dev
```

App: `http://localhost:3000`

## Variaveis de Ambiente

Quando usar Docker Compose:
- `INTERNAL_API_URL=http://backend:8000` (SSR dentro do container)
- `NEXT_PUBLIC_API_URL=http://localhost:8000` (browser no host)

Quando rodar local sem Docker:
- `NEXT_PUBLIC_API_URL=http://localhost:8000`

## Scripts

```bash
npm run dev
npm run build
npm run start
npm run lint
```

## Como Adicionar Nova Tela

1. Criar rota em `src/app/nova-rota/page.tsx`.
2. Criar CSS Module ao lado (`page.module.css`) se necessario.
3. Se precisar de dados da API, adicionar funcao em `src/services/`.
4. Criar tipos em `src/types/` para payloads.
5. Atualizar navegacao no `Header` se a tela for publica no menu.

## Padrao de Organizacao

- Pagina server-first quando possivel (SSR) para dados iniciais.
- Componentes interativos em client components (`'use client'`).
- Regras de formato e transformacao em `utils/`.
- Chamadas de API centralizadas em `services/`.

## Manutencao Recomendada

- Rodar `npm run lint` antes de commit.
- Evitar fetch direto em muitos arquivos; prefira `services/`.
- Reutilizar componentes e tipos para evitar duplicacao.
- Revisar comportamento SSR x Client ao mexer em URLs da API.
