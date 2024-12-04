#!/bin/bash
# install docker
sudo dnf install -y docker
# Start and enable docker service
sudo systemctl start docker
sudo systemctl enable docker
# add user to docker group
sudo usermod -aG docker $USER
# install ecs agent
curl -O https://s3.eu-west-3.amazonaws.com/amazon-ecs-agent-eu-west-3/amazon-ecs-init-latest.x86_64.rpm
sudo yum localinstall -y amazon-ecs-init-latest.x86_64.rpm
# setup ecs.service
sudo sed -i '/^\[Unit\]/a After=cloud-final.service' /lib/systemd/system/ecs.service
sudo systemctl daemon-reload
# mount the ec2 instance to ecs cluster
echo "ECS_CLUSTER=shiba-cluster" | sudo tee /etc/ecs/ecs.config
# start ecs agent
sudo systemctl start ecs.service
sudo systemctl enable ecs.service
