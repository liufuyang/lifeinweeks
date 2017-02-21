#!/bin/bash

set -e

cd frontend
npm run build
cd ..

./start_postgres_local.sh

cd backend
python app.py
