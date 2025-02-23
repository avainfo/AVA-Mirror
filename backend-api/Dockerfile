FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /app

COPY *.csproj ./
RUN dotnet restore

COPY . ./
RUN dotnet publish -c Release -o /out

FROM mcr.microsoft.com/dotnet/sdk:9.0 AS test
WORKDIR /app
COPY --from=build /out ./
CMD ["dotnet", "test", "--verbosity", "normal"]

FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS runtime
WORKDIR /app

COPY --from=build /out ./

ENV ASPNETCORE_URLS=http://+:8080

EXPOSE 8080

CMD ["dotnet", "backend-api.dll"]
