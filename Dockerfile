FROM python:3.7.0-alpine3.8


# Current working directory
WORKDIR /app

COPY . /app

RUN pip3 install pipenv

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "api/app.py", "run", "--host=0.0.0.0", "--port=5000" ]
