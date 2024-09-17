print('Sequencia de Fibonacci')
n = int(input('Quantos termos você quer mostrar: '))
t1 = 1
t2 = 1
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} ->', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('fim')