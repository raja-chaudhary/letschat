release: python manage.py migrate
web: daphne -b 0.0.0.0 -p 8001 letschat.asgi:application
worker: python manage.py runworker channels --settings=letschat.settings -v2