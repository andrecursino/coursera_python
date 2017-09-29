lista = []
nume = True
while nume == True:
    num = int(input('Digite um número: '))
    if num != 0:
        lista.append(num)
    else:
        nume = False

for n in lista[::-1]:
    print(n)