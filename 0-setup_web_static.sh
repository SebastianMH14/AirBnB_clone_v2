#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu /data/
sed -i '57 i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
