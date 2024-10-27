

import customtkinter as ctk

janela= ctk.CTk() # Criar janela

janela.title("App Tste")

janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)



textbox =ctk.CTkTextbox(janela, width=300, height=350, scrollbar_button_color=("green"), scrollbar_button_hover_color="red")
textbox.pack()

textbox.insert("0.0", "Titulo do seu texto" + "ola dev, estou aqui programando interfaces graficas com customtkinter no canal set.\n\n"*20)

janela.mainloop()