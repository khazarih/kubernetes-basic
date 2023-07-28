FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD [ "flask", "--app" , "main", "run", "--host", "0.0.0.0", "--port", "80", "--no-reload"]

