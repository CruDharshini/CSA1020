# Experiment 19 – CI/CD with GitHub Actions

The workflow `.github/workflows/exp19-ci.yml` runs the Flask test and builds the Docker image on pushes and pull requests that touch this experiment. It does not deploy to AWS or publish an image. Add your own protected secrets and deployment environment only if your instructor requires cloud deployment.