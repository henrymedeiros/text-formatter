import PySimpleGUI as sg

def replace_func(string, old_char, new_char):
    return string.replace(old_char, new_char)
    
def insert_char_at_end(user_input, char):
    return user_input.replace('\n', f'{char}\n')

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
            [sg.Radio('Inserir no fim', 'options', key='insert_at_end'), sg.Input(size=(5,0), key='at_end')],
            [sg.Button('Processar')],
            [sg.Text('Saída')],
            [sg.Output(size=(50,6))]
            
            
        ]
        #Janela
        self.janela = sg.Window('Super Text Formatter').layout(layout)
      
        #Extrair
        
    def Iniciar(self):
        while True:                             # The Event Loop
            self.button, self.values = self.janela.Read()
            user_input = self.values['input']
            replace = self.values['replace']
            old_char = self.values['old_char']
            new_char = self.values['new_char']
            insert_at_end = self.values['insert_at_end']
            at_end = self.values['at_end']


            if replace:
                output = replace_func(user_input, old_char, new_char)
                print(output)
            elif insert_at_end:
                if at_end == '':
                    print('Erro! Digite um caractere para inserir ao fim do seu texto!')
                    continue
                print(insert_char_at_end(user_input, at_end))
            else:
                print('Erro! Tente novamente')

        


        
tela = TelaPrincipal()
tela.Iniciar()