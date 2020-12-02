FROM python:3.7

WORKDIR /app

RUN pip install pipenv
RUN pip install gunicorn[gevent]

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --system --skip-lock

COPY . ./

EXPOSE 4000

CMD gunicorn --worker-class gevent --workers 2 --bind 0.0.0.0:4000 app:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
