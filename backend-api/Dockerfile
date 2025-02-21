# Étape 1 : Build avec le SDK .NET
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /app

# Copier et restaurer les dépendances
COPY *.csproj ./
RUN dotnet restore

# Copier le reste des fichiers et compiler
COPY . ./
RUN dotnet publish -c Release -o /out

# Étape 2 : Exécuter les tests avec le SDK
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS test
WORKDIR /app
COPY --from=build /out ./
CMD ["dotnet", "test", "--verbosity", "normal"]

# Étape 3 : Exécuter l’application avec l'image runtime plus légère
FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS runtime
WORKDIR /app

# Copier l'application compilée depuis l'étape build
COPY --from=build /out ./

EXPOSE 8080

CMD ["dotnet", "backend-api.dll"]
