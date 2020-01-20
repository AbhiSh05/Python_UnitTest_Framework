FROM python:3

ADD . /app/

RUN pip install -r ./app/requirements.txt

ENV PYTHONPATH "${PYTONPATH}:/app"

CMD [ "python", "./app/run.py" ]
