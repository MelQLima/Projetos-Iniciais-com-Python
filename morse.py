morse_para_alfabeto = {
    '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
    '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
    '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
    '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
    '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
    '--..': 'z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '/': ' '
}


alfabeto_para_morse = {k:v for v,k in morse_para_alfabeto.items()}


def traduzir_para_morse(texto):
    morse = []

    for letra in texto.lower():
        if letra in alfabeto_para_morse:
            morse.append(alfabeto_para_morse[letra])

    return ' '.join(morse)


def traduzir_para_alfabeto(morse):
    palavras = morse.split(' ')
    alfabeto = []

    for palavra in palavras:
        if palavra in morse_para_alfabeto:
            alfabeto.append(morse_para_alfabeto[palavra])

    return ''.join(alfabeto)


def usuario():
    escolha = input('Deseja traduzir para Código Morse ou para Alfábetico? ').lower()

    if escolha == 'codigo morse' or escolha == 'código morse' or escolha == 'morse':
        texto = input('Digite seu texto em Alfábetico aqui:').lower()
        print('Seu texto em Morse é', traduzir_para_morse(texto))

    elif escolha == 'alfabetico' or escolha == 'alfábetico':
        texto = input('Digite seu texto em Morse:').lower()
        print('Seu texto em Alfábetico é', traduzir_para_alfabeto(texto))

    else:
        print('Escolha inválida. Tente Código Morse ou Alfábetico.')


usuario()
