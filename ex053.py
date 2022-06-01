nome = input('Digite uma frase: ').upper().strip()
frase = nome.split()
junta = "".join(frase)
inverso = ''
for i in range(len(junta) - 1, -1, -1):
    print(junta[i], end="")
    inverso += junta[i]
print(f'O inverso de {junta} é {inverso}')
if inverso == junta:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')

# O for pode ser substituido pelo fatiamento de strings:
# inverso = junta[::-1]
