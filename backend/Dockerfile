FROM p0bailey/docker-flask
MAINTAINER Fuyang Liu "liufu.ty@gmail.com"

COPY flask.conf /etc/nginx/sites-available/

# attach current dir
ADD . /var/www/app
RUN mkdir -p /var/www/app/log

RUN pip install -r /var/www/app/requirements.txt

CMD ["/usr/bin/supervisord"]
