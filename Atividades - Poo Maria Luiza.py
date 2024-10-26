class vendedor ():
    def __init__(self, nome):
     self.nome= nome 
        
vendedor1= vendedor(input('Nome do vendedor:'))
print('Vendedor: ',vendedor1.nome)        

class pessoa():
 def __init__(self,nome, sobrenome,idade, cidade):
     self.nome = nome
     self.sobrenome= sobrenome
     self.idade= idade
     self.cidade= cidade
     
nome_inp = input('Qual o seu nome? ')
sobrenome_inp=input("Qual o seu sobrenome? ")
idade_inp = int(input("Qual a sua idade? "))
cidade_inp= input('Qual sua cidade? ')

pessoa= pessoa(nome_inp, sobrenome_inp, idade_inp, cidade_inp)
print(f"\nome:{pessoa.nome}\nsobrenome: {pessoa.sobrenome}\nidade: {pessoa.idade}\ncidade:{pessoa.cidade}")

#////////////////////////////////////////////////////////////////////////
#EX1 resolvido de outra maneira
class vendedor:
  def __init__(self,nome, nome2):
      self.nome=nome
      self.nome = nome2
         
def informaCAOSAIDA(self):
    print(f"Olá, meu nome é", self.nome, "e eu tenho")

vendedor1= vendedor(input('Nome 1'),input('Sobrenome 2'))
vendedor2= vendedor(input('Nome 2'),None)

vendedor1.informacaoSaida()
vendedor2.informacaoSaida()
     
#ex2/////////////////////////////////////////////////////////////////////////////////////////////////////

     

