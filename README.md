docker build --tag python-docker .
docker images
docker run -d -p 5000:5000 python-docker
docker rmi -f python-docker 