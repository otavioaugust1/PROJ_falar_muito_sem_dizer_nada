import os

def create_project_structure(project_name):
    folders = [
        "docs",
        "src/controler",
        "src/models",
        "src/views",
        "src/utils",
        "src/img",
        "src/app",
        "img",
        "tests"
    ]
    files = [
        "README.md",
        "requirements.txt",
        ".gitignore"
    ]

    for folder in folders:
        os.makedirs(os.path.join(project_name, folder), exist_ok=True)
    
    for file in files:
        open(os.path.join(project_name, file), 'w').close()
    
    print(f"Projeto {project_name} estruturado com sucesso!")

# Exemplo de uso
create_project_structure("meu_projeto_python")
