# Kubectl cheatsheet

## Running Applications
### Pods
In Kubernetes, a pod is the smallest deployable unit that represents a single instance of a running process in a cluster. A pod can contain one or more containers that share the same network namespace and can access the same storage volumes. Pods are created and managed by Kubernetes, and they are scheduled to run on one of the nodes in the cluster. Pods provide a lightweight and flexible abstraction layer that enables Kubernetes to manage the deployment, scaling, and networking of containerized applications. Pods also facilitate the communication and data exchange between containers running in the same pod.

### ReplicaSets
A ReplicaSet is a controller that ensures a specified number of replicas (identical copies) of a pod are running in a cluster at all times. ReplicaSets help to ensure high availability and scalability by automatically scaling the number of pod replicas up or down in response to changes in demand or hardware failures. They are defined by a YAML file that specifies the desired number of replicas, the pod template to use, and other settings. They are responsible for monitoring the status of pods and creating or deleting replicas as necessary to meet the desired state.

### Deployments
A Deployment is a resource object for managing Pods and ReplicaSets via a declarative configuration, which define a desired state that describes the application workload life cycle, number of pods, deployment strategies, container images, and more. The Deployment Controller works to ensure the actual state matches desired state, such as by replacing a failed pod. Out of the box, Deployments support several deployment strategies, like "recreate" and "rolling update", however can be customized to support more advanced deployment strategies such as blue/green or canary deployments.

### StatefulSets
It is a controller that manages the deployment and scaling of a set of stateful pods that require stable network identities and stable storage volumes. StatefulSets are used to run stateful applications such as databases, where the order and uniqueness of each pod is important. StatefulSets provide unique stable network identities and stable storage volumes for each pod, which allows stateful applications to maintain data consistency even when they are scaled up or down, or when nodes fail or are replaced. StatefulSets are defined by a YAML file that includes a pod template, a service to access the pods, and other settings.

### Jobs
a Job is a controller that manages the execution of a finite task or batch job. Jobs are used to run short-lived tasks, such as batch processing, data analysis, or backups, that run to completion and then terminate. Jobs create one or more pods to run the task, and they monitor the completion status of each pod. If a pod fails or terminates, the Job automatically creates a replacement pod to ensure that the task is completed successfully. Jobs are defined by a YAML file that includes a pod template, completion criteria, and other settings.

---
See node information
```
kubectl get nodes -o wide
```
See containers running 
```
kubectl get pods
```
See namespaces
```
kubectl get namespace
```
See services running
```
kubectl get service
```
See namespace and service information
```
kubectl -n <namespace> get svc 
```
Create configmap from file
```
kubectl create configmap nginx-conf --from-file=./nginx.conf
```

## How to delete namespace stuck in Terminating

```
kubectl get namespace ${NAMESPACE} -o json > tmp.json
```
then Remove "finalizers":[]

```
curl -k -H "Content-Type: application/json" -X PUT --data-binary @tmp.json 127.0.0.1:8001/api/v1/namespaces/$NAMESPACE/finalize
```