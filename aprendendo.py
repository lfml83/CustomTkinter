# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:04:42 2024

@author: luizf
"""





class Pessoa():
    
    def __init__(self, nome, idade, comendo = False, falando= False):
        
        self.nome = nome
        self.idade = idade
        self.comendo=comendo
        self.falando=falando
        
    def comer(self, alimento):
        
        if self.comendo:
            print(f'{self.nome} ja esta comendo')
            return
           
        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True
        
    
        

p1 = Pessoa('Luiz',30)
p1.comer('maça')       
p1.comer('maça')