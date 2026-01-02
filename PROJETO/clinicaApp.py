import FreeSimpleGUI as sg
import main as m
import variaveis as var
import time
import matplotlib 
import importlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


layout = [
    [sg.Text('Simulação de uma Clínica Médica', text_color='#222222', justification='center', expand_x=True, font=('Helvetica', 30, 'bold'), background_color='#F5F5F5')],

    [sg.Frame(
    ' Parâmetros da Simulação ',
    [
        [sg.Text('Número de médicos:', text_color='#222222', font=('Helvetica', 14), background_color='#F5F5F5'), sg.Input(key='-MEDS-', font=('Helvetica', 14), default_text='6', expand_x=True, size=(20,1)), sg.Text('Hora de início:', font=('Helvetica', 14), text_color='#222222', background_color='#F5F5F5'), sg.Input(font=('Helvetica', 14), key='-HSTART-', default_text=str(var.hStart), expand_x=True, size=(20,1))],
        [sg.Text('Tempo médio consulta (min):', text_color='#222222', font=('Helvetica', 14), background_color='#F5F5F5'), sg.Input(key='-TMED-', font=('Helvetica', 14), default_text='15.9', expand_x=True, size=(10,1)), sg.Text('Desvio padrão da consulta (min):', text_color='#222222', font=('Helvetica', 14), background_color='#F5F5F5'), sg.Input(key='-DESV-', font=('Helvetica', 14), default_text='2', expand_x=True, size=(10,1))],
    ],
    title_color='#222222',
    relief=sg.RELIEF_SUNKEN,
    font=('Helvetica', 14, 'bold'),
    expand_x=True,
    background_color='#F5F5F5'
),
sg.Frame(
    ' Taxas (doentes/hora) ',
    [
        [sg.Text('0-3h:', font=('Helvetica', 14), text_color='#222222', background_color='#F5F5F5'), sg.Input(font=('Helvetica', 14), key='-TAXA1-', expand_x=True, default_text=str(int(var.taxas[0]['taxa']*60)), size=(10,1)),
         sg.Text('3-5h:', font=('Helvetica', 14), text_color='#222222', background_color='#F5F5F5'), sg.Input(font=('Helvetica', 14), key='-TAXA2-', expand_x=True, default_text=str(int(var.taxas[1]['taxa']*60)), size=(10,1))],
        [sg.Text('5-7h:', font=('Helvetica', 14), text_color='#222222', background_color='#F5F5F5'), sg.Input(font=('Helvetica', 14), key='-TAXA3-', expand_x=True, default_text=str(int(var.taxas[2]['taxa']*60)), size=(10,1)),
         sg.Text('7-9h:', font=('Helvetica', 14), text_color='#222222', background_color='#F5F5F5'), sg.Input(font=('Helvetica', 14), key='-TAXA4-', expand_x=True, default_text=str(int(var.taxas[3]['taxa']*60)), size=(10,1))],
        [sg.Text('9-12h:', font=('Helvetica', 14), text_color='#222222', background_color='#F5F5F5'), sg.Input(font=('Helvetica', 14), key='-TAXA5-', expand_x=True, default_text=str(int(var.taxas[4]['taxa']*60)), size=(10,1))],
    ],
    expand_x=True,
    title_color='#222222',
    relief=sg.RELIEF_SUNKEN,
    font=('Helvetica', 14, 'bold'),
    background_color='#F5F5F5'
)],

    [sg.Push(background_color='#F5F5F5')], 
    
    [sg.HorizontalSeparator(), sg.Text('Teste de variação da taxa de chegada', text_color='#222222', justification='center', expand_x=True, font=('Helvetica', 18, 'bold'), background_color='#F5F5F5'), sg.HorizontalSeparator()],
    [sg.Push(background_color='#F5F5F5'), sg.Button(' Gerar Gráfico ', font=('Helvetica', 23), button_color=('#F5F5F5', '#94B294')), sg.Push(background_color='#F5F5F5')],
    [sg.Push(background_color='#F5F5F5')],
    [sg.Push(background_color='#F5F5F5')],
    [sg.HorizontalSeparator(), sg.Text('Simulação', text_color='#222222', justification='center', expand_x=True, font=('Helvetica', 18, 'bold'), background_color='#F5F5F5'), sg.HorizontalSeparator()],
    [sg.Push(background_color='#F5F5F5'), sg.Button(' Simular Clínica ▶ ', font=('Helvetica', 23), button_color=('#F5F5F5','#2E7D32')), sg.Push(background_color='#F5F5F5')],
    [sg.Push(background_color='#F5F5F5')],
    [sg.Push(background_color='#F5F5F5')],
    [sg.Push(background_color='#F5F5F5'), sg.Text('Tempo entre eventos (segundos)', enable_events=True,text_color='#222222', justification='center', expand_x=True, font=('Helvetica', 15, 'bold'), background_color='#F5F5F5'), sg.Push(background_color='#F5F5F5')],
    [sg.Push(background_color='#F5F5F5'), sg.Slider(range=(0,0.3), default_value=0, orientation='h', resolution= 0.01, size=(60,12), key='-DELAY-', background_color='#F5F5F5', expand_x=True, font=('Helvetica', 11), text_color='#222222', trough_color='#AEAEAE'), sg.Push(background_color='#F5F5F5')],
    [sg.Push(background_color='#F5F5F5')],
    [sg.Multiline(size=(70, 15), key='-OUTPUT-', expand_x=True, expand_y=True, background_color='#F5F5F5', text_color='#222222',autoscroll=True)],
    [sg.Push(background_color='#F5F5F5')],
    [sg.Push(background_color='#F5F5F5'), sg.Text('Gerar Gráficos', text_color='#222222', justification='center', expand_x=True, font=('Helvetica', 15, 'bold'), background_color='#F5F5F5'), sg.Push(background_color='#F5F5F5')],
    [sg.Push(background_color='#F5F5F5'), sg.Button(' Fila de espera ', font=('Helvetica', 14), button_color=('#F5F5F5', '#0C449E')), sg.Button(' Ocupação médicos ', font=('Helvetica', 14), button_color=('#F5F5F5', '#0C449E')), sg.Push(background_color='#F5F5F5')],
    [sg.Push(background_color='#F5F5F5')],

    [sg.HorizontalSeparator()],

    [sg.Text('Projeto realizado por: Inês Vieira e Renato Abreu', text_color='#222222', font=('Helvetica',14), background_color='#F5F5F5'), sg.Push(background_color='#F5F5F5'), sg.Button('Sair', font=('Helvetica', 14), button_color=('#F5F5F5','firebrick'))]
]

window = sg.Window('Clínica Médica', layout, resizable=True, background_color='#F5F5F5')

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, 'Sair'):
        break

    if event == ' Simular Clínica ▶ ':
        importlib.reload(var)

        var.hStart = int(values['-HSTART-'])

        t1 = int(values['-TAXA1-'])/60
        t2 = int(values['-TAXA2-'])/60
        t3 = int(values['-TAXA3-'])/60
        t4 = int(values['-TAXA4-'])/60
        t5 = int(values['-TAXA5-'])/60

        var.taxas = [
            {"tempInicio": 0, "tempFim": 3*60, "taxa": t1},
            {"tempInicio": 3*60, "tempFim": 5*60, "taxa": t2},
            {"tempInicio": 5*60, "tempFim": 7*60, "taxa": t3},
            {"tempInicio": 7*60, "tempFim": 9*60, "taxa": t4},
            {"tempInicio": 9*60, "tempFim": 12*60, "taxa": t5},
        ]

        var.nMeds = int(values['-MEDS-'])
        var.tmed = float(values['-TMED-'])
        var.desv = float(values['-DESV-'])
        
        var.meds = [[f'm{i}', False, None, 0.0, 0.0] for i in range(var.nMeds)]
        
        delay = values['-DELAY-']

        output_txt = ['Seja Bem-vindo!']

        m.simula(-1,True,output_txt)

        window['-OUTPUT-'].update('')
        
        for linha in output_txt:
            window['-OUTPUT-'].print(linha)
            if delay != 0:
                window.refresh()
                time.sleep(delay)
        
        window['-OUTPUT-'].print('Simulação executada com sucesso!')


    if event == ' Fila de espera ':
        plt.close('all')
        m.graficoTamanhoFilas(False)

    if event == ' Ocupação médicos ':
        plt.close('all')
        m.graficoOcupMedicos(False)

    if event == ' Gerar Gráfico ':
        plt.close('all')

        var.nMeds = int(values['-MEDS-'])
        var.tmed = float(values['-TMED-'])
        var.desv = float(values['-DESV-'])

        m.grafico3(False)


window.close()