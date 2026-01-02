import main as m
import variaveis as var

b = int(input('Quer utilizar os valores predefinidos para a simulação da clínica? (0 - Não; Outros inteiros - Sim) '))

if b == 0:
    var.hStart = int(input('A que horas do dia pretende abrir a clínica? '))
    var.nMeds = int(input('Quantos médicos estarão disponíveis durante esta simulação? '))
    var.tmed = float(input('Qual será o tempo médio de cada consulta? '))
    var.desv = float(input('Qual será o desvio padrão ao tempo médio de cada consulta? '))
    var.taxas[0]['taxa'] = int(input('Qual será a taxa de chegada (pacientes/hora) nas primeiras 3 horas? '))/60
    var.taxas[1]['taxa'] = int(input('Qual será a taxa de chegada (pacientes/hora) nas 2 horas seguintes? '))/60
    var.taxas[2]['taxa'] = int(input('Qual será a taxa de chegada (pacientes/hora) nas 2 horas seguintes? '))/60
    var.taxas[3]['taxa'] = int(input('Qual será a taxa de chegada (pacientes/hora) nas 2 horas seguintes? '))/60
    var.taxas[2]['taxa'] = int(input('Qual será a taxa de chegada (pacientes/hora) nas últimas 3 horas? '))/60

m.simula(-1,True,[])

m.graficoTamanhoFilas(True)
m.graficoOcupMedicos(True)
m.grafico3(True)