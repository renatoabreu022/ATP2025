**Resolução do TPC 2 proposto no dia 22/09/2025**

![foto%20uni_resized](https://github.com/user-attachments/assets/8d5bd67c-d7d0-468e-9623-002e6451df77)

*Renato André Matos Abreu (a112333)*

Foi proposto escrever um programa em python que simulava o 'Jogo dos fósforos'. Neste jogo há, de início, 21 fósforos e cada jogador deve escolher tirar à vez entre 1 e 4 fósforos, o jogador que tiver que retirar o último fósforo perde. O TPC consisitia em recriar este jogo, jogando contra o computador, sendo o jogo dividido em 2 níveis:

**Nível 1:** Sendo o computador a jogar em primeiro lugar, este ganha sempre;

**Nível 2:** Sendo nós a jogar em segundo lugar, o computador só ganha caso haja algum erro de cálculo da nossa parte.

Nesta resolução, juntei os dois níveis num programa só e dei a opção de voltar a jogar ou terminar o jogo:

 ```python
import random

def fosforo():
  print("Vamos jogar o jogo dos fósforos!")
  total = 21
  jog = input("Queres jogar primeiro? ")

  while jog != "Sim" and jog != "Não" and jog != "sim" and jog != "não":
    print("Resposta Inválida")
    jog = input("Queres jogar primeiro? ")

  print("Começamos com 21 fósforos")
  if jog == "Sim" or jog == "sim":
    while total > 1:
      n = int(input("Escolhe quantos fósforos queres retirar (entre 1 e 4): "))
      if 1 <= n <= 4:
        total = total - n
        print(f"Agora temos {total} fósforo(s)!")
        n = 5 - n
        total = total - n
        print(f"Eu escolho retirar {n}")
        print(f"Agora temos {total} fósforo(s)!")
        if total == 1:
          print("Eu ganhei!")
          break
      elif n < 1 or n > 4:
        print("Tem que ser um número entre 1 e 4!")

  if jog == "Não" or jog == "não":
    n = random.randint(1,4)
    print(f"Eu escolho retirar {n} fósforo(s)!")
    total = total - n
    print(f"Agora temos {total} fósforo(s)!")
    while total > 1:
      n = int(input("Escolhe quantos fósforos queres retirar (entre 1 e 4): "))
      if 1 <= n <= 4:
        total = total - n
        print(f"Agora temos {total} fósforo(s)!")
        if total == 1:
          print("Ganhaste!")
          break
        n = random.randint(1,4)
        print(f"Eu escolho retirar {n}")
        total = total - n
      elif n < 1 or n > 4:
        print("Tem que ser um número entre 1 e 4!")
      elif total == 1:
        print(f"Agora temos {total} fósforo(s)!")
        print("Eu ganhei!")
        break

fosforo()
escolha = input("Quer jogar de novo? ")  
while escolha == "Sim" or escolha == "sim":
  fosforo()
  escolha = input("Quer jogar de novo? ")
while escolha != "Sim" and escolha != "sim" and escolha != "Não" and escolha != "não":
  print("Inválido")
  escolha = input("Quer jogar de novo? ")
```
