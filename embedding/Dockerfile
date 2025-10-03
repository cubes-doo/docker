FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl git \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir \
    "fastapi>=0.110" "uvicorn[standard]>=0.23" "pydantic>=2" \
    "sentence-transformers>=2.6" \
 && pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cpu \
    torch torchvision torchaudio

ENV MODEL_NAME=intfloat/multilingual-e5-large \
    MODEL_CACHE=/models \
    TRANSFORMERS_CACHE=/models \
    HF_HOME=/models \
    SENTENCE_TRANSFORMERS_HOME=/models

RUN mkdir -p /models && \
    python - <<'PY'
from sentence_transformers import SentenceTransformer
import os
name  = os.environ.get("MODEL_NAME", "intfloat/multilingual-e5-large")
cache = os.environ.get("MODEL_CACHE", "/models")
m = SentenceTransformer(name, cache_folder=cache)
print("Downloaded", name, "-> dim =", m.get_sentence_embedding_dimension())
PY

COPY ./app.py /app/app.py

RUN useradd -m -u 10001 appuser && \
    chown -R appuser:appuser /models /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -fsS http://127.0.0.1:8000/docs >/dev/null || exit 1

ENV HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]