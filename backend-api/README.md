# Backend API - AVA Mirror

⚡ **ASP.NET Core 9.0 API** for managing widgets, users, and real-time communication.

## 📂 Project Structure
```
backend-api/
│── src/
│   ├── Controllers/        # API Controllers (REST/WebSocket)
│   ├── Models/             # Data models
│   ├── Services/           # Business logic
│   ├── Repositories/       # Data access
│   ├── Hubs/               # WebSocket (SignalR)
│   ├── Config/             # Configuration (Firebase, JWT…)
│   ├── Program.cs          # Main entry point
│── tests/                  # Unit and integration tests
│── Dockerfile              # Backend containerization
│── .github/workflows/      # CI/CD (GitHub Actions)
│── swagger.json            # API Documentation (OpenAPI)
```

## 🚀 Installation
### 1️⃣ **Prerequisites**
- .NET 9.0
- Docker (optional)

### 2️⃣ **Run the Backend**
```sh
cd backend-api
dotnet run
```

### 3️⃣ **Test the API**
- Swagger: [http://localhost:5000/swagger](http://localhost:5000/swagger)

## 🏗️ Contribution
- WebSocket using **SignalR**
- Authentication with **JWT**
- Data storage in **Firebase**
