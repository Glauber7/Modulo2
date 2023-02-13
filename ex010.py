from colorama import Fore
print('{:=^40}'.format(' GBR PRODUTOS '))
preco = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTOS
[ 1 ] À vista/pix
[ 2 ] cartão débito
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais parcelas''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(Fore.BLUE + 'Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela, total))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(Fore.BLUE + 'Sua compra será parcelado em {}x de R${:.2f} COM JUROS!'.format(totalparc, parcela))
else:
    total = preco
    print(Fore.RED + 'Opção inválida, tente novamente nas opçôes a cima:')
print(Fore.BLUE + 'Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(preco, total))

