# Infrastructure - AVA Mirror

🛠 Scripts for **Docker**, **CI/CD**, and **Firebase**.

## 📂 Project Structure
```
infra/
│── docker/
│   ├── backend.Dockerfile   # Backend Docker image
│── ci-cd/
│   ├── github-actions.yml   # GitHub Actions pipeline
│── firebase/
│   ├── firebase-config.json # Firebase configuration
│── README.md                # Documentation
```

## 🚀 Deployment
### 1️⃣ **Run Backend in Docker**
```sh
cd backend-api
docker-compose up --build
```

### 2️⃣ **CI/CD with GitHub Actions**
- Push to `dev` → Runs automatic tests.
- Merge to `main` → Triggers auto-deployment.
