# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:43:40 2024

@author: luizf
"""

import customtkinter as ctk

janela= ctk.CTk() # Criar janela

janela.title("App Teste")
janela.geometry("700x400")

ctk.CTkLabel(janela, text = "Curso Customtkinter Aula 10", font=("arial bold",20)).pack(pady=20,padx =5)

ctk.CTkLabel(janela, text = "Este texto é de uma label estatico").pack()


#2 forma: introduduzindo texto por entry(forma mais pratica)
def enviar():
    lab.configure(text=str(entry.get()))

lab = ctk.CTkLabel(janela, text="", width=200, height=25,text_color=("red"),
                   font=("arial bold",16))

lab.pack(pady=10)

entry = ctk.CTkEntry(janela, width=200)
  
entry.pack()

ctk.CTkButton(janela,text="Enviar", width=200, command=(enviar)).pack(pady=10)

janela.mainloop()


#Label de forma dinamica
#1 forma: introduzindo texto por inputs
"""
text_var = ctk.5340
(value=input("Digite seu nome completo"))
lab = ctk.CTkLabel(janela, textvariable=text_var, width=200, height=25,text_color=("red"),
                   font=("arial bold",16))

lab.pack(pady=10)
"""