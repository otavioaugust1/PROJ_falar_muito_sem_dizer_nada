# Gerador de Frases Corporativas

Bem-vindo ao **Gerador de Frases Corporativas**! 🎉  
Este projeto é a solução definitiva para criar frases que soam incrivelmente importantes, mas que na verdade não dizem absolutamente nada. Ideal para reuniões, apresentações e qualquer situação em que você precise impressionar sem se comprometer.

---

## Descrição

Este projeto combina aleatoriamente frases de quatro colunas para gerar sentenças completas que são gramaticalmente corretas, mas sem nenhum conteúdo significativo. Perfeito para aqueles momentos em que você precisa falar muito sem dizer nada!

Agora, com uma interface web desenvolvida em **Flask**, você pode gerar frases de forma interativa, visualizar o histórico de frases geradas e até editar as colunas de frases disponíveis.

---

## Como Funciona

O sistema seleciona aleatoriamente uma frase de cada uma das quatro colunas e as combina para formar uma sentença completa. As frases são exibidas em uma interface web amigável, com opções para:

- Gerar novas frases.
- Visualizar o histórico de frases geradas.
- Editar as colunas de frases disponíveis.

![TABELA](img\TABELA.png)

---

## Como Usar

### Pré-requisitos

- Python 3.x instalado.
- Pip (gerenciador de pacotes do Python).

### Passos

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/otavioaugust1/PROJ_falar_muito_sem_dizer_nada.git
   cd PROJ_falar_muito_sem_dizer_nada

2. **Instale as dependências**:
   ```bash
    pip install -r requirements.txt 

3. **Execute a aplicação**:
   ```bash
    python scripts/run.py

4. **Acesse a aplicação**:

    Abra o navegador e acesse http://127.0.0.1:5000/.

## Funcionalidades
* **Gerar Frases**: Clique no botão para gerar uma nova frase aleatória.

* **Histórico**: Visualize todas as frases geradas durante a sessão.

* **Editar Colunas**: Adicione ou remova frases das colunas disponíveis.

## Estrutura do Projeto
```bash
    gerador-frases-corporativas/
    ├── README.md
    ├── requirements.txt
    ├── .gitgnore
    ├── docs/
    ├── img/
    │       └── tabela.png
    ├── src/
    │   └── gerador_frases/
    │       ├── app.py
    │       ├── templates/
    │       │       ├── adicionar_item.html
    │       │       ├── editar_colunas.html
    │       │       └── index.html
    │       └── utils/
    │               └──gerador.py
    ├── scripts/
    │   └── run.py
    ├── tests
    │   └── gerador_frases.py
    └── LICENSE
```

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para:

* Abrir issues para reportar bugs ou sugerir melhorias.

* Enviar pull requests para adicionar novas funcionalidades ou corrigir problemas.

## Autor
* 👤 Otávio Augusto
* GitHub: @otavioaugust1
* Projeto: Gerador de Frases Corporativas

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.