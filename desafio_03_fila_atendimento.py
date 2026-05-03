import subprocess

subprocess.run("cls",shell=True) 

itens = ("Retirar senha","Chamar o próximo aluno","Mostrar fila","Sair")
fila = []

while True:
    print("SECRETARIA ACADÊMICA")
    for i, item in enumerate(itens,start=1):
        print(f"[{i}] - {item}")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            nome_aluno = input("Digite o nome do aluno: ").capitalize()
            fila.append(nome_aluno)
            print(f"{nome_aluno} entrou na fila de atendimento.\n")
    
        case "2":
            atendido = fila.pop(0)
            print(f"Chamando aluno: {atendido}\n")
        
        case "3":
            if fila:
                print(f"Fila atual:")
                for i, posicao in enumerate(fila,start=1):
                    print(f"{i}° - {posicao}")
            else:
                print("A fila está vazia.\n")

        case "4":
            break

        case _:
            print("Insira uma opção válida\n")