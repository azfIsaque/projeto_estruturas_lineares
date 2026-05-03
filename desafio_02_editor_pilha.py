import subprocess

subprocess.run("cls",shell=True) 

itens = ("Digitar palavra","Desfazer a última palavra","Mostrar texto","Sair")
pilha = []

while True:
    print("EDITOR DE TEXTO")
    for i, item in enumerate(itens,start=1):
        print(f"[{i}] - {item}")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            palavra = input("Digite uma palvra: ")
            pilha.append(palavra)
            print(f"Palavra adicionada: {palavra}\n")
        
        case "2":
            palavra_removida = pilha.pop()
            print(f"Palavra removiida: {palavra_removida}\n")

        case "3":
            print(f"Texto atual: {' '.join(pilha)}\n")

        case "4":
            break

        case _:
            print("Insira uma opção válida\n")