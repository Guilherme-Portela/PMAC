import os
import subprocess
import questionary
from questionary import Style
import json
import sys
from time import sleep

# ----- Style -----
styles = Style([
    ("highlighted", "fg:#FFFFFF bg:#0F4EDF bold")
])


# ----- Functions Utilitaries and Variables -----
def make_proj():
    lang_files = {
        "Python": "./Templates/python.json",
        "JavaScript": "./Templates/javascript.json",
        "C#": "./Templates/c-sharp.json",
        "TypeScript": "./Templates/typescript.json",
        "C++": "./Templates/cpp.json",
        "Java": "./Templates/java.json",
        "C": "./Templates/c.json",
        "Bash": "./Templates/bash.json"
    }

    _file = lang_files.get(lang_choice)
    with open(_file, 'r') as f:
        data = json.load(f)

    template = data.get(templates_choice)
    if proj_path.endswith("/"):
        proj_path = proj_path[:-1]
    for folder in template["folders"]:
        subprocess.run(["mkdir", f'{proj_path}'])
    for file in template["files"]:
        subprocess.run(["touch", f'{proj_path}/{file}'])
    with open(f'{file["docker-file"]}'):
        df = 

def show_summary(data: dict) -> None:
    """
    Mostra no terminal todos os dados do projeto de forma estilizada.
    """
    questionary.print("\n==== A seguir: O seu projeto ====", style="bold fg:cyan")
    for key, value in data.items():
        questionary.print(f"➡ {key}: {value}", style="fg:yellow")
        sleep(1)

def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")

all_data = {}

proj_name, proj_path, author = "", "", ""

templates = {
    "Python": [
        "console",       # app de terminal simples
        "cli",           # CLI com argparse/click/typer
        "flask",         # web app Flask
        "fastapi",       # web app FastAPI
        "data-science",  # Jupyter / Data Science
        "package"        # pacote Python para PyPI
    ],
    "Bash": [
        "script-basic",  # script simples
        "deploy",        # script de deploy
        "backup",        # script de backup
        "cli"            # CLI mínima com getopts
    ],
    "C#": [
        "console",       # console app
        "web-api",       # .NET Core Web API
        "library",       # library .NET Standard
        "wpf",           # GUI WPF / Windows Forms
        "unit-test"      # testes unitários
    ],
    "JavaScript": [
        "console",       # Node.js console app
        "express-api",   # Node.js + Express
        "react",         # React app
        "next",          # Next.js app
        "vite",          # Vite app
        "library"        # pacote Node/NPM
    ],
    "TypeScript": [
        "console",       # Node.js console app
        "express-api",   # Node.js + Express
        "react",         # React TS app
        "next",          # Next.js TS app
        "vite",          # Vite TS app
        "library"        # pacote TS/NPM
    ],
    "Java": [
        "console",       # console app
        "maven",         # Maven project
        "spring",        # Spring Boot API
        "library",       # library Java
        "unit-test"      # testes unitários
    ],
    "C": [
        "console",       # console app
        "makefile",      # projeto com Makefile
        "library",       # library C (static/dynamic)
        "competitive"    # template para programação competitiva
    ],
    "C++": [
        "console",       # console app
        "makefile",      # projeto com Makefile
        "library",       # library C++ (static/dynamic)
        "competitive",   # template para programação competitiva
        "sdl-sfml"       # projeto com SDL2 / SFML (jogos)
    ]
}

def banner():
   print("✨ PMAC - Project Management and Automatic Creation - 0.5 ✨\n") 

# ----- Main -----
clear()
banner()

while not proj_name:
    proj_name = questionary.text("Que nome desejas por á pasta de seu projeto?: ").ask()
    if not proj_name:
        questionary.print("❌ O nome não pode ser vazio. Por favor, tente novamente.", style="bold fg:red")
        sleep(3)
        clear()
        banner()


proj_desc = questionary.text("Descrição curta do projeto? (Opcional): ").ask()
if proj_desc == "":
    proj_desc = None
else:
    pass

while not proj_path:
    proj_path = questionary.path(
        "Escolha a pasta do projeto (Default: ~/Projects/):",
        default="~/Projects/",
        only_directories=True
    ).ask()

    if proj_path == "":
        questionary.print("❌ Por favor, informe um path para o seu projeto.", style="bold fg:red")

lang_choice = questionary.select(
    "Escolha a linguagem:",
    choices=["Python", "Bash", "C#", "JavaScript", "Java", "C", "C++", "TypeScript"],
    style=styles
).ask()

templates_choice = questionary.select(
    "Escolha um template:",
    choices=templates[lang_choice],
    style=styles
).ask()

git_choice = questionary.confirm(
    "Desejas usar versionamento com Git?: "
).ask()

readme_choice = questionary.confirm(
    "Desejas adicionar um README.md?: "
).ask()

if readme_choice == True:
    print("")
    print("Por favor, informe alguns dados para o seu README")

    while not author:
        author = questionary.text("Autor: ").ask()

        if not author:
            questionary.print("❌ O autor não pode ser vazio. Por favor, tente novamente.", style="bold fg:red")

    description = questionary.text("Descrição do seu projeto: ").ask()
    license_type = questionary.select(
        "Escolha a licença:",
        choices=["MIT", "GPL-3.0", "Apache-2.0", "BSD-3-Clause", "Sem Licença", "CC-0"],
        style=styles
    ).ask()
    print("")

else:
    pass

docker_choice = questionary.confirm(
    "Desejas adicionar um Dockerfile ao seu projeto?: "
).ask()

all_data = {
    "Nome do Projeto": proj_name,
    "Descrição do Projeto": proj_desc,
    "Caminho do Projeto": proj_path,
    "Linguagem": lang_choice,
    "Template": templates_choice,
    "Versionamento via Git": git_choice,
    "README": readme_choice,
    "Autor": author if readme_choice else None,
    "Licenciamento": license_type if readme_choice else None,
    "Dockerfile": docker_choice
}

clear()
banner()
show_summary(all_data)

continuar = questionary.confirm("Desejas continuar?").ask()

if continuar:
    questionary.print("✅ Beleza, vamos criar seu projeto!", style="bold fg:green")
else:
    questionary.print("❌ Cancelado pelo usuário.", style="bold fg:red")
    sys.exit(0)

make_proj()
