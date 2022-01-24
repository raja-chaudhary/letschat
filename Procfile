release: python manage.py migrate
web: daphne letschat.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=letschat.settings -v2