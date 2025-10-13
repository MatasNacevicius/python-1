import numpy as np

matrica=np.random.randint(low=-5, high=5, size=(5,5))
print('Matrica:\n',matrica)


ist=[]
for i in range(len(matrica[0,:])):
    ist.append(matrica[i, i])

print('Istrizaine: ',np.array(ist))
print('Istrizaine is kitos puses: ',np.array(ist[::-1]))