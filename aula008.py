from math import sqrt
import random
import emoji

n = float(input('digite um numero '))
r = sqrt(n)
print('a raiz de {} é igual a {:.3f}'.format(n, r))

m = random.randint(1,100)
print('numero aleatorio: {}'.format(m))

print(emoji.emojize('olá, mundo :earth_americas: ', use_aliases=True))