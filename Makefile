NPM = cd frontend && npm run
POETRY = cd ./backend/src && poetry run

install:
	cd backend/src && poetry install
	cd frontend && npm install

dev-frontend:
	${NPM} dev

dev-backend:
	${POETRY} fastapi dev index.py