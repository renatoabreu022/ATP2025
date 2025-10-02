**Resolução do TPC 2 proposto no dia 22/09/2025**

![foto%20uni_resized](https://github.com/user-attachments/assets/8d5bd67c-d7d0-468e-9623-002e6451df77)

*Renato André Matos Abreu (a112333)*

Foi pedido que se criasse um programa em Python com um menu inicial que continha várias opções de operações a realizar numa lista e, ainda, a de sair do programa. O utilizador pode selecionar qualquer uma das operações selecionando o número que lhe está atribuído. Sempre que uma operação termina, é dada a opção de selecionar outra operação do menu.

 ```python
import random
c = True
l = []

while c == True:
    escolha = int(input('''Escolha entre as opções seguintes:
    (1) Criar Lista
    (2) Ler Lista
    (3) Soma
    (4) Média
    (5) Maior
    (6) Menor
    (7) Está ordenada por ordem crescente?
    (8) Está ordenada por ordem decrescente?
    (9) Procurar um elemento
    (0) Sair
    '''))

    if escolha == 1:
        l = []
        tamanho = int(input("Escolha o tamanho da sua lista: "))
        for i in range(tamanho):
            l.append(random.randint(1,100))
        print (f'''A sua lista é a seguinte:
        {l}''')
    elif escolha == 2:
        l = []
        tamanho = int(input("Escolha o tamanho da sua lista: "))
        for i in range(tamanho):
            elem = int(input("Escolha que número quer colocar: "))
            l.append(elem)
        print (f'''A sua lista é a seguinte:
        {l}''')
    elif escolha == 3:
        s = 0
        for i in l:
            s = s + i
        print(f"A soma dos elementos da sua lista é {s}")
    elif escolha == 4:
        a = 0
        for i in l:
            a = a + i
        print(f"A média dos elementos da sua lista é {a/len(l)}")
    elif escolha == 5:
        maior = l[0]
        for i in l:
            if i > maior:
                maior = i
        print(f"O maior valor da sua lista é {maior}")
    elif escolha == 6:
        menor = l[0]
        for i in l:
            if i < menor:
                menor = i
        print(f"O menor valor da sua lista é {menor}")
    elif escolha == 7:
        ordem = True
        for i in range(1,len(l)):
            if l[i] < l[i-1]:
                ordem = False
        if ordem == True:
            print("A sua lista está por ordem crescente")
        else:
            print("A sua lista não está por ordem crescente")
    elif escolha == 8:
        ordem = True
        for i in range(1,len(l)):
            if l[i] > l[i-1]:
                ordem = False
        if ordem == True:
            print("A sua lista está por ordem decrescente")
        else:
            print("A sua lista não está por ordem decrescente")
    elif escolha == 9:
        elem = int(input("Que elemento da sua lista quer saber a posição? "))
        if elem in l:
            for i in l:
                if i == elem:
                    print(f"Posição {l.index(elem)}")
        else:
            print("Posição -1")
    elif escolha == 0:
        print(f'''A sua lista é a seguinte:
        {l}''')
        c = False
```
