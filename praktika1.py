# atlyginimas = 1500
# atl_ir_priedas = 1500*1.2
# atl_kaledinis = 1500*1.7

# metinis = 0
# kartai = 0
# for i in range(1,12+1):
#     if i%2==0:
#         metinis += atl_ir_priedas
#         kartai+=1
#     else:
#         metinis += atlyginimas

# metinis +=atl_kaledinis
# print(f'prieda gavo {kartai} kartus')
# print(f'metines pajamos: {metinis} eur')


# seka = "-3,9,0,2,4,5,10,-45,7,-3,6,0,8"
# sar1 = seka.split(",")
# sar2 = []
# suma=0

# for i in seka:
#     suma+=int(i)
#     if int(i)<0:
#         sar2.append(i)
#     if len(sar2) == 0:
#         print("Nebuvo neigiamu skaiciu")
#     else:
#         print("neigiami skaiciai sarase: ", sar2)

# print("pradiniai duomenys: ", sar1)
# print("skaiciu suma: ", suma)
    


sk = int(input("iveskite skaiciu nuo 1-7: "))

if sk%2==0 and sk!=6:
    print("darbo laikas: 7:30 – 18:00 val.")
elif sk%2!=0 and sk!=7:
    print("darbo laikas: 9:00 – 20:30 val.")
elif sk==6:
    print("darbo laikas: 11:00 – 13:30 val.")
else:
    print("Sekmadieniais servisas nedirba")





