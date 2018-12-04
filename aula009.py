print('''Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String, 
Análise com len(), count(), find(), transformações com replace(), upper(), lower(), 
capitalize(), title(), strip(), junção com join().''')

frase = 'Meu melhor amigo de escola e um MACACO'
frase2 = '     espacos inuteis       '
split = frase.split()

print(len(frase))

print(frase[:7])
print(frase[15:])
print(frase[2:29:2])

print(frase.count('e'))
print(frase.count('e',0, 19))

print(frase.find('escola'))

print('melhor' in frase)

frase = frase.replace('MACACO', 'Android')
print(frase)

print(frase.capitalize())
print(frase.title())
print(frase.upper())
print(frase.lower())

print(frase2.strip())
print(frase2.lstrip())
print(frase2.rstrip())

print(split)
print(len(split))
print(split[4][1:5])
print('-'.join(split))