FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV GRADIO_ANALYTICS_ENABLED=False

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py bearing_and_distance_calculator.py .

EXPOSE 7860

CMD ["python", "app.py"]
