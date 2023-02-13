print('Hello, World')
nome = 'Glauber'
class Computador:
    def __init__(self,marca,modelo):
        self.marca = ''
        self.modelo = ''
    def ligar(self):
        print(f'Ligando o {self.marca}modelo {self.modelo}')
computador_1 = Computador('HP','xps')
computador_1.ligar()


