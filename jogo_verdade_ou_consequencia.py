import random

print("Quantas pessoas irão jogar ? ")
pessoas = input()
print("Quantas rodadas ? ")
rodadas = input()

for x in range(int(rodadas)):
    valor = random.randint(1,int(pessoas))
    print("Pessoa número : " + str(valor))

    print("\n Verdade ou Consequencia ? ")
    print("\n Verdade é 1 Consequencia é 2 ")
    x = input()

    if(int(x) == 1):
        print('Verdade: Python é difícil')
    else:
        print('Consequencia: Plantar bananeira!')

print('Fim do jogo')