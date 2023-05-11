import random

sorte = 12


def teste_sorte(sorte):
    dados = random.randint(1,12)
    if dados <=  sorte:
        print("A sorte está do teu lado.")
        sorte -= 1
    elif dados > sorte:
        print("Desta vez tiveste azar.")
    print(sorte)
   


teste_sorte(sorte)
   
print(sorte)    
    
"""dados = random.randint(1,12)
if dados <=  sorte:
    print("A sorte está do teu lado.")
    sorte -= 1
elif dados > sorte:
        print("Desta vez tiveste azar.")
print(sorte)        """