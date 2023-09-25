#!/usr/bin/env bash
# script to prepare server for deployment

if [ ! -d "/etc/nginx" ]; then
   sudo apt-get -y update
   sudo apt-get -y install nginx
fi
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    <h1>Hello it is me, shehab<h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf  /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
serv_static="location /hbnb_static/ {\n\t alias /data/web_static/current/; \n}\n"
sudo sed -i "33i $serv_static" /etc/nginx/sites-available/default
sudo service nginx restart
