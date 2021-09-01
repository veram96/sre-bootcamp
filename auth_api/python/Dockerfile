FROM python:3-alpine


WORKDIR /api


COPY requirements.txt .


RUN python3 -m pip install -r requirements.txt


COPY src/ .

EXPOSE 8000

CMD [ "python", "./api.py" ]
