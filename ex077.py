palavras = (
    'CURSO', 'PYTHON',
    'PROGRAMAR', 'JAVASCRIPT',
    'HTML', 'CSS', 'AWS',
    'BANCO DE DADOS',
)

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end="")
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end=" ")
