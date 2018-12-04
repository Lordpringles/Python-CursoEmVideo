x = 0
while x < 10:
    x += 1
    print(x)

a = 1
par = imp = 0
while a != 0:
    a = int(input('Digite um valor: '))
    if n != 0:
        if a %2 == 0:
            par += 1
        else:
            imp += 1
print('Voce digitou {} numeros impares e {} numeros pares'.format(imp, par))

b = 's'
while b == 's':
    n = int(input('Digite um valor: '))
    b = str(input('Deseja continuar? [S/N]')).strip().lower()