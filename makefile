STARTUP = python3 manage.py
BASE_URL = http://localhost:8000/

collect-static:
	${STARTUP} collectstatic

lint:
	ruff check .

run-server:
	${STARTUP} runserver

app-browser:
	open ${BASE_URL}

startup: db-browser app-browser run-server

migration:
	${STARTUP} makemigrations blogs

run-migrations:
	${STARTUP} migrate

db-super-user:
	${STARTUP} createsuperuser --username admin --email admin@admin.com --noinput

db-browser:
	open ${BASE_URL}admin/

db-terminal:
	${STARTUP} shell

db-flush:
	${STARTUP} flush --noinput

db-load-data:
	python ./generate_sample_data.py

db-refresh: db-flush db-super-user db-load-data
