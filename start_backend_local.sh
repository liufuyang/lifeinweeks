#!/bin/bash

set -e

cd frontend
npm run build
cd ..

cd backend
python app.py
