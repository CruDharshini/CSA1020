# Experiment 12 – Flask API with Docker & Kubernetes

Replace the image placeholder in deployment.yaml with your published Docker Hub image.

```bash
docker build -t YOUR_DOCKERHUB_USERNAME/csa1020-flask-api:latest .
docker push YOUR_DOCKERHUB_USERNAME/csa1020-flask-api:latest
kubectl apply -f deployment.yaml
kubectl get pods
kubectl get services
```

Test / and /about at http://localhost:30007. A running Kubernetes cluster and Docker Hub login are required; deployment is not verified by this repository commit.
