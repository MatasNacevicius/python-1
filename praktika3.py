import numpy as np

sk=np.random.randint(20)
print(sk)

masyvas=np.random.randint(low=-5, high=5, size=sk)
print(masyvas)

eil = int(input('kiek bus eilucius? '))
stulp = int(input('kiek bus stulpeliu? '))

while eil*stulp!=len(masyvas):
    print("tokios matricos negalima suformuoti")
    eil = int(input('kiek bus eilucius? '))
    stulp = int(input('kiek bus stulpeliu? '))

print(masyvas.reshape(eil,stulp))

unikalios = []
for i in range(len(masyvas)):
    if masyvas[i] not in unikalios:
        unikalios.append(masyvas[i])
print(np.array(unikalios))
