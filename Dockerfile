FROM python:3.12

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:root_app", "--host", "0.0.0.0", "--port", "5000"]