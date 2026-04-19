FROM python:3.11-slim

ARG BUILD_ENV=production
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd -r appuser -g ${GROUP_ID} && \
    useradd -r -g appuser -u ${USER_ID} -m appuser

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN echo "=== Проверка доступа к PyPI ===" && \
    curl -I https://pypi.org/simple/ 2>/dev/null | head -n 1 || \
    (echo "=== НЕТ ДОСТУПА К PyPI ===" && exit 1)

RUN pip install --upgrade pip && \
    pip config set global.index-url https://pypi.org/simple

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/data && \
    chown -R appuser:appuser /app

VOLUME ["/app/data"]

USER appuser

ENTRYPOINT ["sh", "-c", "python manage.py migrate && python data.py && python manage.py runserver 0.0.0.0:8000"]