# lifeinweeks

## About

## Frameworks
Backend is hosted via flask, which is served by uwsgi and Nginx in a docker
container.

## How to run:
* Frontend
    * `$ cd frontend`
    * `$ npm install` for the first time only
    * `$ npm run dev` to run the frontend code
* Backend
    * Install Python3 before running the following command.
    * `$ setup-local-python-env.sh`
    * `$ source YOUR_PYTHON_ENV/bin/activate`
    * `$ pip install -r backend/requirements`
    * `$ start_backend_local.sh`

## Appendix:
* Frontend code structure generation see here http://vuejs-templates.github.io/webpack/

## Other note:

### SSL certificate gen:
```
Tips:
https://www.linode.com/docs/security/ssl/create-a-self-signed-certificate-on-debian-and-ubuntu
https://www.linode.com/docs/security/ssl/provide-encrypted-resource-access-using-ssl-certificates-on-nginx
https://certbot.eff.org/docs/using.html#manual

Cleaning up challenges
Generating key (2048 bits): /etc/letsencrypt/keys/0000_key-certbot.pem
Creating CSR: /etc/letsencrypt/csr/0000_csr-certbot.pem

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at
   /etc/letsencrypt/live/lifeinweeks.ml/fullchain.pem. Your cert will
   expire on 2017-05-13. To obtain a new or tweaked version of this
   certificate in the future, simply run certbot-auto again. To
   non-interactively renew *all* of your certificates, run
   "certbot-auto renew"
```
And in the docker the key needs to be located at:
```
ssl_certificate      /etc/nginx/ssl/fullchain.pem;
ssl_certificate_key  /etc/nginx/ssl/privkey.pem;
```
