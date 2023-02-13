casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salario do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('O valor da parcela será de R${:.2f}.'.format(parcela))
if parcela <= minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Emrpréstimo NEGADO!')
