# TUPLAS SAO IMUTAVEIS

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[1])
for x in lanche:
    print(x)

print(lanche[-2])
print(lanche[2:])

for c in range(0, len(lanche)):
    print(c, lanche[c])

for p, v in enumerate(lanche):
    print(p, ' ',v)

print(sorted(lanche))

a = (2, 5, 3)
b = (5, 8, 1, 2)
c = a + b
print(a)
print(b)
print(c)
print(sorted(a+b))
print(a+b, b+a)
print(c.count(3))
print(c.index(2))
print(c.index(2, 1))