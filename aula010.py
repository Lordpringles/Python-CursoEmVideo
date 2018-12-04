n1 = float(input('nota da primeira prova: '))
n2 = float(input('nota da segunda prova: '))
m = (n1 + n2) / 2
print('Sua media foi {:.2f}'.format(m))
if (m >= 6):
    print('foi uma media boa, parabens!')
else:
    print('foi uma media ruim, estude mais!')
