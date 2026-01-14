## Do this only on the first Master 

```
curl -sfL https://get.k3s.io | sh -s - server --node-taint CriticalAddonsOnly=true:NoExecute --tls-san load_balancer_ip_or_hostname
```

test with
```
sudo k3s kubectl get nodes
```
to add additional servers, get token from first server
```
sudo cat /var/lib/rancher/k3s/server/node-token
```
then run the same command but add the token (replace SECRET with token from previous command)

```
curl -sfL https://get.k3s.io | sh -s - server --token=SECRET --node-taint CriticalAddonsOnly=true:NoExecute --tls-san load_balancer_ip_or_hostname
```
on agents / workers

to run without sudo
```
sudo chmod 644 /etc/rancher/k3s/k3s.yaml
```
get token 

```
sudo cat /var/lib/rancher/k3s/server/node-token
```
## k3s agents / workers
```
curl -sfL https://get.k3s.io | K3S_URL=https://load_balancer_ip_or_hostname:6443 K3S_TOKEN=mynodetoken sh -
```

change sample
