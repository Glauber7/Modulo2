from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento}, tem {idade} anos em {atual}')
if idade == 18:
    print('Voce precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'O prazo de você se alistar não chegou, falta {saldo} anos.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você ja deviria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento teria que ser feito em {ano}.')
