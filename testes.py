
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
    

teste = "xota\nsexo\nmesa\n"
print(alphabetize(teste))