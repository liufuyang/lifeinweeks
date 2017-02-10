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
    * `$ pip install -r backend/requirements`
    * `$ start_backend_local.sh`
