#!/bin/bash

# Enable ssh password authentication 
echo "[TASK 1] Enable ssh password authentication"
sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
echo "PermitRootLogin yes" >> /etc/sshd/sshd_config
systemctl reload sshd