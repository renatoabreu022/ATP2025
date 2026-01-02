# Projeto Laboratorial – Simulação de uma Clínica Médica

Projeto realizado no âmbito da Unidade Curricular de Algoritmos e Técnicas de Programação por:
- Inês Vieira (A111979) 
- Renato Abreu (A112333)

Requisitos:
- Python 3.x
- Bibliotecas: numpy, matplotlib, PySimpleGUI, time, random, json, importlib

Para executar a simulação:
1. Garantir que todos os ficheiros do projeto estão na mesma pasta
2. Executar um dos ficheiros seguintes:
    - `clinicaTerminal.py`
    - `clinicaApp.py`

---

Neste projeto, foi-nos pedido que criássemos um programa em *Python* que permitisse a simulação do funcionamento de uma clínica médica tanto no terminal do computador como numa interface gráfica, sendo possível analisar este sistema face a certos parâmetros como a disponibilidade de médicos ou o tempo de atendimento de cada paciente.

Assim sendo, este programa reproduz a chegada de pacientes ao longo do tempo, o seu atendimento e a formação gradual de filas de espera, devolvendo, no fim, estatísticas descritivas da simulação que permitem a análise do melhor ou pior desempenho da clínica para atender atempadamente cada indivíduo dentro de um tempo dado, recorrendo a um modelo de simulação por eventos discretos. O sistema evolui com base na ocorrência destes eventos, sendo os principais a chegada de pacientes e a saída dos mesmos.

Para uma melhor organização do programa como um todo, dividimo-lo em ficheiros, cada um com a sua função:
- `main.py` *— contém o corpo da simulação*
- `faux.py` *— reúne todas as funções auxiliares ao funcionamento da simulação*
- `variaveis.py` *— reúne as variáveis necessárias à simulação*
- `pessoas.json` *— base de dados com informação sobre pacientes*
- `clinicaTerminal.py` *— simulação a funcionar no terminal*
- `clinicaApp.py` *— interface gráfica da simulação*

### Funcionamento da Simulação

1. **Chegadas**

    A simulação, presente no ficheiro `main.py`, inicia-se com a leitura da base de dados dos pacientes e a seleção aleatória dos pacientes que vão entrar naquela simulação, gerando e guardando todos os eventos de chegada dos pacientes de forma ordenada até à hora definida. 
    
    Estas chegadas são geradas tendo por base taxas de chegada de pacientes que variam com a hora do dia, permitindo verificar horários com maior ou menor afluência de pacientes. Assim que todas as chegadas do dia forem guardadas, o programa inicia a sua leitura. 

2. **Processamento de Eventos**

    Por cada chegada que o programa lê, é verificado se existe algum médico livre. No caso de existir, este paciente é atribuído ao médico, são gerados o tempo que a consulta demora e o evento de saída desta pessoa. 

3. **Gestão das Filas**

    Caso contrário, verifica-se se este paciente é ou não prioritário e este é posicionado na sua respetiva fila. Ainda que tecnicamente existam duas filas no programa, interpretamo-las como uma única fila, na qual os pacientes prioritários são atendidos primeiro.

4. **Saídas**

    A duração de cada consulta é aleatória e gerada a partir de uma distribuição normal à volta de um valor médio e um desvio padrão configuráveis.
    
    Assim que um evento de saída ocorre, o programa verifica se exitem pacientes prioritários em espera e somente no caso de esta fila estar vazia o programa segue para os pacientes sem prioridade. Assim que um paciente é detetado, este é guardado numa variável ao mesmo tempo que é removido da fila de espera. 

O programa segue estes passos até que a fila de eventos esteja vazia.

No fim deste ciclo principal, o programa tem guardadas diferentes métricas importantes:
- Tempo de espera de cada paciente
- Tempo de duração de cada consulta
- Tempo total que cada paciente permaneceu na clínica
- Peso que cada tamanho da fila teve ao longo do tempo *— produto entre o tamanho da fila e o tempo que ela permaneceu nesse tamanho*
- Tempo que cada médico esteve ocupado com algum paciente

Estas métricas são usadas para gerar os gráficos e estatísticas da simulação.

Existem três parâmetros que a função da simulação pede para determinar o seu funcionamento:
- `taxa` — pode tomar o valor de um inteiro positivo *(usa esse valor como taxa constante)* ou `-1` *(usa taxas que variam com a hora)*
- `terminal` — pode tomar o valor `True` ou `False`, *determinando se os eventos são ou não impressos no terminal*
- `output` — precisa de receber uma lista que pode ter elementos *(guarda os eventos na lista para serem mostrados na GUI)* ou não *(não guarda os eventos)*

Modificações nestes parâmetros são necessárias para a utilização da função principal na interface e no terminal, permitindo a reutilização da mesma função para ambientes com funcionamentos diferentes.

Para além destes, o utilizador, pela versão em terminal, na interface ou nos próprios ficheiros, pode alterar certos parâmetros:
- O número de médicos disponíveis
- O tempo médio e o desvio padrão da duração das consultas
- As taxas que variam ao longo do tempo
- O tempo de espera entre a impressão de cada evento na tela

Estas modificações permitem verificar como cada variável altera o funcionamento da clínica tanto individualmente como em conjunto.

### Gráficos Gerados

1. **Evolução do Tamanho da Fila Geral**

    Variáveis represendas: 
    - Eixo horizontal(x) — *tempo da simulação em minutos*
    - Eixo vertical(y) — *número total de pacientes em espera tanto na fila prioritária como na fila não prioritária*

    Este gráfico representa a evolução do tamanho da fila geral (prioritária + não prioritária) ao longo do tempo de simulação.
    Com isto pretendemos avaliar os períodos de maior chegada de pacientes e avaliar se a capacidade de atendimento é suficiente face à taxa de chegada de pacientes.

    Observamos:
    - Crescimento ou redução das filas ao longo da simulação
    - Existência de picos de espera
    - Estabilidade ou instabilidade do sistema (se a fila tende a crescer indefinidamente ou a estabilizar)

2. **Evolução do Tamanho da Fila prioritária**

    Variáveis representadas:
    - Eixo horizontal (x) — *tempo da simulação em minutos*
    - Eixo vertical (y) — *número de pacientes prioritários em espera*

    Este gráfico mostra a evolução da fila de pacientes prioritários ao longo do tempo de simulação.
    Isto permite-nos avaliar o mecanismo de prioridade que implementamos, ou seja, verificar se estes pacientes são efetivamente atendidos mais rapidamente quando comparados com os não prioritários.

    Observamos:
    - A frequência com que pacientes prioritários aguardam atendimento
    - Se a fila prioritária tende a acumular pacientes
    - A eficácia do sistema de prioridades em situações de pico

3. **Evolução do Tamanho da Fila Não prioritária**

    Variáveis representadas:
    - Eixo horizontal (x) — *tempo da simulação em minutos*
    - Eixo vertical (y) — *número de pacientes não prioritários em espera*

    Este gráfico representa a evolução da fila de espera dos pacientes não prioritários ao longo do tempo de simulação.
    Assim sendo, permite-nos avaliar o impacto das prioridades no tempo de espera destes pacientes e analisar se a sua fila sofre atrasos significativos em períodos de maior taxa de chegada de pacientes.

    Observamos:
    - Períodos em que os pacientes não prioritários são mais afetados
    - Possíveis períodos de acumulação excessiva de pacientes


4. **Evolução da Ocupação Média dos Médicos**

    Variáveis representadas:
    - Eixo horizontal (x) — *tempo da simulação em minutos*
    - Eixo vertical (y) — *percentagem média de médicos ocupados (%)*

    Este gráfico apresenta a evolução da ocupação média dos médicos ao longo do tempo de simulação.
    O objetivo é analisar a utilização dos recursos humanos da clínica, permitindo identificar períodos de subutilização ou sobrecarga.

    Observamos:
    - Avaliar se o número de médicos é adequado
    - Identificar momentos de pico de trabalho

5. **Tamanho Médio da Fila vs. Taxa de Chegada de Pacientes**

    Variáveis representadas:
    - Eixo horizontal (x) — *taxa média de chegada de pacientes (pacientes/hora)*
    - Eixo vertical (y) — *tamanho da fila geral*

    Este gráfico mostra a relação entre a taxa média de chegada de pacientes e o tamanho médio da fila de espera, realiza automaticamente várias simulações para diferentes taxas de chegada (10 a 30) e apresenta o impacto no tamanho médio da fila.
    O seu objetivo é analisar a sensibilidade do sistema a variações na procura e identificar o ponto a partir do qual a clínica entra em regime de congestionamento.
    Sendo assim, ajuda-nos a tomar decisões acerca do número de médicos ou reorganização de horários.

    Observamos:
    - O impacto do aumento da procura no desempenho do sistema
    - Limitações operacionais da clínica
    
    Particulariades:
    - É realizado através da execução repetida da simulação, mantendo todos os parâmetros do sistema constantes, exceto um.
        - Parâmetro que varia: taxa média de chegada de pacientes
        - Unidade: pacientes/hora
        - Distribuição: processo de chegadas modelado por uma distribuição exponencial *(distribuição de Poisson)*
    - Em cada iteração:
        - A taxa de chegada é fixada num determinado valor
        - O estado da simulação é reiniciado por cada taxa
        - O sistema é sempre simulado durante o mesmo período de tempo
        - São recolhidas métricas de desempenho no final da simulação
    - A taxa de chegada varia entre 10 e 30 pacientes por hora, permitindo analisar o comportamento do sistema desde situações de baixa procura até cenários de sobrecarga
    


### Interface Gráfica 

A interface gráfica tem como objetivo permitir ao utilizador configurar, executar e analisar a simulação da clínica médica de forma interativa, sem necessidade de modificar o código-fonte. 

**Permite ao utilizador:**
- Definir os parâmetros principais da simulação;
- Iniciar a simulação e acompanhar os eventos;
- Controlar a velocidade de apresentação dos eventos;  
- Gerar gráficos (referidos acima) para análise do comportamento do sistema.

**Parâmetros Controlados pelo Utilizador:**
- Número de médicos disponíveis na clínica;
- Hora de início da simulação;
- Tempo médio de consulta e respetivo desvio padrão em minutos;
- Taxas de chegada de pacientes, definidas para diferentes períodos do dia a partir da hora de início *(0–3h, 3–5h, 5–7h, 7–9h e 9–12h)*
- Tempo entre eventos, através de um slider, que controla a velocidade com que os eventos são apresentados no ecrã *(0 a 0.3 segundos)*

Estes parâmetros permitem ao utilizador simular diferentes cenários operacionais da clínica.

Os gráficos são apresentados em janelas externas utilizando o *Matplotlib*

### Resultados e Observações

**Objetivo:** Interpretar o comportamento observado na simulação da clínica médica.

1. **Tendências do programa:**
    - O número de pacientes nas filas aumenta nos períodos com maior taxa de chegada, refletindo o fluxo esperado de pacientes ao longo do dia.
    - A ocupação dos médicos acompanha inversamente o tamanho das filas *— quando há muitos médicos disponíveis, a fila diminui rapidamente; quando todos estão ocupados, a fila cresce*
    - O tempo médio de espera aumenta conforme a taxa de chegada se aproxima ou excede a capacidade de atendimento dos médicos.

2. **Comportamentos esperados:**
    - Pacientes prioritários são atendidos mais rapidamente
    - O tempo médio de permanência na clínica cresce com o aumento da taxa de chegada
    - Médicos menos ocupados recebem pacientes preferencialmente, equilibrando a carga de trabalho

3. **Observações:**

    Ocorrem pequenas flutuações na ocupação dos médicos e nos tamanhos das filas podem ocorrer devido à aleatoriedade do tempo de consulta e chegadas, mesmo com taxas constantes.

4. **Variabilidade do sistema:**

    A simulação apresenta uma variabilidade que parece ser natural, devido à distribuição aleatória das chegadas e dos tempos de consulta. Esta variabilidade é mais visível em períodos de alta taxa de chegada, onde pequenas diferenças no tempo de chegada de cada paciente podem afetar significativamente o tempo médio de espera e o tamanho das filas.

    Métricas como tempo médio de espera e ocupação de médicos podem variar entre diferentes execuções da simulação, mesmo mantendo os mesmos parâmetros.

5. **Fatores com maior impacto:**
    - Taxa de chegada de pacientes — *influencia diretamente o tamanho das filas e o tempo de espera*
    - Número de médicos disponíveis — *impacta a ocupação média e a capacidade de atender pacientes sem acumular filas*
    - Distribuição de prioridades — *pacientes prioritários reduzem o tempo de espera para casos críticos, alterando a dinâmica da fila geral*

De forma geral, o sistema comporta-se como esperado, com tendências claras na relação entre taxa de chegada, número de médicos e tempo de espera. 
A variabilidade observada destaca a importância de analisar vários cenários para compreender o comportamento da clínica em diferentes condições.


### Conclusões

A simulação permitiu analisar o desempenho operacional de uma clínica médica de forma controlada, mostrando como os diferentes parâmetros influenciam o tempo de espera e a saturação dos recursos.
Foi possível quantificar métricas importantes, como tempo médio de consulta, tempo médio de permanência na clínica, tamanho médio das filas e percentagem de ocupação dos médicos, oferecendo uma visão clara da dinâmica do programa.
Este modelo confirma que pacientes prioritários são atendidos mais rapidamente.

No entanto, o programa assume que os tempos de consulta seguem distribuições fixas e que os médicos têm disponibilidade constante durante todo o período, o que pode diferir da realidade, não se consideram fatores externos como ausências de médicos ou atrasos inesperados e deixa-se que os médicos trabalhem até depois do fecho definido da clínica para atender todos os que chegam até à hora definida.

Apesar das limitações, o modelo é flexível e pode ser ampliado para representar cenários mais complexos e próximos da realidade.
