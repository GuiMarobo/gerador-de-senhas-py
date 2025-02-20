# senha_gui.py

import tkinter as tk
from tkinter import messagebox
from senha_logica import gerar_senha #importa a função gerar_senha do arquivo senha_logica.py

def gerar_senha_gui():
    senha_gerada = gerar_senha(
        usar_maiusculas.get(),
        usar_minusculas.get(),
        usar_numeros.get(),
        usar_simbolos.get()
    )

    if senha_gerada is None:
        messagebox.showwarning("Erro", "Selecione pelo menos uma opção para gerar sua senha.")
    else:
        resultado.config(text=senha_gerada)

janela = tk.Tk()
janela.title('Gerador de Senhas - by: @GuiMarobo')
janela.geometry("400x350")
janela.config(bg="#111111")
 
titulo = tk.Label(
    janela, text="Gerador de Senhas", font=("Arial", 18, "bold"), fg="#f5fffb", bg="#111111"
)
titulo.pack(pady=10)

usar_maiusculas = tk.BooleanVar()
usar_minusculas = tk.BooleanVar()
usar_numeros = tk.BooleanVar()
usar_simbolos = tk.BooleanVar()

check_maiusculas = tk.Checkbutton(janela, text='Usar maiúsculas', variable=usar_maiusculas, bg="#111111")
check_maiusculas.pack(anchor="w")

check_minusculas = tk.Checkbutton(janela, text='Usar minúsculas', variable=usar_minusculas, bg="#111111")
check_minusculas.pack(anchor="w")

check_numeros = tk.Checkbutton(janela, text='Usar números', variable=usar_numeros, bg="#111111")
check_numeros.pack(anchor="w")

check_simbolos = tk.Checkbutton(janela, text='Usar símbolos', variable=usar_simbolos, bg="#111111")
check_simbolos.pack(anchor="w")

resultado = tk.Label(janela, text="Sua senha aparecerá aqui", font=("Arial", 14, "bold"), fg="#0077cc", bg="#111111")
resultado.pack(pady=20)

botao_gerar = tk.Button(
    janela, text="Gerar Senha", command=gerar_senha_gui,
    font=("Arial", 14, "bold"), bg="#4CAF50", fg="black",
    padx = 10, pady = 5, relief="raised", borderwidth=3
)
botao_gerar.pack(pady=10)

janela.mainloop()