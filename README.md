# Umbrella Data Vault

Projeto de estudo para coletar dados de personagens de Resident Evil e expor essas informações para consumo no frontend.

## Estrutura

- `backend/`: código Python responsável por buscar, transformar os dados e expor a API HTTP

## Status Atual

O backend possui:

- **Scraper** para buscar HTML do site fonte
- **Parsers** para listar personagens e montar os detalhes de um personagem
- **API FastAPI** com endpoints para lista de personagens e biografia
- **Testes automatizados** para scraper, parsers e rotas da API

## API

A API expõe:

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/characters_list` | Lista de personagens (`name`, `param`) |
| GET | `/character-bio/{param}` | Biografia e dados do personagem (ou `null` se não encontrado) |

Documentação interativa (Swagger): após subir o servidor, acesse `/docs`.

## Próximos passos

- Consumir a API no frontend
- (Opcional) Cache ou persistência para reduzir chamadas ao site fonte
