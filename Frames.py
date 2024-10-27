# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:34:04 2024

@author: luizf
"""

import customtkinter as ctk

janela= ctk.CTk() # Criar janela

janela.title("App Tste")

janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)


frame1 = ctk.CTkFrame(master=janela,width=200, height=330,fg_color="teal", bg_color="red", border_width = 10, corner_radius=30).place(x=10,y=60)
frame2 = ctk.CTkFrame(master=janela,width=200, height=330).place(x=230,y=60)
frame3 = ctk.CTkFrame(master=janela,width=200, height=330).place(x=450,y=60)
janela.mainloop()