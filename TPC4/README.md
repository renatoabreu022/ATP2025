**Resolução do TPC 4 proposto no dia 09/10/2025**

![foto%20uni_resized](https://github.com/user-attachments/assets/8d5bd67c-d7d0-468e-9623-002e6451df77)

*Renato André Matos Abreu (a112333)*

Foi pedido que se construísse um programa em Python que simulasse a gestão das salas de um cinema com um conjunto específico de funções e um menu para acesssar as diversas funções e executá-las.

**Conjunto de funções**

```python
def listar(cinema):
    i = 0
    while i < len(cinema):
        print(cinema[i])
        i += 1

def disponivel(cinema,filme,lugar):
    i = 0
    while i < len(cinema):
        if filme == cinema[i][2]:
            if lugar in cinema[i][1]:
                return False
        i += 1
    return True

def vendebilhete(cinema,filme,lugar):
    i = 0
    while i < len(cinema):
        if filme == cinema[i][2]:
            if lugar in cinema[i][1]:
                return "Esse lugar já está ocupado"
            else:
                cinema[i][1].append(lugar)
                print(f"O lugar {lugar} para o filme {filme} foi vendido com sucesso")
        i += 1
    return listar(cinema)

def listardisponibilidades(cinema):
    i = 0
    while i < len(cinema):
        print(f"Existem {cinema[i][0] - len(cinema[i][1])} lugares disponíveis para o filme {cinema[i][2]}")
        i += 1

def inserirSala(cinema,sala):
    i = 0
    while i < len(cinema):
        if sala[2] == cinema[i][2]:
            return "Esse filme já vai ser exibido noutra sala"
        i += 1
    cinema.append(sala)
    print("Sala adicionada com sucesso")
    listar(cinema)

def reset(cinema):
    cinema.clear()
    return "Todas as salas foram removidas"
```

**Utilização das funções num menu**

```python
cin = []
b = True
while b == True:
  m = int(input('''MENU
  (1) Criar uma Sala
  (2) Disponibilidade das Salas
  (3) Disponibilidade de um Lugar
  (4) Vender um Bilhete
  (5) Listar Salas de Cinema
  (6) Reset
  (0) Sair          
            
  Opção: '''))
  if m == 1:
    lug = int(input("Quantos lugares terá a sala? "))
    filme = input("Qual será o filme exibido? ")
    inserirSala(cin,[lug,[],filme])
  elif m == 2:
    listardisponibilidades(cin)
  elif m == 3:
    filme = input("Qual filme quer acessar? ")
    lug = int(input("Qual lugar quer verificar? "))
    if disponivel(cin,filme,lug):
      print("O lugar está livre")
    elif not disponivel(cin,filme,lug):
      print("O lugar está ocupado")
  elif m == 4:
    filme = input("Qual filme quer assistir? ")
    lug = int(input("Qual lugar quer reservar? "))
    vendebilhete(cin,filme,lug)
  elif m == 5:
    listar(cin)
  elif m == 6:
    reset(cin)
  elif m == 0:
    b = False
```
