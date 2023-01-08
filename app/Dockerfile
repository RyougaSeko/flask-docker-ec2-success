FROM ubuntu:22.04
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update -y
RUN apt install python3-pip -y

RUN mkdir -p /var/www
COPY ./requirements.txt /var/www
RUN pip install -r /var/www/requirements.txt

COPY ./gunicorn.py /var/www

COPY ./app.py /var/www

WORKDIR /var/www

CMD ["gunicorn", "app:app", "--config", "/var/www/gunicorn.py" ]
# FROM ubuntu:22.04

# RUN apt-get update -y
# RUN apt-get install python3-pip -y
# RUN apt-get install gunicorn3 -y

# COPY requirements.txt requirements.txt
# COPY flaskapp /opt/

# RUN pip3 install -r requirements.txt
# WORKDIR /opt/
# EXPOSE 5000

# CMD ["gunicorn3", "-b", "0.0.0.0:5000", "app:app", "--workers=5"]
