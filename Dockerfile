FROM python:3.11-slim

RUN mkdir -p /usr/src/rizikovarada
WORKDIR /usr/src/rizikovarada

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "run.py" ]
