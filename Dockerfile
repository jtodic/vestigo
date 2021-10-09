FROM python:3.9
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
ENV PORT 8080
CMD [ "python", "./hello-app.py" ]