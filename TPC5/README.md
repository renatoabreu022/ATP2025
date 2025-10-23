**Resolução do TPC 5 proposto no dia 16/10/2025**

![foto%20uni_resized](https://github.com/user-attachments/assets/8d5bd67c-d7d0-468e-9623-002e6451df77)

*Renato André Matos Abreu (a112333)*

Foi pedido que se criasse uma aplicação para gerir turmas através de um menu de operações, sendo possível criar turmas, adicionar alunos, listar a turma, consultar alunos através do seu id, guardar cada turma no ficheiro, carregar a turma do ficheiro e sair da aplicação.

```python
def criarTurma():
    print("Turma criada")
    return []

def inserirAluno(turma):
    nome = input("Insira o nome do aluno: ")
    existe = True
    while existe == True:
        existe = False
        id = int(input("Insira o ID do aluno: "))
        for a in turma:
            if a[1] == id:
                print("Esse ID já está a ser utilizado")
                existe = True
    tpc = int(input("Insira a nota do TPC do aluno: "))
    proj = int(input("Insira a nota do projeto do aluno: "))
    teste = int(input("Insira a nota do teste do aluno: "))
    aluno = (nome, id, [tpc, proj, teste])
    turma.append(aluno)
    print("O aluno foi adicionado com sucesso")

def listarTurma(turma):
    for a in turma:
        print(f"Nome: {a[0]}, ID: {a[1]}, Nota do TPC: {a[2][0]}, Nota do Projeto: {a[2][1]}, Nota do Teste: {a[2][2]}")

def consultar(id,turma):
    for a in turma:
        if a[1] == id:
            print(f'''Este é o aluno de id {id}: 
            Nome: {a[0]}, Nota do TPC: {a[2][0]}, Nota do Projeto: {a[2][1]}, Nota do Teste: {a[2][2]}''')

def guardarTurma(turma,nometurma):
    f = open(f"./{nometurma}.txt", "a")
    for t in turma:
        f.write(f"{t[0]};{t[1]};{t[2][0]};{t[2][1]};{t[2][2]}\n")
    print("Turma guardada com sucesso")

def carregarTurma(nometurma):
    f = open(f"./{nometurma}.txt", "r")
    for linha in f:
        print(linha, end = '')

def menu():
    j = True

    while j == True:
        esc = int(input('''Menu:
            (1) Criar uma turma
            (2) Adicionar um aluno na turma
            (3) Listar a turma
            (4) Consultar um aluno pelo ID
            (5) Guardar turma
            (6) Carregar turma
            (0) Sair
                    
            Escolha uma opção: '''))

        if esc not in range(0,7):
            print("Escolha inválida")
        elif esc == 0:
            f.close()
            j = False
        elif esc == 1:
            d = input("Insira o nome da turma: ")
            t = criarTurma()
        elif esc == 2:
            inserirAluno(t)
        elif esc == 3:
            listarTurma(t)
        elif esc == 4:
            id = int(input("Insira o ID do aluno: "))
            consultar(id,t)
        elif esc == 5:
            guardarTurma(t,d)
        elif esc == 6:
            p = input("Insira o nome da turma: ")
            print("Nome;ID;Nota do TPC;Nota do Projeto;Nota do Teste")
            carregarTurma(p)

menu()
```
