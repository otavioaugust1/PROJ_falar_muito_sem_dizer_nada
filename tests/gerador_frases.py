import random

# Tabela de frases
coluna1 = [
    "Caros colegas,", "Por outro lado,", "Não podemos esquecer que", "Do mesmo modo,", 
    "A prática mostra que", "Nunca é demais insistir que", "A experiência mostra que", 
    "É fundamental ressaltar que", "O incentivo ao avanço tecnológico, assim como", 
    "Assim mesmo,", "Além disso,", "Em contrapartida,", "Por fim,", "Adicionalmente,", 
    "Em suma,", "Finalmente,"
]

coluna2 = [
    "a execução deste projeto", "a complexidade dos estudos efetuados", "a atual estrutura de organização", 
    "o novo modelo estrutural aqui preconizado", "o desenvolvimento de formas distintas de atuação", 
    "a constante divulgação das informações", "a consolidação das estruturas", 
    "a análise dos diversos resultados", "o início do programa de formação de atitudes", 
    "a expansão de nossa atividade", "a implementação de novas estratégias", 
    "a revisão dos procedimentos atuais", "a integração de tecnologias avançadas", 
    "a capacitação contínua dos colaboradores", "a colaboração entre departamentos", 
    "a avaliação periódica dos processos"
]

coluna3 = [
    "nos obriga à análise", "cumpre um papel essencial na formulação", "auxilia a preparação e a estruturação", 
    "contribui para a correta determinação", "assume importantes posições na definição", 
    "facilita a definição", "prejudica a percepção da importância", "oferece uma boa oportunidade de verificação", 
    "acarreta um processo de reformulação", "exige precisão e definição", "requer uma avaliação cuidadosa", 
    "pode resultar em melhorias significativas", "deve ser considerada", "é essencial para o crescimento", 
    "fortalece a coesão", "garante a melhoria contínua"
]

coluna4 = [
    "das nossas opções de desenvolvimento futuro.", "das nossas metas financeiras e administrativas.", 
    "das atitudes e das atribuições da diretoria.", "das novas proposições.", 
    "das opções básicas para o sucesso do programa.", "do nosso sistema de formação de quadros.", 
    "das condições apropriadas para os negócios.", "dos índices pretendidos.", 
    "das formas de ação.", "dos conceitos de participação geral.", "dos recursos disponíveis.", 
    "na eficiência operacional.", "para manter a competitividade no mercado.", 
    "sustentável da organização.", "e a eficiência das operações.", "e a adaptação às mudanças do mercado."
]

def gerar_frase():
    frase = f"{random.choice(coluna1)} {random.choice(coluna2)} {random.choice(coluna3)} {random.choice(coluna4)}"
    return frase

def main():
    while True:
        print(gerar_frase())
        resposta = input("Deseja gerar outra frase? (SIM/NÃO): ").strip().upper()
        if resposta == "NÃO":
            print("Obrigado! Até a próxima.")
            break

if __name__ == "__main__":
    main()
