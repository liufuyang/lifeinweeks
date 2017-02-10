#!/bin/bash

cd frontend
npm run build
cd ..

cd backend
python app.py
