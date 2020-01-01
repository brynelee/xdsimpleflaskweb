FROM python:alpine

WORKDIR /usr/src/app

RUN pip install flask

COPY . .

CMD [ "python", "./webapp.py" ]
