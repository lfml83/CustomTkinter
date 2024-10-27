# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 21:25:11 2024

@author: luizf
"""

import customtkinter as ctk

janela= ctk.CTk() # Criar janela

janela.title("App Tste")

janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)

janela._set_appearance_mode("dark")


def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry("500x250")

btn_novatela = ctk.CTkButton(master = janela, text="Abrir nova janela",command=nova_tela).place(x=300, y=100)

janela.mainloop()