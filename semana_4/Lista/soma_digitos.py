num = str(input('Digite um numero inteiro: '))
a = 0
total = 0
while len(num) > a:
    total += int(num[a])
    a += 1
print(total)