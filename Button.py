# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:17:16 2024

@author: luizf
"""

import customtkinter as ctk
from tkinter import * 
from PIL import Image

janela= ctk.CTk() # Criar janela

janela.title("App Teste")
janela.geometry("700x400")

ctk.CTkLabel(janela, text = "Curso Customtkinter Aula 12(button)", font=("arial bold",20)).pack(pady=20,padx =5)


img=ctk.CTkImage(light_image=Image.open("./youtub.png"),dark_image=Image.open("./youtub.png"), size=(20,20))

def evento():
    pass



ctk.CTkButton(janela, text="Youtube",command=evento,
              width=200
              ,height=70
              ,fg_color=("transparent")
              ,text_color=("red")
              ,hover_color=("green")
              ,font=("arial bold",18)
              ,border_color=("white")
              ,border_width=3
              ,border_spacing=20
              ,corner_radius=20
              ,state="normal"
              ,image=img).pack(pady=30)
janela.mainloop()
