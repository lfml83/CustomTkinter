# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:37:03 2024

@author: luizf
"""

import customtkinter as ctk

janela= ctk.CTk() # Criar janela

janela.title("App Tste")

janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)


tabview = ctk.CTkTabview(janela, width=400, corner_radius=20, border_width=(2), border_color=("red"),
                         fg_color="teal", segmented_button_fg_color=("red"),segmented_button_selected_color=("green"),
                         segmented_button_unselected_color=("blue"))
tabview.pack()

tabview.add("Nomes")
tabview.add("Idades")
tabview.add("Genero")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)
tabview.tab("Genero").grid_columnconfigure(0, weight=1)

text = ctk.CTkLabel(tabview.tab("Nomes"), text = "Salvador Eduardo\nEugenio Eduardo\nAntonio Tomocene")
text.pack()

idd = ctk.CTkLabel(tabview.tab("Idades"), text = "23\n31\n42")
idd.pack()

gen = ctk.CTkLabel(tabview.tab("Genero"), text = "Masculino\nMasculino\nFeminino")
gen.pack()

janela.mainloop()