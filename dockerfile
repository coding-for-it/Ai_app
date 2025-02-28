FROM python:3.9-slim

# Install system dependencies for building Python packages
RUN apt-get update && apt-get install -y build-essential libpq-dev

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
