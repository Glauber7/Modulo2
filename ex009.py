from colorama import Fore

peso = float(input('Qual é o seu peso?(Kg) '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if 18.5 <= imc < 25:
    print(Fore.BLUE + 'Seu peso está normal.')
elif imc < 18:
    print(Fore.YELLOW + 'Você está abaixo do peso.')
elif 25 <= imc < 30:
    print(Fore.GREEN + ' Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print(Fore.ORANGE + 'Está com OBESIDADE CUIDADO Você precisa emagracer!')
elif 40 <= imc > 40:
    print(Fore.RED + 'Você está com OBESIDADE MÓRBIDA CUIDADO! Você necessita de cirurgia urgente!')
