FROM python:3.9

WORKDIR d_app

COPY ./d_app /d_app

RUN pip install -r /d_app/requirements.txt

RUN python manage.py migrate

EXPOSE 8082

CMD ["python3", "-u", "manage.py", "–host", "0.0.0.0", "–port", "8082"]

