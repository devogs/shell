#!/bin/bash

apt update && apt upgrade -y
apt install net-tools -y
apt-get install openssh-server -y
systemctl enable ssh
systemctl start ssh
apt install ansible -y
