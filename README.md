# Umbrella Data Vault

Projeto de estudo para coletar dados de personagens de Resident Evil e expor essas informacoes para consumo no frontend.

## Estrutura

- `backend/`: codigo Python responsavel por buscar e transformar os dados

## Status Atual

O backend atualmente possui:

- scraper para buscar HTML do site fonte
- parser para listar personagens
- parser para montar os detalhes de um personagem
- testes automatizados para scraper e parsers

## Proximo Passo

O proximo passo natural do projeto e criar endpoints HTTP para transformar essa logica em uma API consumida pelo frontend.