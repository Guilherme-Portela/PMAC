import os

templates = {
    "Python": [
        "console", "cli", "flask", "fastapi", "data-science", "package"
    ],
    "Bash": [
        "script-basic", "deploy", "backup", "cli"
    ],
    "C#": [
        "console", "web-api", "library", "wpf", "unit-test"
    ],
    "JavaScript": [
        "console", "express-api", "react", "next", "vite", "library"
    ],
    "TypeScript": [
        "console", "express-api", "react", "next", "vite", "library"
    ],
    "Java": [
        "console", "maven", "spring", "library", "unit-test"
    ],
    "C": [
        "console", "makefile", "library", "competitive"
    ],
    "C++": [
        "console", "makefile", "library", "competitive", "sdl-sfml"
    ]
}

# Pasta onde salvar os dockerfiles
output_dir = "./Templates/docker-files"
os.makedirs(output_dir, exist_ok=True)

# Modelos básicos para cada linguagem
docker_templates = {
    "Python": """FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python3", "main.py"]
""",
    "Bash": """FROM debian:stable-slim
WORKDIR /scripts
COPY . .
CMD ["bash", "script.sh"]
""",
    "C#": """FROM mcr.microsoft.com/dotnet/sdk:8.0
WORKDIR /src
COPY . .
RUN dotnet build
CMD ["dotnet", "run"]
""",
    "JavaScript": """FROM node:20-slim
WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "start"]
""",
    "TypeScript": """FROM node:20-slim
WORKDIR /app
COPY . .
RUN npm install && npm run build
CMD ["npm", "start"]
""",
    "Java": """FROM openjdk:21-slim
WORKDIR /app
COPY . .
CMD ["java", "Main"]
""",
    "C": """FROM gcc:13
WORKDIR /src
COPY . .
RUN gcc -o main main.c
CMD ["./main"]
""",
    "C++": """FROM gcc:13
WORKDIR /src
COPY . .
RUN g++ -o main main.cpp
CMD ["./main"]
"""
}

# Criar um dockerfile para cada linguagem + template
for lang, tmpl_list in templates.items():
    for tmpl in tmpl_list:
        filename = f"{lang.lower()}-{tmpl}.dockerfile"
        filepath = os.path.join(output_dir, filename)

        base = docker_templates.get(lang, "FROM scratch\n")
        content = f"# Dockerfile para {lang} - {tmpl}\n{base}"

        with open(filepath, "w") as f:
            f.write(content)

print(f"✅ Dockerfiles gerados em {output_dir}")
