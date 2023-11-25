FROM python:3.10

WORKDIR .

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./api_heart_attack_prediction.py" ]
