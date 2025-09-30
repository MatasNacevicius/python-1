import random
import numpy as np
# 1pav


# sar1= [-9,7,0,10,45,-9,-3,20,45]
# sar2 = [-12,4,5,7,10,-9,0,5,6,3,2,10]
# sar=[]
# for i in range(0,len(sar1),2):
#     sar.append(sar1[i])
# for i in range(0,len(sar2),3):
#     sar.append(sar2[i])
# print(sar)


# 2pav

# sar1= [-9,7,0,10,45,-9,-3,20,45]
# sar2 = [-12,4,5,7,10,-9,0,5,6,3,2,10]
# sar1.extend(sar2)
# # arba
# for i in range(len(sar2)):
#     sar1.append(sar2[i])

# print(sar1)


# 3pav

# sar1=[-6,-5,-4,-3]
# sar2=[1,2,3,4,5,6]
# sar=[]

# for i in range(3):
#     sar.append(sar2[i])

# sar.extend(sar1)

# for i in range(3,len(sar2)):
#     sar.append(sar2[i])

# print(sar)


# 4pav

# mas=[]
# el=int(input('Kiek sarase elementu? '))
# if el>0:
#     for i in range(0,el):
#         a=int(input('Ivesk elementa: '))
#         mas.append(a)
#     print(mas)
# else:
#     print("Sarasas gali buti sudaromas tik is teigiamo skaiciaus elementu")


# 5pav

# mas=[]
# el=int(input('Kiek sarase elementu? '))
# while el<=0:
#     el=int(input('Iveskite teigiama saraso elementu skaiciu: '))
# for i in range(el):
#     a=int(input('Ivesk elementa: '))
#     mas.append(a)
# print(mas)


# 5pav

# masA=np.random.randint(50,size=10)
# print('A masyvas: ',masA)
# print("Didziausia reiksme: ", masA.max())
# print("Maziausa reiksme: ", masA.min())


# 6pav

# el=int(input('Kiek masyve elementu? '))
# nuo=int(input('Maziausia galima reiksme? '))
# iki=int(input('Didziausia galima reiksme? '))

# masA=np.random.randint(low=nuo, high=iki, size=el)
# print('A masyvas: ',masA)
# print("Didziausia reiksme: ", masA.max())
# print("Maziausa reiksme: ", masA.min())


# 7pav

# el=np.random.randint(10)

# masA=np.random.randint(10, size=el)
# print("A masyvas: ", masA)
# print("Masyvo elementu skaicius: ", len(masA))


# 8pav

# el=np.random.randint(-5,10)
# if el>0:
#     masA=np.random.randint(10,size=el)
#     print("A masyvas: ", masA)
#     print("Masyvo elementu skaicius: ", len(masA))
# else:
#     print("Sugeneruotas skaicius: ", el)
#     quit("Masyvo sugeneruoti is tokio skaiciaus negalima")


# 9pav

# el=int(input('Kiek elementu sudaro masyva?'))
# mas=np.random.randint(low=-12, high=15, size=el)
# print("Masyvas: ",mas)
# eil=int(input('Kiek formuojamoje matricoje eiluciu? '))
# stulp=int(input('Kiek formuojamoje matrioje stulpeliu? '))
# if eil*stulp==el:
#     matr=mas.reshape(eil,stulp)
#     print("Matrica\n", matr)
# else:
#     quit("Tokios matricos sudaryti negalima")


# 10pav

el=np.random.randint(20)
mas=np.random.randint(low=-12, high=15, size=el)
print("Masyvas: ",mas)
print("Jo elementu skaicius: ", el)
eil=int(input('Kiek formuojamoje matricoje eiluciu? '))
stulp=int(input('Kiek formuojamoje matrioje stulpeliu? '))
if eil*stulp==el:
    matr=mas.reshape(eil,stulp)
    print("Matrica\n", matr)
else:
    quit("Tokios matricos sudaryti negalima")