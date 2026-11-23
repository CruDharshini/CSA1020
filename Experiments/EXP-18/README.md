# Experiment 18 – Multi-Container App with Kubernetes

Build and push the backend image, replace the username in kubernetes.yaml, and change the placeholder database password before applying it.

```bash
docker build -t YOUR_DOCKERHUB_USERNAME/csa1020-backend:latest .
docker push YOUR_DOCKERHUB_USERNAME/csa1020-backend:latest
kubectl apply -f kubernetes.yaml
kubectl get deployments
kubectl get pods -w
kubectl get services
```

The manifest creates backend, Nginx frontend and MySQL workloads/services. This is a starter lab deployment: Nginx is not yet configured as a reverse proxy to the backend, and MySQL storage is ephemeral. Do not use the sample password in a real deployment.