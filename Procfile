release: python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser --no-input 

web: gunicorn happy_project.wsgi --log-file -