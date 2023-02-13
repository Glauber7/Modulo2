from colorama import Fore
print('{:=^40}'.format(' CONTAGEM REGRESSIVA! '))
from time import sleep
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print(Fore.BLUE +'FELIZ ANO NOVO!!!')
