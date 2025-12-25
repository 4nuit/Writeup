FROM python:3.13-slim
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd chall

COPY --chown=chall:chall app.py factory.py ./
COPY --chown=chall:chall templates ./templates

USER chall
EXPOSE 1337
CMD ["gunicorn", "--workers", "1", "--bind", "0.0.0.0:1337", "app:app"]
