from clrprint import *
import random
import os

def Capitulo_1():
    capitulo = open('C1.txt', encoding='utf-8', mode='r')

    print(capitulo.read())
    
    escolha = 1
        
    while escolha != '24' and escolha != '47':
        escolha = input("Escolha >> ")
            
    if escolha == '24':
        Capitulo_24()
    elif escolha == '47':
        Capitulo_47()
    
    
def Capitulo_24():
    os.system('cls')
    capitulo = open('C24.txt', encoding='utf-8', mode='r')

    print(capitulo.read())
    
    escolha = 1
        
    while escolha != '70' and escolha != '47':
        escolha = input("Escolha >> ")
            
    if escolha == '70':
        Capitulo_70()
    elif escolha == '47':
        Capitulo_47() 
    
    
def Capitulo_47():
    os.system('cls')
    capitulo = open('C47.txt', encoding='utf-8', mode='r')

    print(capitulo.read())
    
    escolha = 1
        
    while escolha != '70' and escolha != '24':
        escolha = input("Escolha >> ")
            
    if escolha == '70':
        Capitulo_70()
    elif escolha == '24':
        Capitulo_24() 
     

def Capitulo_70():
    print("Em preparação")

    

    
    
Capitulo_1()
#Capitulo_47()
