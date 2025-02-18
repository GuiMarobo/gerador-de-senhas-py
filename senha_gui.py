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
janela.geometry("400x400")
janela.config(bg="#f0f0f0")
 
titulo = tk.Label(janela, text='Gerador de Senhas', font=('Arial', 16, "bold"), bg="#f0f0f0")
titulo.grid(row=0, column=0, columnspan=2, pady=10)

usar_maiusculas = tk.BooleanVar()
usar_minusculas = tk.BooleanVar()
usar_numeros = tk.BooleanVar()
usar_simbolos = tk.BooleanVar()

check_maiusculas = tk.Checkbutton(janela, text='Usar maiúsculas', variable=usar_maiusculas)
check_maiusculas.grid(row=1, column=0, sticky="w", padx=10)

check_minusculas = tk.Checkbutton(janela, text='Usar minúsculas', variable=usar_minusculas)
check_minusculas.grid(row=2, column=0, sticky="w", padx=10)

check_numeros = tk.Checkbutton(janela, text='Usar números', variable=usar_numeros)
check_numeros.grid(row=3, column=0, sticky="w", padx=10)

check_simbolos = tk.Checkbutton(janela, text='Usar símbolos', variable=usar_simbolos)
check_simbolos.grid(row=4, column=0, sticky="w", padx=10)

resultado = tk.Label(janela, text="Sua senha aparecerá aqui", font=("Arial", 14), fg="blue", bg="#f0f0f0")
resultado.grid(row=5, column=0, columnspan=2, pady=20)

botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha_gui)
botao_gerar.grid(row=6, column=0, columnspan=2, pady=10)

janela.mainloop()