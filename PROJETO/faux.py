import numpy as np
import variaveis as var

def enqueue(q, ev):
    if not q:
        q.append(ev)
    elif q:
        i = 0
        colocado = False
        while i < len(q) and not colocado:
            if ev[0] < q[i][0]:
                q.insert(i, ev)
                colocado = True
            i += 1
        if not colocado: 
            q.append(ev)
    return q 

def dequeue(q):
    return q[0], q[1:]

def empty(q):
    return len(q) == 0

def geraIntChegada(taxa):
    return np.random.exponential(1/taxa)

def geraTempoConsulta(tmed,desv):
    return max(1, np.random.normal(tmed,desv)) 

def pesquisaID(id, pesq, bd):
    indicePorID = {d['id']: d for d in bd} 
    if pesq == 'prioridade':
        v = indicePorID[id][pesq]['prioritario']
    else:
        v = indicePorID[id][pesq]
    return v

def pesquisaMedico(listaMed): 
    med = None
    livres = [m for m in listaMed if not m[1]] 
    if livres: 
        med = min(livres, key = lambda m: m[4])
    return med

def ocupaMedico(m):
    m[1] = not m[1]

def inicioConsulta(m, t): 
    m[3] = t

def atribuiPaciente(m, p):
    m[2] = p

def tempoOcupado(m, t):
    m[4] += t

def min2hour(t, hInicio):
    h = int(t//60)
    m = int(t%60)
    h2 = (hInicio + h) % 24
    return f'{h2:02d}:{m:02d}' 

def reset():
    var.tempoAtual = 0.0
    var.queue = []
    var.queuePrioritario = []
    var.eventoAtual = ()
    var.queueEv = []
    var.chegadas = {}
    var.temposClinica = []
    var.temposEspera = []
    var.temposConsulta = []
    var.tmedEspera = 0
    var.tmedConsulta = 0
    var.tmedClinica = 0
    var.ocupacaoMeds = {}
    var.dAtendidos = 0
    var.tamQ = 0
    var.ultimoTempoQ = 0
    var.areaQ = 0
    var.tmaxQ = 0
    var.tmedQ = 0
    var.tamQP = 0
    var.ultimoTempoQP = 0
    var.areaQP = 0
    var.tmaxQP = 0
    var.tmedQP = 0
    var.tamQQP = 0
    var.ultimoTempoQQP = 0
    var.areaQQP = 0
    var.tmaxQQP = 0
    var.tmedQQP = 0
    var.evolucaoTempo = []
    var.evolucaoQueue = []
    var.evolucaoQueueP = []
    var.evolucaoQQP = []
    var.evolucaoOcup = []
    var.meds = [[f'm{i}', False, None, 0.0, 0.0] for i in range(var.nMeds)]