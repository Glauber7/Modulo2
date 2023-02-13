n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Entre {n1} e {n2} sua média é {media}.')
if media >=5 and media < 6:
    print('O aluno está de RECUPERAÇÃO!')
elif media >=6 and media < 9:
    print('PARABÉNS APROVADO!')
else:
    print('O aluno está REPROVADO!')
