import customtkinter as ctk

janela= ctk.CTk() # Criar janela

janela.title("App Tste")

janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)


def abrir():
    dialog = ctk.CTkInputDialog(title="Caixa de dialogo", text = "Digite o numero do seu celular")
    print(dialog.get_input())
    
btn = ctk.CTkButton(janela, text= "Abrir caixa de dialogo", command=(abrir))
btn.pack()

janela.mainloop()