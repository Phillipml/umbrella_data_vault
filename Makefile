NPM = cd frontend && npm run
POETRY = cd ./backend/src && poetry run

install:
	cd backend/src && poetry install
	cd frontend && npm install

dev-front:
	${NPM} dev

dev-back:
	${POETRY} fastapi dev index.py