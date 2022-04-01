#!/bin/bash

sudo systemctl enable kubelet
sudo kubeadm config images pull

### 
sudo kubeadm init \
  --pod-network-cidr=172.18.0.0/16 \
  --upload-certs
  
### Configure kubectl 
mkdir -p $HOME/.kube
sudo cp -f /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

### Install Calico
kubectl create -f https://docs.projectcalico.org/manifests/tigera-operator.yaml 
kubectl create -f https://docs.projectcalico.org/manifests/custom-resources.yaml
