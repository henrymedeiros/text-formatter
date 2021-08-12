
def alphabetize(user_input):
    if ',' in user_input:
        return ','.join(sorted(user_input.split(',')))
    return '\n'.join(sorted(user_input.split('\n')))
    

teste = "xota,sexo,tenso"
print(alphabetize(teste))