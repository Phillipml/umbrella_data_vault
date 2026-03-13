# Umbrella Data Vault

Projeto de estudo para coletar dados de personagens de Resident Evil e exibir em uma interface web. O backend busca e transforma os dados do site fonte; o frontend consome a API e exibe lista e detalhes dos personagens.

## Estrutura

| Pasta       | Descrição |
|------------|-----------|
| `backend/` | API em Python (FastAPI): scraper, parsers e endpoints HTTP |
| `frontend/`| Aplicação Next.js (React): lista de personagens, busca e página de detalhe |

## Como rodar

### Pré-requisitos

- Node.js e npm (frontend)
- Python 3 e Poetry (backend)

### Instalação

Na raiz do repositório:

```bash
make install
```

Isso executa `poetry install` no backend e `npm install` no frontend.

### Desenvolvimento

- **Frontend** (Next.js em http://localhost:3000):

  ```bash
  make dev-front
  ```

- **Backend** (FastAPI):

  ```bash
  make dev-back
  ```

O frontend consome a API via `NEXT_PUBLIC_API_BASE` (ex.: `http://127.0.0.1:8000`). Configure no `frontend/.env` se necessário.

### Outros comandos (Makefile)

| Comando        | Ação                    |
|----------------|-------------------------|
| `make format-front` | Prettier no frontend   |
| `make format-back`   | Ruff no backend        |
| `make lint-front`    | ESLint no frontend     |

## API (backend)

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Health: `{"Umbrella": "Data System"}` |
| GET | `/characters-list` | Lista de personagens (`name`, `param`) |
| GET | `/character-bio/{param}` | Biografia e dados do personagem (ou `null` se não encontrado) |

Em falha do site fonte, os endpoints de lista e biografia retornam **503** com `"Source temporarily unavailable"`. Documentação interativa: `/docs` (Swagger).

Detalhes de instalação, testes e deploy do backend: [backend/README.md](backend/README.md).

## Documentação por parte

- [backend/README.md](backend/README.md) — API, testes, deploy na Vercel
- [frontend/README.md](frontend/README.md) — Next.js, estrutura e variáveis de ambiente
