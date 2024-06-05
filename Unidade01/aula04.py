# Exercicio 01

def Metodo(self):
atual = self.inicio
self.inicio = atual.proximo

# Exercicio 02
def Metodo(self):
atual = self.inicio

if self.inicio == None:
    print("none")
else: 
   while atual != None:
            print(atual)
            atual = atual.proximo
            
# Exercicio 03
def Metodo(Lista):
    if Lista.inicio == None :
       return  True
    else:
       return False