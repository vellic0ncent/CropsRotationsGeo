docker rm -f $(docker ps -a -q)
#docker-compose up --build
docker-compose up -d
docker ps
