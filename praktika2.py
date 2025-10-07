s1=['augame', 45,-7, 'mes', 2,8,0, 'kliūtis,', 9]
s2=[ 'įveikę' ,-12,-9, 'bet,', 'pradėti,', 3,81, 'kažko']
s3=[-7,-3,0, 'nuo', 9,4, 'Sunku',12]

sk=[]
txt=[]

for i in s1:
    if type(i)==int:
        sk.append(i)
    else:
        txt.append(i)
for i in s2:
    if type(i)==int:
        sk.append(i)
    else:
        txt.append(i)
for i in s3:
    if type(i)==int:
        sk.append(i)
    else:
        txt.append(i)
print('skaiciu sarasas: ', sk)
print('teksto sarasas', txt)
print(f'skaiciu saraso vidurkis: {sum(sk)/len(sk):1.2f} ')
print(f'\nSarasas is kitos puses: {txt[::-1]}')
print(f'Sarasas apjungtas i sakini: {" ".join(txt[::-1])}')
