# Steps on Installing High Availability Rancher using Helm with MetalLB

Install Helm on your personal computer


## Installing Ingress Nginx 
```yaml
helm repo add nginx-stable https://helm.nginx.com/stable
helm repo update
```

Get helm values and write it to yml file
```yaml
helm show values ingress-nginx/ingress-nginx > ingress-nginx.yml
```
Edit the yml file and change the following: 
```yaml
hostNetwork: true #set hostNetwork to true

hostPort:
    enabled: true #set hostPort to true

kind: DaemonSet #set kind to DaemonSet
```

Create namespace for ingress-nginx
```yaml
kubectl create namespace ingress-nginx
```

Perform the installation 
```yaml
helm install ${RELEASE NAME} ingress-nginx/ingress-nginx -n ingress-nginx --values ingress-nginx.yml --set controller.watchIngressWithoutClass=true
```

## Rancher Installation 
Add the Helm Chart Repository
```yaml
helm repo add rancher-stable https://releases.rancher.com/server-charts/stable
```

Create a Namespace for Rancher
```yaml
kubectl create namespace cattle-system
```
Install cert-manager
```yaml
# If you have installed the CRDs manually instead of with the `--set installCRDs=true` option added to your Helm install command, you should upgrade your CRD resources before upgrading the Helm chart:
kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.7.1/cert-manager.crds.yaml

# Add the Jetstack Helm repository
helm repo add jetstack https://charts.jetstack.io

# Update your local Helm chart repository cache
helm repo update

# Install the cert-manager Helm chart
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.7.1
```
For verification of Pods
```yaml
kubectl get pods --namespace cert-manager

NAME                                       READY   STATUS    RESTARTS   AGE
cert-manager-5c6866597-zw7kh               1/1     Running   0          2m
cert-manager-cainjector-577f6d9fd7-tr77l   1/1     Running   0          2m
cert-manager-webhook-787858fcdb-nlzsq      1/1     Running   0          2m
```

Install Rancher with Helm and Your Chosen Certificate Option

Set the hostname to the DNS name you pointed at your load balancer.
Set the bootstrapPassword to something unique for the admin user.
```yaml
helm install rancher rancher-stable/rancher \
  --namespace cattle-system \
  --set hostname=rancher.my.org \
  --set bootstrapPassword=admin
  ```