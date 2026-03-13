# Umbrella Data Vault — Frontend

Interface web do **Umbrella Data Vault**: lista de personagens de Resident Evil com busca e página de detalhe (biografia, imagem, dados básicos). Consome a API do backend via RTK Query.

## Stack

- **Next.js 16** (App Router)
- **React 19**
- **Redux Toolkit** (RTK Query) para chamadas à API
- **Tailwind CSS 4** para estilos
- **TypeScript**

## Estrutura principal

```text
frontend/
├── app/
│   ├── layout.tsx       # Layout raiz, Header, Footer, metadata
│   ├── page.tsx         # Página inicial (lista de personagens + busca)
│   ├── [param]/
│   │   └── page.tsx     # Página de detalhe do personagem (slug na URL)
│   ├── layout/         # Header, Footer, List, Search
│   ├── lib/
│   │   └── api.ts       # RTK Query (getCharactersList, getCharacterData)
│   ├── providers/
│   │   └── Providers.tsx
│   ├── types/
│   │   └── types.d.ts   # CharacterListed, CharacterData
│   └── globals.css
├── public/
│   └── umbrella-icon.png
├── .env                 # NEXT_PUBLIC_API_BASE (URL da API)
└── package.json
```

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do `frontend/` (ou `.env.local`):

```env
NEXT_PUBLIC_API_BASE=http://127.0.0.1:8000
```

Ajuste a URL conforme o ambiente (desenvolvimento local do backend ou URL de deploy).

## Como rodar

Na raiz do repositório:

```bash
make dev-front
```

Ou, dentro de `frontend/`:

```bash
npm run dev
```

Acesse [http://localhost:3000](http://localhost:3000). A lista e o detalhe dependem do backend estar no ar e da URL configurada em `NEXT_PUBLIC_API_BASE`.

## Scripts (package.json)

| Script   | Comando           | Descrição              |
|----------|-------------------|------------------------|
| dev      | `npm run dev`     | Servidor de desenvolvimento |
| build    | `npm run build`   | Build de produção      |
| start    | `npm run start`   | Servidor de produção   |
| lint     | `npm run lint`    | ESLint                 |
| format   | `npm run format`  | Prettier               |

## Conteúdo e créditos

Os dados exibidos vêm do [Resident Evil Database](https://www.residentevildatabase.com/). O projeto é de estudo; créditos aos autores do site e da base de dados.
