FROM python:3.11-slim-bookworm
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP manage.py
EXPOSE 8000
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]