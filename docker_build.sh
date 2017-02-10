
eval $(docker-machine env default)

cd frontend
npm run build
cd ..

cd backend
docker build -t liufuyang/lifeinweeks:latest .
