release: python manage.py makemigrations home hub blog watchdog clientauth && python manage.py migrate && python manage.py createsuperuser --no-input

web: gunicorn happy_project.wsgi --log-file -
