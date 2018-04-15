FROM python:3.6

RUN mkdir /neo4j

COPY code/ ./

RUN pip install neo4j-driver

COPY requirements.txt requirements.txt

COPY code /src/code

RUN pip install -r requirements.txt

# ENTRYPOINT ["python3", "-m", "code"]
