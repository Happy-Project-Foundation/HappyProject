release: python manage.py makemigrations blog clientauth gallery home hub watchdog && python manage.py migrate

web: gunicorn happy_project.wsgi --log-file -
