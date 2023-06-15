FROM python:3-alpine3.17

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./flask ./app/flask

WORKDIR /app/flask/

ENTRYPOINT [ "python" ]

CMD ["impersonation.py" ]