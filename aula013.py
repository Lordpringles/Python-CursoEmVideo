escolha = int(input('''Voce quer contar em ordem crescente ou decrescente?
Digite 1 para crescente
Digite 2 para decrescente'''))
if escolha == 1:
    for x in range(1,101):
        print (x)
        if x == 90:
            print('Chegamos a 90%')
if escolha == 2:
    for c in range (100, 0, -1):
        print(c)
        if c == 10:
            print('chegamos a 90%')