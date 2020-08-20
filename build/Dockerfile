FROM python:latest

WORKDIR /app
COPY .. app/

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

EXPOSE 8080

CMD [ "python","app.py" ]