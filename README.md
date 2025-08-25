# PMAC - Project Management and Automatic Creation

✨ **Versão atual: 0.2.2** ✨  

PMAC é uma ferramenta automatizada para criação de projetos de software. Ele gera a estrutura inicial do projeto, arquivos README, versionamento Git, Dockerfiles e templates específicos para diversas linguagens, agilizando a configuração de novos projetos e mantendo boas práticas desde o início.

---

## Descrição Detalhada

O PMAC foi criado para desenvolvedores que querem iniciar projetos rapidamente, sem perder tempo configurando pastas, arquivos essenciais e templates. Ele suporta múltiplas linguagens e frameworks, como:

- **Python**: console, CLI, Flask, FastAPI, Data Science (Jupyter), pacotes PyPI  
- **Bash**: scripts básicos, deploy, backup, CLI mínima  
- **C#**: console, web API, library, WPF/Windows Forms, testes unitários  
- **JavaScript / TypeScript**: console, Node.js + Express, React, Next.js, Vite, libraries  
- **Java**: console, Maven, Spring Boot API, library, unit-tests  
- **C / C++**: console, Makefile, library, programação competitiva, SDL/SFML

O PMAC permite criar rapidamente um projeto com:

1. Estrutura de pastas e arquivos adequados ao template escolhido.
2. README.md inicial, com informações do projeto, autor e licença.
3. Dockerfile opcional para containerização.
4. Versionamento via Git integrado.

---

## Explicação de Cada Pergunta do Formulário

1. **Nome do projeto**  
   Define a pasta raiz do projeto. Não pode ficar vazia.  

2. **Descrição curta do projeto**  
   Um resumo opcional do propósito do projeto.  

3. **Caminho do projeto**  
   Local onde o projeto será criado. Por padrão: `~/Projects/`.  

4. **Escolha da linguagem**  
   Define o ecossistema do projeto (Python, C#, Java, etc.)  

5. **Escolha do template**  
   Define a estrutura interna (console, web, CLI, library, etc.)  

6. **Versionamento com Git**  
   Cria automaticamente o repositório Git inicial, pronto para commits.  

7. **Adicionar README.md**  
   Gera um README inicial, com autor, descrição e licença escolhida.  

8. **Autor e Licença**  
   Permite creditar o criador e definir regras de uso e distribuição.  

9. **Adicionar Dockerfile**  
   Cria um arquivo Docker inicial, pronto para containerizar o projeto.

---

## Comandos Disponíveis

Após criar o projeto, você pode utilizar comandos comuns para cada linguagem. Alguns exemplos:

- **Python**  
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar projeto
python app.py
```

### Timeline de updates
```v1.0.0```: *"Criação automatica dos projetos"*
```v2.0.0```: *"Criação automatica + gerenciamento dos projetos"*
