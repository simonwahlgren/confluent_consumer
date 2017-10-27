FROM fyndiq/python-alpine-kafka:latest

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /code
COPY confluent-consumer.py /code

CMD ./confluent-consumer.py
