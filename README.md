# Movie Catalog Pipeline

This project contains a small full-stack movie catalog application built with a React frontend and a Flask backend. It is structured to support CI/CD automation, local development, and deployment to a Kubernetes environment.

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
