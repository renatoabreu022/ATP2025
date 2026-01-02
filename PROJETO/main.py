import random
import json
import time
import faux as fun
import variaveis as var
import numpy as np
import matplotlib 
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt

f = open('pessoas.json', 'r', encoding='utf-8')
pacientes = json.load(f)
def simula(taxa, terminal, output):
    listaPacientes = pacientes.copy() 
    random.shuffle(listaPacientes)
    i = 0
    while var.tempoAtual < var.tempoSim and i < len(listaPacientes):
        fun.enqueue(var.queueEv, (var.tempoAtual, 'Chegada', listaPacientes[i]['id']))

        if taxa == -1:
            for v in var.taxas:
                if var.tempoAtual in range(v['tempInicio'],v['tempFim']):
                    tx = v['taxa']
        else:
            tx = taxa

        temp = fun.geraIntChegada(tx)
        var.tempoAtual += temp
        i += 1

    while var.queueEv:
        var.eventoAtual, var.queueEv = fun.dequeue(var.queueEv)
        if terminal:
            if not output:
                print(f'[{fun.min2hour(var.eventoAtual[0], var.hStart)}] {var.eventoAtual[1]} {fun.pesquisaID(var.eventoAtual[2], 'nome', pacientes)}({var.eventoAtual[2]})')
            elif output:
                output.append(f'[{fun.min2hour(var.eventoAtual[0], var.hStart)}] {var.eventoAtual[1]} {fun.pesquisaID(var.eventoAtual[2], 'nome', pacientes)}({var.eventoAtual[2]})')
        var.tempoAtual = var.eventoAtual[0] 
        var.evolucaoTempo.append(var.tempoAtual)
        var.evolucaoQueue.append(var.tamQ)
        var.evolucaoQueueP.append(var.tamQP)
        var.evolucaoQQP.append(var.tamQQP)

        taxaOcupados = 100 * sum(1 for m in var.meds if m[1])/len(var.meds) 
        var.evolucaoOcup.append(taxaOcupados)

        if var.eventoAtual[1] == 'Chegada':

            var.chegadas[var.eventoAtual[2]] = var.tempoAtual 

            medicoAtual = None
            medicoAtual = fun.pesquisaMedico(var.meds)

            if medicoAtual: 
                fun.ocupaMedico(medicoAtual)
                fun.inicioConsulta(medicoAtual, var.tempoAtual)
                tCons = round(fun.geraTempoConsulta(var.tmed, var.desv), 5)
                var.temposConsulta.append(tCons)
                fun.atribuiPaciente(medicoAtual, var.eventoAtual[2])
                fun.enqueue(var.queueEv, (var.tempoAtual + tCons, 'Saída', var.eventoAtual[2]))
                var.temposEspera.append(0)
            else: 
                if fun.pesquisaID(var.eventoAtual[2], 'prioridade', pacientes):
                    variacaoP = var.tempoAtual - var.ultimoTempoQP
                    var.areaQP += var.tamQP * variacaoP 
                    var.ultimoTempoQP = var.tempoAtual 
                    
                    variacaoQ = var.tempoAtual - var.ultimoTempoQQP
                    var.areaQQP += var.tamQQP * variacaoQ
                    var.ultimoTempoQQP = var.tempoAtual

                    var.queuePrioritario.append((var.eventoAtual[2], var.tempoAtual)) 
                    var.tamQP += 1 
                    var.tamQQP += 1

                    if var.tamQP > var.tmaxQP: 
                        var.tmaxQP = var.tamQP 
                    
                    if var.tamQQP > var.tmaxQQP:
                        var.tmaxQQP = var.tamQQP

                else: 
                    variacao = var.tempoAtual - var.ultimoTempoQ 
                    var.areaQ += var.tamQ * variacao
                    var.ultimoTempoQ = var.tempoAtual

                    variacaoQ = var.tempoAtual - var.ultimoTempoQQP
                    var.areaQQP += var.tamQQP * variacaoQ
                    var.ultimoTempoQQP = var.tempoAtual

                    var.queue.append((var.eventoAtual[2], var.tempoAtual))
                    var.tamQ += 1
                    var.tamQQP += 1

                    if var.tamQ > var.tmaxQ:
                        var.tmaxQ = var.tamQ
                    
                    if var.tamQQP > var.tmaxQQP:
                        var.tmaxQQP = var.tamQQP

                if terminal:
                    if not output:
                        print(f'Existe {len(var.queue) + len(var.queuePrioritario)} paciente(s) na fila de espera!')
                    elif output:
                        output.append(f'Existe {len(var.queue) + len(var.queuePrioritario)} paciente(s) na fila de espera!')


        elif var.eventoAtual[1] =='Saída':
            var.dAtendidos += 1
            
            tclin = var.tempoAtual - var.chegadas[var.eventoAtual[2]] 
            var.temposClinica.append(tclin)

            i = 0
            encontrado = False
            while i < len(var.meds) and not encontrado: 
                if var.meds[i][2] == var.eventoAtual[2]:  
                    fun.ocupaMedico(var.meds[i]) 
                    fun.tempoOcupado(var.meds[i], var.tempoAtual-var.meds[i][3])
                    fun.atribuiPaciente(var.meds[i] , None)
                    encontrado = True
                    indiceMed = i
                i=i+1
            
            if var.queuePrioritario:
                variacaoP = var.tempoAtual - var.ultimoTempoQP 
                var.areaQP += var.tamQP * variacaoP
                var.ultimoTempoQP = var.tempoAtual

                variacaoQ = var.tempoAtual - var.ultimoTempoQQP
                var.areaQQP += var.tamQQP * variacaoQ
                var.ultimoTempoQQP = var.tempoAtual

                ev, var.queuePrioritario = fun.dequeue(var.queuePrioritario) 
                prox_doente, tchegada = ev
                var.tamQP -= 1 
                var.tamQQP -= 1

            elif var.queue:
                variacao = var.tempoAtual - var.ultimoTempoQ
                var.areaQ += var.tamQP * variacao
                var.ultimoTempoQ = var.tempoAtual

                variacaoQ = var.tempoAtual - var.ultimoTempoQQP
                var.areaQQP += var.tamQQP * variacaoQ
                var.ultimoTempoQQP = var.tempoAtual

                ev, var.queue = fun.dequeue(var.queue)
                prox_doente, tchegada = ev
                var.tamQ -= 1
                var.tamQQP -= 1

            else:
                prox_doente = None
            
            if prox_doente:
                fun.ocupaMedico(var.meds[indiceMed])
                fun.inicioConsulta(var.meds[indiceMed], var.tempoAtual)
                fun.atribuiPaciente(var.meds[indiceMed], prox_doente)

                tempo_espera = var.tempoAtual - tchegada   
                var.temposEspera.append(tempo_espera) 

                tCons = fun.geraTempoConsulta(var.tmed, var.desv)
                var.queueEv = fun.enqueue(var.queueEv, (var.tempoAtual + tCons, 'Saída', prox_doente))
        if terminal:
            time.sleep(0.07) 

    var.areaQ += var.tamQ * (var.tempoSim - var.ultimoTempoQ)
    var.areaQP += var.tamQP * (var.tempoSim - var.ultimoTempoQP)
    var.areaQQP += var.tamQQP * (var.tempoSim - var.ultimoTempoQQP)

    var.tmedQ = round(var.areaQ / var.tempoSim, 2)
    var.tmedQP = round(var.areaQP / var.tempoSim, 2)
    var.tmedQQP = round(var.areaQQP / var.tempoSim, 2)

    var.tmedConsulta = np.mean(var.temposConsulta) 
    var.tmedClinica = np.mean(var.temposClinica) 

    var.tmedEspera = np.mean(var.temposEspera) 

    if terminal:
        if not output:
            print('========================================')
            print(f'Hoje, atendemos {var.dAtendidos} pacientes!')
            print(f'O tempo médio das consultas foi de {round(var.tmedConsulta,2)} minutos!')
            print(f'Cada paciente esteve, em média, {round(var.tmedClinica, 2)} minutos na clínica!')
            print(f'A fila não prioritária teve um tamanho médio de {var.tmedQ} pacientes e um tamanho máximo de {var.tmaxQ} pacientes!')
            print(f'A fila prioritária teve um tamanho médio de {var.tmedQP} pacientes e um tamanho máximo de {var.tmaxQP} pacientes!')
            print(f'A fila geral teve um tamanho médio de {var.tmedQQP} pacientes e um tamanho máximo de {var.tmaxQQP} pacientes!')
            for m in var.meds:
                print(f'O médico de ID {m[0]} esteve ocupado durante {round(m[4]*100/var.tempoSim, 2)}% do seu horário de trabalho.')
            print(f'O tempo médio de espera dos doentes foi de {round(var.tmedEspera,2)} minutos.')
        elif output:
            output.append('========================================')
            output.append(f'Hoje, atendemos {var.dAtendidos} pacientes!')
            output.append(f'O tempo médio das consultas foi de {round(var.tmedConsulta,2)} minutos!')
            output.append(f'Cada paciente esteve, em média, {round(var.tmedClinica, 2)} minutos na clínica!')
            output.append(f'A fila não prioritária teve um tamanho médio de {var.tmedQ} pacientes e um tamanho máximo de {var.tmaxQ} pacientes!')
            output.append(f'A fila prioritária teve um tamanho médio de {var.tmedQP} pacientes e um tamanho máximo de {var.tmaxQP} pacientes!')
            output.append(f'A fila geral teve um tamanho médio de {var.tmedQQP} pacientes e um tamanho máximo de {var.tmaxQQP} pacientes!')

            for m in var.meds:
                output.append(f'O médico de ID {m[0]} esteve ocupado durante {round(m[4]*100/var.tempoSim, 2)}% do seu horário de trabalho.')
            output.append(f'O tempo médio de espera dos doentes foi de {round(var.tmedEspera,2)} minutos.')


def graficoTamanhoFilas(b):
    plt.figure(figsize=(14,6))
    plt.step(var.evolucaoTempo, var.evolucaoQQP)
    plt.xlabel('Tempo (min)')
    plt.ylabel('Número de pacientes')
    plt.title('Evolução do tamanho da fila geral')
    plt.grid(True)
    plt.show(block=b)

    plt.figure(figsize=(14,6))
    plt.step(var.evolucaoTempo, var.evolucaoQueueP)
    plt.xlabel('Tempo (min)')
    plt.ylabel('Número de pacientes')
    plt.title('Evolução do tamanho da fila prioritária')
    plt.grid(True)
    plt.show(block=b)


    plt.figure(figsize=(14,6))
    plt.step(var.evolucaoTempo, var.evolucaoQueue)
    plt.xlabel('Tempo (min)')
    plt.ylabel('Número de pacientes')
    plt.title('Evolução do tamanho da fila não prioritária')
    plt.grid(True)
    plt.show(block=b)
  
def graficoOcupMedicos(b):
    plt.figure(figsize=(14,6))
    plt.step(var.evolucaoTempo, var.evolucaoOcup)
    plt.xlabel('Tempo da simulação (minutos)')
    plt.ylabel('Ocupação média (%)')
    plt.title('Evolução da ocupação média dos médicos')
    plt.grid(True)
    plt.show(block=b)
   
def grafico3(b):
    mediasFila = []
    for t in range(10,31):
        fun.reset()                      
        simula(t/60, False, [])
        mediasFila.append(var.tmedQQP)

    plt.scatter(range(10,31), mediasFila)
    plt.xlabel('Taxa média de chegada (doentes/hora)')
    plt.ylabel('Tamanho médio da fila')
    plt.title('Tamanho médio da fila vs taxa de chegada')
    plt.grid(True)
    plt.show(block=b)
