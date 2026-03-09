# Backend

Backend em Python responsavel por:

- buscar o HTML do site fonte
- extrair a lista de personagens
- extrair os detalhes de um personagem

No momento, o projeto ainda esta na fase de parser e testes. A camada de endpoints HTTP sera o proximo passo.

## Estrutura

```text
backend/
├─ src/backend/
│  ├─ scraper.py
│  └─ parsers/
│     ├─ character_list.py
│     └─ character_detail.py
└─ tests/
   ├─ test_scraper.py
   ├─ test_character_list.py
   └─ test_character_detail.py
```

## Arquivos Principais

### `src/backend/scraper.py`

Responsavel por fazer as requisicoes HTTP para o site fonte.

- `get_character_list()`: busca a pagina com todos os personagens
- `get_character_content(param)`: busca a pagina de detalhe de um personagem pelo parametro da URL

### `src/backend/parsers/character_list.py`

Transforma o HTML da pagina de personagens em uma lista de objetos com:

- `name`
- `param`

Exemplo de retorno:

```python
[
    {"name": "Ada Wong", "param": "ada-wong"},
    {"name": "Albert Wesker", "param": "albert-wesker"},
]
```

### `src/backend/parsers/character_detail.py`

Transforma o HTML de um personagem em um dicionario com informacoes basicas.

Exemplo de retorno:

```python
{
    "Name": "Ada Wong",
    "Img": "https://img.example/ada.png",
    "Ano de nascimento": "1974",
    "Altura": "1,70 m",
    "Bio": "Ada e uma espia misteriosa."
}
```

## Como instalar

Com Poetry:

```bash
poetry install
```

Se preferir usar o ambiente virtual do Poetry:

```bash
poetry shell
```

## Como rodar os testes

O projeto tem `pytest` instalado, mas os testes foram escritos de forma simples com `unittest`. Por isso, voce pode rodar de dois jeitos.

### Rodando com pytest

```bash
pytest
```

### Rodando com unittest

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## O que os testes cobrem

### `tests/test_scraper.py`

Valida o comportamento do scraper sem acessar a internet de verdade.

- quando a requisicao responde `200`, retorna o HTML
- quando a requisicao falha, retorna `"Error"`

### `tests/test_character_list.py`

Valida a extracao da lista de personagens.

- monta corretamente os campos `name` e `param`
- retorna lista vazia quando nao encontra personagens no HTML

### `tests/test_character_detail.py`

Valida a extracao dos dados de um personagem.

- monta nome, imagem, bio e atributos basicos
- retorna `None` quando o scraper falha
- nao quebra quando falta `"Ano de nascimento"` no HTML

## Observacoes

- Os testes usam `mock` para simular respostas e evitar dependencia de internet
- O objetivo atual e manter os parsers confiaveis antes de criar os endpoints
- Quando a API for criada, o ideal sera adicionar testes para as rotas tambem
