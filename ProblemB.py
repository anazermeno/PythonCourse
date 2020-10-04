
ini = int(input())
fin = int(input())
num = int(input())

prov = str(num)
cont = 0
while ini <= fin:
    prov2 = str(ini) + 'a'

    for i in range(len(prov2)):
        if prov2[i] == prov:
            cont += 1
    ini += 1
print(cont)
