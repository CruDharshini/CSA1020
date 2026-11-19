# Experiment 11 – Static Website with Docker

Build and run locally:

```bash
docker build -t csa1020-static-site .
docker run --rm -d --name csa1020-static-site -p 8080:80 csa1020-static-site
```

Open http://localhost:8080. Verify with `docker ps`; stop with `docker stop csa1020-static-site`.
