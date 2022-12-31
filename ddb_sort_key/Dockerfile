FROM python:3


RUN pip install boto3

COPY . .

CMD [ "python", "./read_with_sort_key.py" ]
