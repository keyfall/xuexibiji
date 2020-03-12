#!/bin/bash

ls 
/root/kubeadm-basic.images > /tmp/image-list.txt


cd /root/kubeadm-basic.images


for i in $( cat /tmp/image-list.txt)

do
        
	docker load -i $i

done



rm -rf /tmp/image-list.txt