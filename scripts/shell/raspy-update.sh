#!/bin/sh
#
# pulls only latest code from github.

echo "gitting latest code..."
sudo git pull -v https://github.com/zoroloco/raspy-bot-controller.git
echo "restarting raspy..."
sudo systemctl restart raspy.service
