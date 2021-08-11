import PySimpleGUI as sg

def replace_func(string, old_char, new_char):
    return string.replace(old_char, new_char)
    
def insert_char_at_end(user_input, char):
    return user_input.replace('\n', f'{char}\n')

def insert_char_at_beginning(user_input, char):
    user_input = char+user_input
    return user_input.replace('\n', f'\n{char}')[:-1]

def alphabetize(user_input):
    words = []
    temp_string = []
    for char in user_input:
        if(char!="\n"):
            temp_string.append(char)
            continue
        words.append(''.join(temp_string))
        temp_string = []
    return '\n'.join(sorted(words))

            


def encrypt():
    pass

def to_binary():
    pass

def errorMessage(char, message):
    if char == '':
        print(f'Erro! Digite um caractere para {message} seu texto!')
        return True
    return False

class TelaPrincipal:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Seu texto')],
            [sg.Multiline(size=(50,6), key='input')],
            [sg.Text('Escolha uma opção abaixo')],
            [sg.Radio('Alfabetizar', 'options', key='alphabetize')],
            [sg.Radio('Substituir', 'options', key='replace')],
            [sg.Text('Antigo termo'), sg.Input(size=(5,0), key='old_char'), sg.Text('Novo termo'), sg.Input(size=(5,0), key='new_char')],
            [sg.Radio('Inserir', 'options', key='insert')],
            [sg.Check('Ao começo', key='insert_at_beginning'), sg.Check('Ao fim', key='insert_at_end'), sg.Input(size=(5,0), key='inserted_char')],
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
            alphabetize_radio = self.values['alphabetize']
            replace = self.values['replace']
            old_char = self.values['old_char']
            new_char = self.values['new_char']
            insert = self.values['insert']
            insert_at_end = self.values['insert_at_end']
            insert_at_beginning = self.values['insert_at_beginning']
            inserted_char = self.values['inserted_char']

            if replace:
                output = replace_func(user_input, old_char, new_char)
                if errorMessage(inserted_char, "substituir no"):
                    continue
                print(output)
            
            if insert:
                if insert_at_end and insert_at_beginning:
                    if errorMessage(inserted_char, "inserir no começo e no fim do"):
                        continue
                    aux = insert_char_at_end(user_input, inserted_char)
                    print(insert_char_at_beginning(aux, inserted_char))
                elif insert_at_end:
                    if errorMessage(inserted_char, "inserir no fim do"):
                        continue
                    print(insert_char_at_end(user_input, inserted_char))
                elif insert_at_beginning:
                    if errorMessage(inserted_char, "inserir no começo do"):
                        continue
                    print(insert_char_at_beginning(user_input, inserted_char))
                
            if alphabetize_radio:
                output = alphabetize(user_input)
                print(output)

            else:
                print('Erro! Tente novamente')

        
tela = TelaPrincipal()
tela.Iniciar()