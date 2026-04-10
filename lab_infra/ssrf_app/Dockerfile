FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN pip install Flask==2.2.5
EXPOSE 5001
CMD ["python", "app.py"]
