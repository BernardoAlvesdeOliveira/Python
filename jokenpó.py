# se divirta jogando com o coputador

import random as r

while True:
    print("")
    print("         VAMOS JOGAR JOKENPÓ")
    print("")
    lista = [1, 2, 3]
    print("[1] pedra - [2] papel - [3] tesoura")
    print("=-" * 18)

    while True:
        try:
            p = int(input('Escolha uma opção: '))
            if p in lista:
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    randomm = r.choice(lista)

    if randomm == p:
        print("EMPATE")
    elif randomm == 1 and p == 2:
        print("VOCÊ VENCEU!")
    elif randomm == 1 and p == 3:
        print("VOCÊ PERDEU")
    elif randomm == 2 and p == 3:
        print("VOCÊ VENCEU!")
    elif randomm == 2 and p == 1:
        print("VOCÊ PERDEU")
    elif randomm == 3 and p == 2:
        print("VOCÊ PERDEU")
    elif randomm == 3 and p == 1:
        print("VOCÊ VENCEU!")

    while True:
        play_again = input("Deseja jogar novamente? (s/n): ")
        if play_again.lower() == "s" or play_again.lower() == "n":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    if play_again.lower() != "s":
        break

print("Obrigado por jogar!")
