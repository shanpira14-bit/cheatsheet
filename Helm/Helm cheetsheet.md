# Helm cheatsheet

Get helm values and write it to yml file
```
helm show values ingress-nginx/ingress-nginx > ingress-nginx.yml
```

Install Helm applicationg using the value inside the yml file.
```
helm install myingress ingress-nginx/ingress-nginx -n ingress-nginx --values ingress-nginx.yaml --set controller.watchIngressWithoutClass=true 
```
