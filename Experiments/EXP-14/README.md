# Experiment 14 – Continuous Deployment with GitHub Actions

The workflow in `.github/workflows/exp14-docker.yml` builds the Docker image whenever files for this experiment change on the working branch. It does not push to Docker Hub because that requires your own repository secrets. Check the Actions tab for the build result.