import matplotlib.pyplot as plt

def extraiMin(t):
    res = []
    for _,tmin,_,_ in t:
        res.append(tmin)
    return res

def extraiMax(t):
    res = []
    for _,_,tmax,_ in t:
        res.append(tmax)
    return res

def extraiPrecip(t):
    res = []
    for _,_,_,p in t:
        res.append(p)
    return res

def grafTabMeteo(t):
    x1 = list(range(1,len(t)+1))
    y1 = extraiMax(t)
    plt.plot(x1,y1,label = 'Temperatura Máxima', color = 'orangered')

    x2 = list(range(1,len(t)+1))
    y2 = extraiMin(t)
    plt.plot(x2,y2,label = 'Temperatura Mínima', color = 'skyblue')

    x3 = list(range(1,len(t)+1))
    y3 = extraiPrecip(t)
    plt.plot(x3,y3,label = 'Precipitação', color = 'slateblue')

    plt.title('Evolução Meteorológica')
    plt.legend(loc = 'best')
    plt.show()
    return

def medias(tabMeteo):
    res = []
    for i in tabMeteo:
        res.append((i[0],(i[1]+i[2])/2))
    return res

def guardaTabMeteo(t, fnome):
    f = open(f"./{fnome}","a")
    for i in t:
        f.write(f"{i[0][0]};{i[0][1]};{i[0][2]};{i[1]};{i[2]};{i[3]}\n")
    f.close()
    return

def carregaTabMeteo(fnome):
    res = []
    f = open(f"./{fnome}","r")
    for l in f:
        c = l.split(';')
        res.append(((int(c[0]),int(c[1]),int(c[2])),float(c[3]),float(c[4]),float(c[5])))
    f.close()
    return res

def minMin(tabMeteo):
    minm = tabMeteo[0][1]
    for i in tabMeteo:
        if i[1] < minm:
            minm = i[1]
    return minm

def amplTerm(tabMeteo):
    res = []
    for i in tabMeteo:
        ampl = i[2] - i [1]
        res.append((i[0],ampl))
    return res

def maxChuva(tabMeteo):
    maxc = tabMeteo[0][3]
    data = tabMeteo[0][0]
    for i in tabMeteo:
        if i[3] > maxc:
            maxc = i[3]
            data = i[0]
    return (data, maxc)

def diasChuvosos(tabMeteo, p):
    res = []
    for i in tabMeteo:
        if i[3] > p:
            res.append((i[0],i[3]))
    return res

def maxPeriodoCalor(tabMeteo, p):
    res = []
    for i in tabMeteo:
        if i[3] < p:
            res.append((i[0],i[3]))
    troca = True
    while troca:
        troca = False
        i = 0
        while i < len(tabMeteo) - 1:
            ano1,mes1,dia1 = tabMeteo[i][0]
            ano2,mes2,dia2 = tabMeteo[i+1][0]
            if (ano1,mes1,dia1) > (ano2,mes2,dia2):
                tabMeteo[i] , tabMeteo[i+1] = tabMeteo[i+1] , tabMeteo[i]
                troca = True
            i += 1
    j = 0
    c = 0
    cmaior = 0
    while j < len(tabMeteo):
        if tabMeteo[j][3] < p:
            c +=1
        else:
            if c > cmaior:
                cmaior = c
            c = 0
        j += 1
    if c > cmaior:
        cmaior = c
    return cmaior

def regDia():
    a = int(input("Insira o ano da data que quer registar: "))
    m = int(input("Insira o mês da data que quer registar: "))
    d = int(input("Insira o dia da data que quer registar: "))
    tmax = float(input("Insira a temperatura máxima nesse dia: "))
    tmin = float(input("Insira a temperatura mínima nesse dia: "))
    p = float(input("Insira a precipitação desse dia: "))
    print("Dia registado com sucesso!")
    return ((a,m,d), tmin, tmax, p)

def menu():
    b = True
    tabMeteo = []
    while b:
        esc = int(input('''Escolha uma das opções seguintes
                    (1) Registar Dia
                    (2) Temperaturas Médias
                    (3) Temperatura Mínima Mais Baixa
                    (4) Amplitudes Térmicas
                    (5) Dia de Precipitação Máxima
                    (6) Dias Chuvosos
                    (7) Máximo Período de Calor
                    (8) Gráfico de Evolução Meteorológica 
                    (9) Guardar Registos
                    (10) Carregar Registos
                    (0) Sair
                    
                    Opção: '''))
        if esc == 0:
            b = False
        elif esc == 1:
            t = regDia()
            tabMeteo.append(t)
        elif esc == 2:
            med = medias(tabMeteo)
            print(med)
        elif esc == 3:
            min = minMin(tabMeteo)
            print(min)
        elif esc == 4:
            amp = amplTerm(tabMeteo)
            print(amp)
        elif esc == 5:
            max = maxChuva(tabMeteo)
            print(max)
        elif esc == 6:
            p = float(input('Defina o valor de precipitação mínima para um dia chuvoso: '))
            dia = diasChuvosos(tabMeteo,p)
            print(dia)
        elif esc == 7:
            p = float(input('Defina o valor de precipitação máximo para um dia de calor: '))
            calor = maxPeriodoCalor(tabMeteo,p)
            print(calor)
        elif esc == 8:
            grafTabMeteo(tabMeteo)
        elif esc == 9:
            fnome = input("Indique em qual ficheiro quer guardar os registos: ")
            guardaTabMeteo(tabMeteo,fnome)
        elif esc == 10:
            fnome = input("Indique de qual ficheiro quer carregar os registos: ")
            print(carregaTabMeteo(fnome))
        else:
            print('Opção inválida')

menu()