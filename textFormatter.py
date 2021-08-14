import PySimpleGUI as sg

def replace_func(string, old_char, new_char):
    return string.replace(old_char, new_char)
    
def insert_char_at_end(user_input, char):
    return user_input.replace('\n', f'{char}\n')

def insert_char_at_beginning(user_input, char):
    user_input = char+user_input
    return user_input.replace('\n', f'\n{char}')[:-1]

def alphabetize(user_input):
    if ',' in user_input:
        return ','.join(sorted(user_input[:-1].split(',')))
    return '\n'.join(sorted(user_input[:-1].split('\n')))

def changeCase(user_input, case_type):
    if case_type == 'lowercase':
        return user_input[:-1].lower()
    elif case_type == 'uppercase':
        return user_input[:-1].upper()
    elif case_type == 'justified':
        words = user_input[:-1].split(' ')
        new_words = []
        for word in words:
            new_word = list(word)
            new_word[0] = new_word[0].upper()
            new_words.append(''.join(new_word))
        return ' '.join(new_words)
       
        
        


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
            [sg.Radio('Minúscula', 'options', key='lowercase'),sg.Radio('Maiúscula', 'options', key='uppercase'),sg.Radio('Justificado', 'options', key='justified')],
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
            lowercase = self.values['lowercase']
            uppercase = self.values['uppercase']
            justified = self.values['justified']

            if replace:
                output = replace_func(user_input, old_char, new_char)
                if errorMessage(new_char, "substituir no"):
                    continue
                print(output)
            
            elif insert:
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
            elif alphabetize_radio:
                output = alphabetize(user_input)
                print(output)
            elif lowercase:
                print(changeCase(user_input, 'lowercase'))
            elif uppercase:
                print(changeCase(user_input, 'uppercase'))
            elif justified:
                print(changeCase(user_input, 'justified'))
            else:
                print('Erro! Tente novamente')
        
tela = TelaPrincipal()
tela.Iniciar()