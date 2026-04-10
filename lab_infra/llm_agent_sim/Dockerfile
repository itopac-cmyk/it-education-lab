FROM python:3.10-slim
WORKDIR /app
COPY agent.py .
RUN pip install Flask==2.2.5 && apt-get update && apt-get install -y iputils-ping
EXPOSE 5002
CMD ["python", "agent.py"]
