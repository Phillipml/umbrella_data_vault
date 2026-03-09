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
| GET | `/` | Health: `{"Umbrella": "Data System"}` |
| GET | `/characters-list` | Lista de personagens (`name`, `param`) |
| GET | `/character-bio/{param}` | Biografia e dados do personagem (ou `null` se não encontrado) |

Em caso de falha no site fonte (timeout, indisponibilidade), os endpoints de lista e biografia retornam **503** com a mensagem `"Source temporarily unavailable"`.

Documentação interativa (Swagger): após subir o servidor, acesse `/docs`.

## Deploy (Vercel)

O backend está preparado para deploy na Vercel como projeto separado (Root Directory = `backend`). Ver instruções em `backend/README.md`.

## Próximos passos

- Consumir a API no frontend
- (Opcional) Cache ou persistência para reduzir chamadas ao site fonte
