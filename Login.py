import PySimpleGUI as sg
import CalculoIMC
from time import sleep

# Layout
import cadastroClientes

sg.change_look_and_feel('DarkAmber')
layout = [
    [sg.Text('Usuário', size=(10, 0)), sg.Input(key='usuario', size=(15, 0))],
    [sg.Text('Senha', size=(10, 0)), sg.Input(key='senha', password_char='*', size=(15, 0))],
    [sg.Checkbox('Salvar login?', key='salvarLogin')],
    [sg.Button('Entrar'), sg.Text(size=(20,0), key='mensagem')]
]
# Janela
janela = sg.Window('Login', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Gabriel' and valores['senha'] == '1234':
            janela['mensagem'].update('Bem Vindo !')
            janela.close()
            cadastroClientes.Iniciar()
        else:
            janela['mensagem'].update('Usuário ou Senha Incorreto !', text_color='red')

