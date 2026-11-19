# Experiment 16 – Containerize Flask To-Do App

```bash
docker build -t csa1020-flask-todo .
docker run --rm -d --name csa1020-flask-todo -p 5000:5000 csa1020-flask-todo
```

Open http://localhost:5000. Tasks are held in memory and reset when the container restarts.
