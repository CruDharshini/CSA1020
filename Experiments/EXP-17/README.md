# Experiment 17 – Push & Pull Docker Image

Build, tag, push, pull and run the image:

```bash
docker build -t YOUR_DOCKERHUB_USERNAME/csa1020-html-site:latest .
docker login
docker push YOUR_DOCKERHUB_USERNAME/csa1020-html-site:latest
docker pull YOUR_DOCKERHUB_USERNAME/csa1020-html-site:latest
docker run --rm -d -p 8080:80 YOUR_DOCKERHUB_USERNAME/csa1020-html-site:latest
```

Open http://localhost:8080. Never commit registry credentials.