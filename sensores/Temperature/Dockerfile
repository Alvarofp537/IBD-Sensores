FROM python:3.12-slim
WORKDIR /app
COPY temperature.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "-u", "temperature.py"]
