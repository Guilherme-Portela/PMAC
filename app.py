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

# ----- Utilities -----
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_summary(data: dict):
    questionary.print("\n==== A seguir: O seu projeto ====", style="bold fg:cyan")
    for key, value in data.items():
        questionary.print(f"➡ {key}: {value}", style="fg:yellow")
        sleep(0.5)

# ----- Licenses -----
temp_license = {
    "MIT": {
        "nome": "MIT License",
        "tipo": "Permissiva",
        "conteudo": "Permite uso, cópia, modificação, mesclagem, publicação, distribuição, sublicenciamento e venda. Exige manutenção do aviso de direitos autorais."
    },
    "GPL-3.0": {
        "nome": "GNU General Public License v3.0",
        "tipo": "Copyleft Forte",
        "conteudo": "Garante liberdade de usar, estudar, redistribuir e melhorar. Obras derivadas devem ser sob a mesma licença."
    },
    "Apache-2.0": {
        "nome": "Apache License 2.0",
        "tipo": "Permissiva",
        "conteudo": "Permite uso, modificação e distribuição. Concede licença de patente. Exige aviso de direitos autorais e NOTICE."
    },
    "BSD-3-Clause": {
        "nome": "BSD 3-Clause",
        "tipo": "Permissiva",
        "conteudo": "Permite uso, cópia, modificação e redistribuição. Exige manutenção do aviso de direitos autorais."
    },
    "CC-0": {
        "nome": "Creative Commons Zero v1.0 Universal",
        "tipo": "Domínio Público",
        "conteudo": "O autor renuncia a todos os direitos. Pode ser usado para qualquer finalidade sem atribuição."
    }
}

# ----- Templates -----
templates = {
    "Python": ["console","cli","flask","fastapi","data-science","package"],
    "Bash": ["script-basic","deploy","backup","cli"],
    "C#": ["console","web-api","library","wpf","unit-test"],
    "JavaScript": ["console","express-api","react","next","vite","library"],
    "TypeScript": ["console","express-api","react","next","vite","library"],
    "Java": ["console","maven","spring","library","unit-test"],
    "C": ["console","makefile","library","competitive"],
    "C++": ["console","makefile","library","competitive","sdl-sfml"]
}

# ----- Banner -----
def banner():
    print("✨ PMAC - Project Management and Automatic Creation - 0.5 ✨\n")

# ----- Core Function -----
def make_proj(lang_choice, templates_choice, proj_path, proj_name, author, docker_choice, readme_choice, license_type, git_choice, proj_desc):
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

    # Carregar template da linguagem
    _file = lang_files.get(lang_choice)
    with open(_file, 'r') as f:
        data = json.load(f)

    template = data.get(templates_choice)
    if not template:
        questionary.print(f"❌ Template '{templates_choice}' não encontrado!", style="bold fg:red")
        return

    proj_path = os.path.normpath(proj_path)  # normaliza path para Windows/Linux
    os.makedirs(proj_path, exist_ok=True)

    # Criar pastas
    for folder in template.get("folders", []):
        os.makedirs(os.path.join(proj_path, folder), exist_ok=True)

    # Criar arquivos
    for file in template.get("files", []):
        open(os.path.join(proj_path, file), "a").close()

    # Dockerfile
    if docker_choice:
        docker_template_path = template.get("docker-file")
        if docker_template_path and os.path.exists(docker_template_path):
            with open(docker_template_path, 'r') as docker_file:
                with open(os.path.join(proj_path, "Dockerfile"), 'w') as newdf:
                    newdf.writelines(docker_file.readlines())

    # README e Licença
    if readme_choice:
        with open(os.path.join(proj_path, "README.md"), 'w') as readme:
            readme.write(f"# {proj_name}\n")
            readme.write(f"### By: {author}\n")
            if proj_desc:
                readme.write(f"{proj_desc}\n")

        if license_type != "Sem Licença":
            license_info = temp_license.get(license_type)
            if license_info:
                with open(os.path.join(proj_path, "license.txt"), 'w') as lic:
                    lic.write(f"License type: {license_info['tipo']}\n")
                    lic.write(license_info["conteudo"])

    # Git init silencioso
    if git_choice:
        subprocess.run(
            ["git", "init"],
            cwd=proj_path,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

# ----- Main Program -----
clear()
banner()

proj_name = questionary.text("Nome da pasta do projeto:").ask()
while not proj_name:
    questionary.print("❌ O nome não pode ser vazio.", style="bold fg:red")
    proj_name = questionary.text("Nome da pasta do projeto:").ask()

proj_desc = questionary.text("Descrição curta do projeto (opcional):").ask() or None

proj_path = questionary.path("Escolha a pasta do projeto (Default: ~/Projects/):", default="~/Projects/", only_directories=True).ask()
while not proj_path:
    questionary.print("❌ Informe um path válido.", style="bold fg:red")
    proj_path = questionary.path("Escolha a pasta do projeto (Default: ~/Projects/):", default="~/Projects/", only_directories=True).ask()

lang_choice = questionary.select("Escolha a linguagem:", choices=list(templates.keys()), style=styles).ask()
templates_choice = questionary.select("Escolha um template:", choices=templates[lang_choice], style=styles).ask()

git_choice = questionary.confirm("Desejas usar versionamento com Git?:").ask()
readme_choice = questionary.confirm("Desejas adicionar README.md?:").ask()
docker_choice = questionary.confirm("Desejas adicionar Dockerfile?:").ask()

author, license_type = None, None
if readme_choice:
    author = questionary.text("Autor:").ask()
    while not author:
        questionary.print("❌ Autor não pode ser vazio.", style="bold fg:red")
        author = questionary.text("Autor:").ask()

    license_type = questionary.select(
        "Escolha a licença:",
        choices=["MIT", "GPL-3.0", "Apache-2.0", "BSD-3-Clause", "Sem Licença", "CC-0"],
        style=styles
    ).ask()

all_data = {
    "Nome do Projeto": proj_name,
    "Descrição do Projeto": proj_desc,
    "Caminho do Projeto": proj_path,
    "Linguagem": lang_choice,
    "Template": templates_choice,
    "Versionamento via Git": git_choice,
    "README": readme_choice,
    "Autor": author,
    "Licenciamento": license_type,
    "Dockerfile": docker_choice
}

clear()
banner()
show_summary(all_data)

if questionary.confirm("Desejas continuar?").ask():
    questionary.print("✅ Criando projeto...", style="bold fg:green")
    make_proj(lang_choice, templates_choice, proj_path, proj_name, author, docker_choice, readme_choice, license_type, git_choice, proj_desc)
    questionary.print("🎉 Projeto criado com sucesso!", style="bold fg:green")
else:
    questionary.print("❌ Cancelado pelo usuário.", style="bold fg:red")
    sys.exit(0)
