release: python manage.py makemigrations home hub blog && python manage.py migrate

web: gunicorn happy_project.wsgi --log-file -