# Backend

Backend em Python responsável por:

- buscar o HTML do site fonte
- extrair a lista de personagens e os detalhes de um personagem
- expor uma API HTTP (FastAPI) para consumo pelo frontend

## Estrutura

```text
backend/
├── src/
│   ├── index.py          # entrypoint FastAPI (Vercel + local)
│   └── backend/
│       ├── config.py     # cookies/headers para o scraper
│       ├── scraper.py    # requisições HTTP ao site fonte
│       └── parsers/
│           ├── character_list.py   # lista de personagens
│           └── character_detail.py # detalhes/biografia
├── requirements.txt      # dependências para pip (ex.: Vercel)
├── vercel.json           # (opcional) config do deploy
└── tests/
    ├── test_scraper.py
    ├── test_character_list.py
    ├── test_character_detail.py
    └── test_main.py      # testes da API
```

O `src/index.py` configura o `sys.path` para importar o pacote `backend` e expõe o app FastAPI (rotas e tratamento de erro 503).

## API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Health: `{"Umbrella": "Data System"}` |
| GET | `/characters-list` | Lista de personagens com `name` e `param` |
| GET | `/character-bio/{param}` | Dados e biografia do personagem (slug na URL). Retorna `null` se não existir. |

Se o site fonte estiver indisponível ou der timeout, `/characters-list` e `/character-bio/{param}` retornam **503** com `detail: "Source temporarily unavailable"`.

Exemplo de resposta de `/characters_list`:

```json
[
  {"name": "Ada Wong", "param": "ada-wong"},
  {"name": "Albert Wesker", "param": "albert-wesker"}
]
```

Exemplo de resposta de `/character-bio/ada-wong`:

```json
{
  "Name": "Ada Wong",
  "Img": "https://...",
  "Ano de nascimento": "1974",
  "Altura": "1,70 m",
  "Bio": "..."
}
```

## Como instalar

Com Poetry:

```bash
poetry install
```

Para ativar o ambiente virtual:

```bash
poetry shell
```

## Como rodar a API

Na raiz do backend (`backend/`):

```bash
poetry run fastapi dev src/index.py
```

Ou com uvicorn (garantindo que `src` esteja no path):

```bash
cd backend && set PYTHONPATH=src && poetry run uvicorn index:app --reload
```

No Linux/macOS use `export PYTHONPATH=src` em vez de `set PYTHONPATH=src`.

Documentação interativa: http://127.0.0.1:8000/docs

## Como rodar os testes

Com pytest (recomendado):

```bash
poetry run pytest
```

Com unittest:

```bash
poetry run python -m unittest discover -s tests -p "test_*.py"
```

## O que os testes cobrem

### `tests/test_scraper.py`

Comportamento do scraper (sem acessar a internet).

- Requisição com status 200 retorna o HTML
- Requisição com falha retorna `"Error"`

### `tests/test_character_list.py`

Extração da lista de personagens a partir do HTML.

- Monta corretamente os campos `name` e `param`
- Retorna lista vazia quando não encontra personagens

### `tests/test_character_detail.py`

Extração dos dados de um personagem.

- Monta nome, imagem, bio e atributos básicos
- Retorna `None` quando o scraper falha
- Não quebra quando falta "Ano de nascimento" no HTML

### `tests/test_main.py`

Rotas da API FastAPI (parsers mockados).

- `GET /characters-list`: retorna 200 e lista; lista vazia quando não há personagens
- `GET /character-bio/{param}`: retorna 200 e dados quando existe; retorna 200 e `null` quando não existe

## Deploy na Vercel

1. Crie um projeto na Vercel apontando para o repositório.
2. Defina **Root Directory** = `backend`.
3. **Install Command:** `pip install -r requirements.txt`
4. **Build Command** e **Output Directory:** deixe em branco.
5. Faça o deploy. A Vercel detecta o app FastAPI em `src/index.py`.

A API ficará disponível em `https://seu-projeto.vercel.app` (ex.: `/`, `/characters-list`, `/character-bio/ada-wong`).

## Observações

- Os testes usam `mock` para simular respostas e evitar dependência de internet.
- A API chama os parsers em tempo real; para muitos acessos, considere cache ou persistência.
- Em falha do site fonte, as rotas de lista e biografia retornam 503 em vez de derrubar a função.
