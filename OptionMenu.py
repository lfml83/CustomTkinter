# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 16:49:00 2024

@author: luizf
"""

import customtkinter as ctk

janela= ctk.CTk() # Criar janela

janela.title("App Teste")
janela.geometry("700x400")

ctk.CTkLabel(janela, text = "Menu de opções - 09", font=("arial bold",20)).pack(pady=20,padx =5)

ctk.CTkLabel(janela, text= "Escolha o seu mês de nascimento: ", font=("arial bold", 14)).pack()


mes_var=ctk.StringVar(value="Escolha o mes")

def mes_nascimento(escolha):
    print(f"O seu mes de nascimento: {escolha}")

mes=ctk.CTkOptionMenu(janela, 
                  values=(["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Outros"]),
                  command=mes_nascimento,
                  variable=mes_var, width=250,height=50)

mes.pack(pady=10)








"""
mes=ctk.CTkOptionMenu(janela, 
                  values=(["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Outros"]),
                  command=mes_nascimento)

mes.pack(pady=10)
mes.set("Escolha o Mês")

"""

janela.mainloop()