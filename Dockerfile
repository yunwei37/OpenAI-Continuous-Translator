FROM ubuntu:22.04
ADD . /app
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git pip \
    && rm -rf /var/lib/apt/lists/* && pip3 install --target=/app -r requirements.txt

WORKDIR /app
ENV PYTHONPATH /app
CMD ["python3", "/app/main.py"]
