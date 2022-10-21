#!/bin/sh

apt-get update
apt-get upgrade -y
apt install curl -y

# Install youtube-dl
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
