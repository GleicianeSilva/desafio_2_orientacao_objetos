'''

1. O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres. Modele um sistema orientado a objetos para representar contas
correntes do Banco Delas seguindo os requisitos abaixo.

● Cada conta corrente pode ter um ou mais clientes como titular.
● O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
● A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
● Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela fizer um depósito, aumentaremos o saldo.
● Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até renda_mensal.
● Clientes homens por enquanto não têm direito a cheque especial. Para modelar seu sistema, utilize obrigatoriamente os conceitos

"classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".

'''

class Cliente:

    def __init__(self, nome, telefone, renda):
      self.nome = nome
      self.telefone = telefone
      self.renda_mensal = renda
      self.saldo = 0.0

    def sacar(self): 
       
       while True:
        
        print('\n------------------------------------>SACAR<------------------------------------')
        

        cliente  = int(input('\nQual conta corrente deseja sacar => 1 - Cliente Mulher e 2 - Cliente Homem: '))
    
        if cliente == 1:
            valor = float(input("\nQuanto deseja sacar: R$"))
            if valor <= self.saldo or (self.saldo - valor) >= self.renda_mensal:
                self.saldo -=valor
                print(f'\n{self.nome}, o seu saque foi no valor de R$:{valor}. \n\nSaldo da Conta Corrente: R${self.saldo}. Renda Mensal: R${self.renda_mensal}')
            else:
                  raise ValueError(f'\n{self.nome}, você não tem saldo suficiente para realizar o saque.')
            
            
            operacao = int(input('\nDeseja realizar mais algum saque => 1(sim) ou 2(não): '))

            if operacao == 1:
               valor = float(input("\nQuanto deseja sacar: R$"))
               if valor <= self.saldo + self.renda_mensal:
                  self.saldo -=valor
                  return print(f'\n{self.nome}, o seu saque foi no valor de R$:{valor}. \n\nSaldo da Conta Corrente: R${self.saldo}. Renda Mensal: R${self.renda_mensal}')
               else:
                  raise ValueError(f'\n{self.nome}, você não tem saldo suficiente para realizar o saque.')
            else:
               return print(f'\n{self.nome}, o seu saque foi no valor de R$:{valor}. \n\nSaldo da Conta Corrente: R${self.saldo}')

                   
        elif cliente == 2:
               valor = float(input("\nQuanto deseja sacar: R$"))
               if valor <= self.saldo:
                   self.saldo -=valor
                   print(f'\n{self.nome}, o seu saque foi no valor de R$:{valor}. \n\nSaldo da Conta Corrente: R${self.saldo}. Renda Mensal: R${self.renda_mensal}')
               else:
                   raise ValueError(f'\n{self.nome}, você não tem saldo suficiente para realizar o saque.')


               operacao = int(input('\nDeseja realizar mais algum saque => 1(sim) ou 2(não): '))

               if operacao == 1:
                  valor = float(input("\nQuanto deseja sacar: R$"))
                  if valor <= self.saldo + self.renda_mensal:
                     self.saldo -=valor
                     return print(f'\n{self.nome}, o seu saque foi no valor de R$:{valor}. \n\nSaldo da Conta Corrente: R${self.saldo}. Renda Mensal: R${self.renda_mensal}')
                  else:
                     raise ValueError(f'\n{self.nome}, você não tem saldo suficiente para realizar o saque.')
               else:
                  return print(f'\n{self.nome}, o seu saque foi no valor de R$:{valor}. \n\nSaldo da Conta Corrente: R${self.saldo}. Renda Mensal: R${self.renda_mensal}')       

        else:
            raise ValueError('\nOpção incorreta! Tente novamente.') 
      

    def depositar(self):   
       
        print('\n------------------------------------>DEPOSITAR<------------------------------------')
        
        cliente  = int(input('\nQual conta corrente deseja depositar => 1 - Cliente Mulher e 2 - Cliente Homem: '))
    
        if cliente == 1:
           valor = float(input("\nQuanto deseja depositar: R$"))
           self.saldo +=valor
           print(f'\n{self.nome}, seu deposito foi no valor de: R${valor}. \n\nSaldo da Conta Corrente: R${self.saldo}. Renda Mensal: R${self.renda_mensal}')
           print('\n')
        
           operacao = int(input('\nDeseja realizar mais algum deposito => 1(sim) ou 2(não): '))

           if operacao == 1:
              
              valor = float(input("\nQuanto deseja depositar: R$"))
              self.saldo +=valor
              print(f'\n{self.nome}, seu novo deposito foi no valor de: R${valor}. \n\nSaldo da Conta Corrente: R${self.saldo}. Renda Mensal: R${self.renda_mensal}')
              print('\n')
           
        elif cliente == 2:
           valor = float(input("\nQuanto deseja depositar: R$"))
           self.saldo +=valor
           print(f'\n{self.nome}, seu novo deposito foi no valor de: R${valor}. \nSaldo da Conta Corrente: R${self.saldo}. Renda Mensal: R${self.renda_mensal}')
           print('\n')

           operacao = int(input('\nDeseja realizar mais algum deposito => 1(sim) ou 2(não): '))

           if operacao == 1:
              
              valor = float(input("\nQuanto deseja depositar: R$"))
              self.saldo +=valor
              print(f'\n{self.nome}, seu novo deposito foi no valor de: R${valor}. \n\nSaldo da Conta Corrente: R${self.saldo}. Renda Mensal: R${self.renda_mensal}')
              print('\n')
                   
        else:
            raise ValueError('\nOpção incorreta! Tente novamente.')

   
cliente_mulher = Cliente('Maria', '8199999-9999', 3000.00)
cliente_homem = Cliente('Luiz', '8199999-9999', 5000.00)


cliente_mulher.depositar()
cliente_mulher.sacar()


cliente_homem.depositar()
cliente_homem.sacar()

