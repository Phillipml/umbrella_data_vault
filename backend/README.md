# Backend

Backend em Python responsável por:

- buscar o HTML do site fonte
- extrair a lista de personagens e os detalhes de um personagem
- expor uma API HTTP (FastAPI) para consumo pelo frontend

## Estrutura

```text
backend/
├── src/backend/
│   ├── main.py           # app FastAPI e rotas
│   ├── config.py         # cookies/headers para o scraper
│   ├── scraper.py        # requisições HTTP ao site fonte
│   └── parsers/
│       ├── character_list.py   # lista de personagens
│       └── character_detail.py # detalhes/biografia
└── tests/
    ├── test_scraper.py
    ├── test_character_list.py
    ├── test_character_detail.py
    └── test_main.py      # testes da API
```

## API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/characters_list` | Lista de personagens com `name` e `param` |
| GET | `/character-bio/{param}` | Dados e biografia do personagem (slug na URL). Retorna `null` se não existir. |

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
poetry run fastapi dev src/backend/main.py
```

Ou com uvicorn:

```bash
poetry run uvicorn backend.main:app --reload --app-dir src
```

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

- `GET /characters_list`: retorna 200 e lista; lista vazia quando não há personagens
- `GET /character-bio/{param}`: retorna 200 e dados quando existe; retorna 200 e `null` quando não existe

## Observações

- Os testes usam `mock` para simular respostas e evitar dependência de internet
- A API chama os parsers em tempo real; para muitos acessos, considere cache ou persistência
