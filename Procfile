release: python manage.py makemigrations blog clientauth gallery home hub watchdog && python manage.py migrate && python manage.py createsuperuser --no-input

web: gunicorn happy_project.wsgi --log-file -
