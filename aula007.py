n1 = float(input('Digite um numero '))
n2 = float(input('digite outro numero '))
nome = input('qual seu nome? ')

print('\nvai tomar no cu {:=^20}'.format(nome))
print('vai tomar no cu {:>20}!'.format(nome))
print('vai tomar no cu {:<20}!\n'.format(nome))


print('soma:{}'.format(n1+n2), end= ' ')
print('subtração:{}'.format(n1-n2))
print('multiplicação:{}'.format(n1*n2))
print('divisão:{:.3f}'.format(n1/n2))
print('pontenciação:{}'.format(n1**n2))
print('divisao inteira:{}'.format(n1//n2))
print('resto:{}'.format(n1%n2))