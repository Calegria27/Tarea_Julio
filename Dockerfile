FROM python:3

WORKDIR /app

COPY ejemplo.py/ /app/ejemplo.py

CMD ["python","ejemplo.py"]
