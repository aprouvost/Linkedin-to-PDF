FROM python3.8-alpine

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "flask", "run"]