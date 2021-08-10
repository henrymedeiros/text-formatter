import PySimpleGUI as sg

def replace(string, old_char, new_char):
    return string.replace(old_char, new_char)
    
def add_char_at_end(string, char):
    return string+char;

def add_char_at_beginning(string, char):
    return char+string;

def encrypt():
    pass

def to_binary():
    pass


class TelaPrincipal:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Seu texto')],
            [sg.Multiline(size=(50,6), key='input')],
            [sg.Text('Escolha uma opção abaixo')],
            [sg.Radio('Substituir', 'options', key='replace')],
            [sg.Text('Antigo termo'), sg.Input(size=(5,0), key='old_char'), sg.Text('Novo termo'), sg.Input(size=(5,0), key='new_char')],
            [sg.Radio('Inserir no fim', 'options', key='insert_at_end')],
            [sg.Button('Processar')]
            
            
        ]
        #Janela
        self.janela = sg.Window('Super Text Formatter').layout(layout)
        self.button, self.values = self.janela.Read()
        #Extrair
        
    def Iniciar(self):
        user_input = self.values['input']
        replace = self.values['replace']
        old_char = self.values['old_char']
        new_char = self.values['new_char']
        insert_at_end = self.values['insert_at_end']
        print(self.values)

        
tela = TelaPrincipal()
tela.Iniciar()