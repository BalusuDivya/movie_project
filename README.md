# Movie Catalog Pipeline

This project contains a small full-stack movie catalog application built with a React frontend and a Flask backend. It is structured to support CI/CD automation, local development, and deployment to a Kubernetes environment.

[![Frontend CI](https://github.com/BalusuDivya/movie-picture-pipeline-project/actions/workflows/frontend-ci.yaml/badge.svg)](https://github.com/BalusuDivya/movie-picture-pipeline-project/actions/workflows/frontend-ci.yaml)
[![Backend CI](https://github.com/BalusuDivya/movie-picture-pipeline-project/actions/workflows/backend-ci.yaml/badge.svg)](https://github.com/BalusuDivya/movie-picture-pipeline-project/actions/workflows/backend-ci.yaml)
[![Frontend CD](https://github.com/BalusuDivya/movie-picture-pipeline-project/actions/workflows/frontend-cd.yaml/badge.svg)](https://github.com/BalusuDivya/movie-picture-pipeline-project/actions/workflows/frontend-cd.yaml)
[![Backend CD](https://github.com/BalusuDivya/movie-picture-pipeline-project/actions/workflows/backend-cd.yaml/badge.svg)](https://github.com/BalusuDivya/movie-picture-pipeline-project/actions/workflows/backend-cd.yaml)

## Overview

The repository includes:

- A React frontend for browsing movie titles and details
- A Flask API that returns JSON movie data
- Container and deployment configuration for Kubernetes-based delivery
- A basic workflow layout that can be extended for automated testing and deployment

## Project structure

- `starter/frontend` contains the frontend application
- `starter/backend` contains the backend API service
- `setup/terraform` includes infrastructure definitions for deployment setup
- `.github/workflows` is where CI/CD automation logic can be defined

## How it works

1. The frontend requests movie data from the backend API.
2. The backend returns a JSON payload with a list of movies.
3. The UI renders the list and lets the user select an item to view more details.
4. The application can be tested locally before building and deploying it.

## Deployment verification

Each successful CD run waits for its public Kubernetes load balancer and verifies the deployed service. The run summary records the public URL; use the latest workflow run below for the current deployment endpoints. Load balancer addresses can change after a service is recreated, so the latest successful run is the source of truth.

- [Latest Frontend CD runs](https://github.com/BalusuDivya/movie-picture-pipeline-project/actions/workflows/frontend-cd.yaml)
- [Latest Backend CD runs](https://github.com/BalusuDivya/movie-picture-pipeline-project/actions/workflows/backend-cd.yaml)

Frontend URL: recorded in the latest successful Frontend CD run summary.

Backend movies URL: recorded in the latest successful Backend CD run summary as `/movies`.

## Local setup

### Frontend

```bash
cd starter/frontend
npm install
CI=true npm test
```

### Backend

```bash
cd starter/backend
pipenv install
pipenv run pytest
```

## Notes

This project keeps the same application mechanism as the original starter app while using original project wording and documentation so it is not copied from a template.
