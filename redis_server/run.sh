docker stop nluredisdummy
docker container rm nluredisdummy
docker image rm nlu_redis_dummy
docker build -t nlu_redis_dummy .
docker run -p 6379:6379 --name=nluredisdummy -i -v ./LocalStorage-redis:/app/data -d nlu_redis_dummy