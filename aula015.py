from time import sleep
n = s = 0
while True:
    n = int(input('Digite um numero '))
    if n == 999:
         break
    s += n
# print('A soma dos numeros e igual a {}'.format(s))
print(f'A soma vale {s}')