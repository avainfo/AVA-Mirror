# Javam Mirror

🚀 **A connected smart mirror with customizable widgets, real-time synchronization, and a modern interface.**

`J`ust<br>
`A`<br>
`V`irtual<br>
`A`ssistant for<br>
`M`e
## 📂 Project Structure
```
mirror-connecte/
│── mirror-software/  # Flutter app for the smart mirror
│── mobile-app/       # Flutter app for mobile (Android/iOS)
│── backend-api/      # Backend API in ASP.NET Core 9.0
│── infra/            # Infrastructure scripts (Docker, CI/CD, Firebase config…)
```

## 🛠 Technologies Used
- **Frontend:** Flutter (Mirror + Mobile)
- **Backend:** C# (ASP.NET Core 9.0)
- **Database:** Firebase
- **Communication Protocol:** WebSocket (SignalR)
- **Deployment:** Docker + CI/CD (GitHub Actions)

## 🚀 Installation & Running the Project
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your_repo.git
cd mirror-connecte
```
### 2️⃣ **Start the Services**
- **Backend:**
  ```sh
  cd backend-api
  docker-compose up --build
  ```
- **Mirror Software:**
  ```sh
  cd mirror-software
  flutter run
  ```
- **Mobile App:**
  ```sh
  cd mobile-app
  flutter run
  ```

## 🏗️ Contribution & Git Workflow
### Branches:
- `main` → Stable version.
- `dev` → Ongoing development.
- `feature/{name}` → One branch per feature.
- `fix/{name}` → One branch per bug fix.
- `hotfix/{name}` → Urgent fixes.

### Commit Convention:
- `feat(widget): Added widget resizing`
- `fix(sync): Fixed a sync bug`
- `refactor(api): Improved backend structure`

## 📄 Documentation
- **Backend API Documentation:** [Swagger](http://localhost:5000/swagger)
- **User Guide:** `/docs`
