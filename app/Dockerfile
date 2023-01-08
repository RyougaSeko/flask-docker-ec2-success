FROM ubuntu:22.04
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update -y
RUN apt install python3-pip -y
RUN apt-get update -y
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg
RUN apt-get install git -y
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

RUN mkdir -p /var/www
COPY ./requirements.txt /var/www
RUN pip3 install --no-cache-dir torch==1.13.1
RUN pip3 install -r /var/www/requirements.txt

COPY ./gunicorn.py /var/www

COPY ./app.py /var/www

WORKDIR /var/www

CMD ["gunicorn", "app:app", "--config", "/var/www/gunicorn.py", "--timeout", "500"]