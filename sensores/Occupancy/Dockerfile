FROM python:3.12-slim
WORKDIR /app
COPY occupancy.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "-u", "occupancy.py"]
