FROM python:3

WORKDIR /home/bot

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py" ]
