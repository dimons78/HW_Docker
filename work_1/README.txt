
sudo docker build -t my-nginx .

sudo docker run --name my-nginx-server -d -p 8081:80 my-nginx

