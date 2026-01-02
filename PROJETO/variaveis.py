hStart = 8 
nMeds = 6
tmed = 15.9 
desv = 2 
tempoAtual = 0.0
tempoSim = 12*60
taxas = [
    {
        'tempInicio': 0,
        'tempFim': 3*60,
        'taxa': 20/60
    },
    {
        'tempInicio': 3*60,
        'tempFim': 5*60,
        'taxa': 40/60
    },
    {
        'tempInicio': 5*60,
        'tempFim': 7*60,
        'taxa': 33/60
    },
    {
        'tempInicio': 7*60,
        'tempFim': 9*60,
        'taxa': 36/60
    },
    {
        'tempInicio': 9*60,
        'tempFim': 12*60,
        'taxa': 38/60
    },
] 

meds = [[f'm{i}', False, None, 0.0, 0.0] for i in range(nMeds)]
queue = []
queuePrioritario = []
eventoAtual = ()
queueEv = [] 

chegadas = {} 
temposClinica = []
temposEspera = []
temposConsulta = []

tmedEspera = 0
tmedConsulta = 0
tmedClinica = 0
ocupacaoMeds = {} 
dAtendidos = 0

tamQ = 0
ultimoTempoQ = 0
areaQ = 0
tmaxQ = 0
tmedQ = 0

tamQP = 0
ultimoTempoQP = 0
areaQP = 0
tmaxQP = 0
tmedQP = 0

tamQQP = 0
ultimoTempoQQP = 0
areaQQP = 0
tmaxQQP = 0
tmedQQP = 0

evolucaoTempo = []
evolucaoQueue = []
evolucaoQueueP = []
evolucaoQQP = []
evolucaoOcup = []



