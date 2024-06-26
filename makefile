STARTUP = python3 manage.py
BASE_URL = http://localhost:8000/

run-server:
	${STARTUP} runserver

app-browser:
	open ${BASE_URL}

startup: app-browser db-browser run-server

migration:
	${STARTUP} makemigrations blogs

run-migrations:
	${STARTUP} migrate

super-user:
	${STARTUP} createsuperuser

db-browser:
	open ${BASE_URL}admin/

db-terminal:
	${STARTUP} shell
