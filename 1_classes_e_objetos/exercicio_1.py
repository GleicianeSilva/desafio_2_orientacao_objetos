'''
1. Crie uma classe que modele o objeto "carro".
2. Um carro tem os seguintes atributos: ligado, cor, modelo,
velocidade.
3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
desacelera.
4. Crie uma instância da classe carro.
5. Faça o carro "andar" utilizando os métodos da sua classe.
6. Faça o carro "parar" utilizando os métodos da sua classe.
'''

class Carro:   
    def __init__(self): 
        self.ligada = False
        self.cor = 'Cinza'
        self.modelo = 'Toyota'
        self.velocidade = 0

    def ligar(self):
        if not self.ligada :
            self.ligada = True
            print(f'A {self.modelo}({self.cor}) está ligada.') 
        else:
            print(f'ERRO: A {self.modelo}({self.cor}) já se encontra ligada.') 
              
    def desligar(self):   
        if self.ligada:
            self.ligada = False 
            self.velocidade = 0
            print(f'A {self.modelo}({self.cor}) está desligado.')     
        else:
            print(f'ERRO: A {self.modelo}({self.cor}) já se encontra desligada.')       

    
    def acelerar(self,velocidade):
        if self.ligada:
            self.velocidade+=velocidade
            print(f'A {self.modelo}({self.cor}) está acelerado com velocidade de: {self.velocidade}km/h')
        else:
            print(f'ERRO: A {self.modelo}({self.cor}) encontrar desligada. Impossível acelerar.')
    
    def desacelerar(self,velocidade):
        if self.ligada>0:
            self.velocidade-=velocidade
            if self.velocidade < 0:
                self.velocidade = 0
            print(f'A {self.modelo}({self.cor}) está desacelerado com velocidade de: {self.velocidade}km/h')
    
        else:
            print(f'ERRO: A {self.modelo}({self.cor}) encontrar desligada. Impossível desacelerar.')

automovel = Carro()
automovel.ligar()
automovel.acelerar(50)
automovel.desacelerar(20)
automovel.desligar()


