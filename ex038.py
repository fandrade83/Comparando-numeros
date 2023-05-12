n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O \033[1;32m Primeiro\033[m numero é maior!')
elif n2 > n1:
    print('O \033[1;33m Segundo\033[m numero é Maior')
else:
    print('Os numeros são \033[1;34mIGUAIS\033[m! ')
