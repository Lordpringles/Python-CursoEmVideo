lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[3] = 'picole'
print(lanche)
lanche.append('cookie')
print(lanche)
lanche.insert(0, 'hotdog')
print(lanche)
del lanche[3]
print(lanche)
lanche.pop() #lanche.pop(4)
print(lanche)
lanche.remove('hotdog')
print(lanche)
valores = list(range(4,11))
print(valores)
valor = [9, 8, 3, 6, 5, 7, 2]
valor.sort() #FOREVAAA
print(valor)
valor.sort(reverse=True) #FOREVAAA
print(valor)
print(len(valor))
valores[2] = 12
print(valores)
valores.append(3)
print(valores)
valores.insert(3, 2)
print(valores)
valores.pop(3)
print(valores)
val = list()
for x in range(0, 5):
    val.append(int(input('Digite um valor: ')))
print(val)
a = val # a = val[:] (COPIA DOS VALORES, NAO LIGAÇAO)
a[2] = 8
print(a, '\n',val)