FROM python:3.8
COPY ./requirements.txt requirements.txt
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirementst.txt