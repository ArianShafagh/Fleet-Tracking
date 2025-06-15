FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install paho-mqtt mysql-connector-python pymongo requests
CMD ["python", "sqlS.py"] 
