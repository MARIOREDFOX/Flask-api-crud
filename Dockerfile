FROM python3


# Current working directory
WORKDIR /app

COPY . /app

RUN pip3 install pipenv

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]

EXPOSE 5000

CMD [ "app.py", "run", "--host=0.0.0.0" ]
