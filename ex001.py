nome = str(input('Qual é o seu nome? ')).upper()
if nome == 'Glauber':
    print('Que nome Lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João' or nome == 'José':
    print('Seu nome é bem popular aqui no brasil.')
elif nome in 'Ana Flavia Antonia':
    print('Esses nomes tem a característica feminina.')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom Dia, {nome}')