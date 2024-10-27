

import customtkinter as ctk
from tkinter import * 


janela= ctk.CTk() # Criar janela

janela.title("App Teste")
janela.geometry("700x400")

ctk.CTkLabel(janela, text = "Curso Customtkinter Aula 10", font=("arial bold",20)).pack(pady=20,padx =5)


entry = ctk.CTkEntry(janela, width=300,placeholder_text=("Digite o seu nome completo..."))

entry.pack(pady=20)

def pegar():
    print(entry.get())
    entry.delete(0, END)
    pass



ctk.CTkButton(janela, width=300, text = "Pegar texto", command=pegar).pack()
#ctk.CTkButton(janela, width=300, text = "Apagar texto", command=apagar).pack(pady=5)
janela.mainloop()
