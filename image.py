# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:53:51 2024

@author: luizf
"""

import customtkinter as ctk
from tkinter import * 
from PIL import Image

janela= ctk.CTk() # Criar janela

janela.title("App Teste")
janela.geometry("700x400")

ctk.CTkLabel(janela, text = "Curso Customtkinter Aula 13(imagem)", font=("arial bold",20)).pack(pady=20,padx =5)

img1 = ctk.CTkImage(light_image=Image.open("./youtub.png"),dark_image=Image.open("./youtub.png"), size=(20,20))

ctk.CTkLabel(janela, text=None, image=(img1)).pack()


janela.mainloop()
