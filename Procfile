release: python manage.py makemigrations home && python manage.py migrate

web: gunicorn happy_project.wsgi --log-file -