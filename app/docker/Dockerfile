
FROM python:3.8-alpine
WORKDIR /app
RUN apk update && \
    apk add \
      bash \
      make \
      gcc \
      g++ \
      postgresql-dev \
      jpeg-dev \
      zlib-dev
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
ENV PYTHONDONTWRITEBYTECODE=1
ENTRYPOINT [ "docker/entrypoint.sh" ]
COPY ./ ./
