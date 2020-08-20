FROM python:latest

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "uvicorn","app:app","--reload","--port", "8080","--host","0.0.0.0" ]