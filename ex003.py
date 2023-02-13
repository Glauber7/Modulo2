num = int(input('Digite um número inteiro: '))
print('''Escolha uma das base para conversão:
[1] Conveter para BINÀRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} Convertido para BINÁRIO é igual á {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é igual á {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é igual á {}'. format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente Novamente: ')

