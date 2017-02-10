FROM p0bailey/docker-flask
MAINTAINER Fuyang Liu "liufu.ty@gmail.com"

# Use python3 and pip3, also update uwsgi.ini to use plugins=python3
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev uwsgi-plugin-python3
RUN pip3 install uwsgi

COPY flask.conf /etc/nginx/sites-available/

# attach current dir
ADD . /var/www/app
RUN mkdir -p /var/www/app/log

RUN pip3 install -r /var/www/app/requirements.txt

CMD ["/usr/bin/supervisord"]
