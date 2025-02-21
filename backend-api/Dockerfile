FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /app

# Copier le fichier .csproj et restaurer les dépendances
COPY *.csproj ./
RUN dotnet restore

# Copier le reste des fichiers et compiler
COPY . ./
RUN dotnet publish -c Release -o /out

FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS runtime
WORKDIR /app

# Copier les fichiers compilés de l'étape précédente
COPY --from=build /out .

EXPOSE 8080

CMD ["dotnet", "backend-api.dll"]
