docker build -f ./Customer/Dockerfile . -t tweets_read:1.0
docker run --network kafka-network -v C:/Users/svitl/PycharmProjects/Lab7/Customer:/tweets_progect_customer --rm tweets_read:1.0