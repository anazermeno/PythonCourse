ini = int(input())
fin = int(input())
num = int(input())
cont = 0

for curr in range(ini, fin + 1):
    cont += str(curr).count(str(num))

print(cont)
