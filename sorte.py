import random
import os


pericia = random.randint(1,12) + 6
forca = random.randint(1,12) + 12
sorte = random.randint(1,12) + 6

pericia_foe = 9
forca_foe = 9
sorte_foe = 12

def sorte_combate_ofensivo(luck, strength):

    print(f"Sorte inicial: {sorte}")
    print(f"força do inimigo inicial: {forca_foe}")
    dados = random.randint(1,12)
    
    if dados <= sorte:
        print(f"Tiveste sorte. O teu inimigo sofre +2 dano na força")
        sorte -= 1
        forca_foe -=2
    else:
        print(f"Tiveste azar. O teu inimigo sofre apenas 1 dano na força.")
        sorte -= 1
        forca_foe += 1
        
        
        
sorte_combate_ofensivo(sorte, forca_foe)   
     

print(f"Sorte final:{sorte}")
print(f"Força do inimigo final: {forca_foe}")
