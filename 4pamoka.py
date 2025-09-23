# pirma uzduotis

# sk1 = int(input('ivesk pirma skaiciu: '))
# sk2 = int(input('ivesk antra skaiciu: '))

# suma = sk1 + sk2
# print("skaiciu suma =",suma)
# skirtumas = sk1 - sk2
# print("skaiciu skirtumas =",skirtumas)

# if (skirtumas<0):
#     print("skirtumas yra neigiamas")
# elif (skirtumas>0):
#     print("skirtumas yra teigiamas")
# else:
#     print("skirtumas yra lygus nuliui")


# antra uzduotis

# sk1 = int(input('ivesk pirma skaiciu: '))
# sk2 = int(input('ivesk antra skaiciu: '))

# if (sk2==0):
#     quit("dalyba is 0 ne
# galyma")
# else:
#     dalyba = sk1%sk2
#     print("skaiciu dalybos liekana = ",dalyba)


# trecia uzduotis

# sk1 = int(input('ivesk pirma skaiciu: '))
# sk2 = int(input('ivesk antra skaiciu: '))
# sk3 = float(input('ivesk trecia skaiciu: '))

# suma = sk1 + sk2
# print("pirmo ir antro skaiciaus suma = ", suma)
# suma1 = suma * sk3
# print("sumos ir trecio skaiciaus sandauga = ", round(suma1,2))


# ketvirta uzduotis

sk1 = int(input('ivesk pirma skaiciu: '))
sk2 = int(input('ivesk antra skaiciu: '))
sk3 = int(input('ivesk trecia skaiciu: '))
sk4 = int(input('ivesk ketvirta skaiciu: '))
sar = []
sar.append(sk1)
sar.append(sk2)
sar.append(sk3)
sar.append(sk4)
teigsuma = 0
neigsuma = 0

# if(sk1>0):
#     teigsuma+=sk1
# else:
#     neigsuma+=sk1
# if(sk2>0):
#     teigsuma+=sk2
# else:
#     neigsuma+=sk2
# if(sk3>0):
#     teigsuma+=sk3
# else:
#     neigsuma+=sk3
# if(sk4>0):
#     teigsuma+=sk4
# else:
#     neigsuma+=sk4

# print("teigiamu suma: ", teigsuma)
# print("neigiamu suma: ", neigsuma)

for i in range(len(sar)):
    if (sar[i]>0):
        teigsuma+=sar[i]
    else:
        neigsuma+=sar[i]

print("teigiamu suma: ", teigsuma)
print("neigiamu suma: ", neigsuma)