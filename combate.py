from clrprint import *
import random
import os




#pericia lançar um dado e somar 6
#força lançar dois dados e somar 12
#sorte lançar um dado e somar 6

#variaveis do jogador

  
pericia = random.randint(1,12) + 6
forca = random.randint(1,12) + 12
sorte = random.randint(1,12) + 6


#variáveis do inimigo
pericia_foe = 9
forca_foe = 9
sorte_foe = 12

#Esta variavel indica se é possível fugir do combate.
fuga = False

        
#função de combate.        

def combate(pericia, forca, sorte, pericia_foe, forca_foe, sorte_foe, fuga):
    while forca > 0 and forca_foe > 0:
    
        """Esta variavel pretende informar quem fez o ultimo hit, para poder desbloquear o teste de sorte correcto
         Se o valor dela for 0, o ulimo hit foi do inimigo no jogador. Se o valor dela for 1, o ultimo hit foi do jogador no inimigo"""
         
        last_hit = None
        global forca_global
        global sorte_global
        
        forca_global = forca
        sorte_global = sorte
        
        
        #Esta secção do código mostra as stats do jogador e do inimigo.
        print(f"Perícia Jogador = {pericia}."+7*" "+f"Perícia Inimigo = {pericia_foe}.")
        print(f"Força Jogador = {forca}"+10*" "+f"Força Inimigo = {forca_foe}.")
        print(f"Sorte Jogador = {sorte}"+10*" "+f"Sorte Inimigo = {sorte_foe}.\n")

        dados = random.randint(1,12)
        dados = random.randint(1,12)
        ataque_inimigo = pericia_foe + dados
        clrprint(f"O inimigo lançou os dados. O PODER DE ATAQUE DO INIMIGO É {ataque_inimigo}", clr='g')
        dados = random.randint(1,12)
        ataque_jogador = pericia + dados
        clrprint(f"Lançaste os dados."+9*" "+f"O TEU PODER DE ATAQUE É {ataque_jogador}.\n", clr='g')
    
        if ataque_jogador > ataque_inimigo:
            clrprint("FERISTE O INIMIGO.\n", clr='r')
            forca_foe -= 2
            last_hit = 1
        if ataque_jogador < ataque_inimigo:
            clrprint("FOSTE FERIDO PELO INIMIGO\n", clr='r')
            forca -= 2
            last_hit = 0
        if ataque_jogador == ataque_inimigo:
            clrprint("Conseguiram desviar-se mutuamente dos ataques.\n", clr='g')
        
        # este segmento de código impede que sejam mostrados os resultados caso o inimigo já tenha sido derrotado.        
        if forca_foe >= 0:
            print(f"O jogador tem agora {forca} força.")
            print(f"O inimigo tem agora {forca_foe} força.")
            
        
    
        if forca_foe <= 0:
            print("Parabéns jogador, ganhaste o combate.")
        elif forca <= 0:
            print("Lamento, jogador, foste morto neste combate.")
        else:
            
            #este segmento do código pretende dar a opção ao jogador de continuar, testar a sorte ou tentar a fuga.
            print("Queres continuar o combate? > \n")
            print("Continuar. [ENTER]")
            print("Testar sorte. [s]")
            print("Tentar fugir. [f]")
            
            
            
            cont = input(">")
            os.system('cls')
            #se for para continuar, basta carregar em qualquer tecla, mas à partida será o enter.
            if cont == 's':
                #esta secção do código divide o teste de sorte em sorte para aumentar dano no inimigo, ou sorte para reduzir o dano ao jogador.
                
                if last_hit == 1:
                    #tentativa de aumentar dano no inimigo.
                    dados = random.randint(1,12)
                    if dados <= sorte:
                        print(f"Tiveste sorte. O teu inimigo sofre +2 dano na força")
                        sorte -= 1
                        forca_foe -=2 
                        os.system('pause')
                        os.system('cls')
                    else:
                        print(f"Tiveste azar. O teu inimigo sofre apenas 1 dano na força.")
                        sorte -= 1
                        forca_foe += 1
                        os.system('pause')
                        os.system('cls')    
                        
                if last_hit == 0:
                    #tentiva de reduzir dano no jogador.
                    dados = random.randint(1,12)
                    if dados <= sorte:
                        print(f"Tiveste sorte. O inimigo apenas te atingiu de raspão, sofres apenas 1 dano na força.")
                        sorte -= 1
                        forca += 1
                        os.system('pause')
                        os.system('cls')
                    else:
                        print(f"Tiveste azar. Sofreste um ferimento profundo. Recebes +1 ponto de dano na tua força.")
                        sorte -=1
                        forca -=1
                        os.system('pause')
                        os.system('cls')
                                
                        
                                           
            elif cont == 'f':
                    if fuga == True:
                        print("Conseguiste fugir, mas sofreste um dano de 2 pontos.")
                        #return forca_global
                        #return sorte_global
                         
                    if fuga == False:
                        print("Não é possível fugir! Tens de lutar!")
                        
    return forca, sorte        
    
    
    
                          
            
forca,sorte = combate(pericia, forca, sorte, pericia_foe, forca_foe, sorte_foe, fuga)
          
        
        
            
"""Este segmento do código iguala a variavel global, com a força e sorte do jogador no final do combate criada no interior do motor de combate na variavel força que é
#a variavel que utilizamos durante o combate."""

#forca = forca_global
#sorte = sorte_global  
          
print(f"{forca}")
print(f"{sorte}")





