import subprocess

subprocess.run("cls",shell=True) 

ana = 0
bruno = 0
carlos = 0

print("Candidatos:\n1. Ana\n2. Bruno\n3. Carlos")

while True:
    voto = input("Digite o nome do candidato (fim para encerrar): ").capitalize()
    if voto == "Ana":
        ana += 1
    elif voto == "Bruno":
        bruno += 1
    elif voto == "Carlos":
        carlos +=1
    elif voto == "Fim":
        break
    else:
        print("Voto inválido. Tente novamente")


subprocess.run("cls",shell=True) 
print("Resultado da votação:")
print(f"Ana: {ana} votos\nBruno {bruno} votos\nCarlos {carlos} votos")

if ana > bruno and carlos:
    print("O vencedor é: Ana.")
elif bruno > ana and carlos:
    print("O vencedor é: Bruno.")
elif carlos > ana and bruno:
    print("O vencedor é: Carlos.")
else:
    print("Houve um empate entre os candidatos.")