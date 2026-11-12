# Stage 1

FROM python:3.12-slim AS builder

WORKDIR /build

COPY requirements.txt ./

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

RUN useradd --create-home --uid 1000 appuser

USER 1000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]