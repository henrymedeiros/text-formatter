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
            [sg.Text('Texto')],
            [sg.Multiline(size=(50,6), key='entrada')],
            [sg.Text('Substituir caracteres')],
            [sg.Text('Antigo'),sg.Input(key='old_char'), sg.Text('Novo'), sg.Input(key='new_char')],
            [sg.Button('Processar')]
            
        ]
        #Janela
        self.janela = sg.Window('Stringnator').layout(layout)
        self.button, self.values = self.janela.Read()
        #Extrair
        
    def Iniciar(self):
        
        entrada = self.values['entrada']
        old_char = self.values['old_char']
        new_char = self.values['new_char']
        
tela = TelaPrincipal()
tela.Iniciar()