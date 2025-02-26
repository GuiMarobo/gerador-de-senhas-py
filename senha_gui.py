# senha_gui.py

import tkinter as tk
from tkinter import messagebox
from senha_logica import gerar_senha #importa a função gerar_senha do arquivo senha_logica.py

def gerar_senha_gui():
    tamanho = tamanho_senha.get()
    senha_gerada = gerar_senha(
        usar_maiusculas.get(),
        usar_minusculas.get(),
        usar_numeros.get(),
        usar_simbolos.get(),
        tamanho
    )

    if senha_gerada is None:
        messagebox.showwarning("Erro", "Selecione pelo menos uma opção para gerar sua senha.")
    else:
        resultado.config(text=senha_gerada)

janela = tk.Tk()
janela.title('Gerador de Senhas - by: @GuiMarobo')
janela.geometry("400x400")
janela.config(bg="#2C2F33")
 
titulo = tk.Label(
    janela, text="Gerador de Senhas", font=("Arial", 18, "bold"), fg="#FFFFFF", bg="#2C2F33"
)
titulo.pack(pady=10)

usar_maiusculas = tk.BooleanVar()
usar_minusculas = tk.BooleanVar()
usar_numeros = tk.BooleanVar()
usar_simbolos = tk.BooleanVar()

check_maiusculas = tk.Checkbutton(janela, text='Usar maiúsculas', variable=usar_maiusculas, bg="#2C2F33", fg="#FFFFFF")
check_maiusculas.pack(anchor="w")

check_minusculas = tk.Checkbutton(janela, text='Usar minúsculas', variable=usar_minusculas, bg="#2C2F33", fg="#FFFFFF")
check_minusculas.pack(anchor="w")

check_numeros = tk.Checkbutton(janela, text='Usar números', variable=usar_numeros, bg="#2C2F33", fg="#FFFFFF")
check_numeros.pack(anchor="w")

check_simbolos = tk.Checkbutton(janela, text='Usar símbolos', variable=usar_simbolos, bg="#2C2F33", fg="#FFFFFF")
check_simbolos.pack(anchor="w")

tamanho_senha = tk.IntVar(value=12)
label_tamanho = tk.Label(janela, text="Tamanho da senha:", font=("Arial", 12), bg="#2C2F33", fg="#7289DA")
label_tamanho.pack(pady=5)

scale_tamanho = tk.Scale(janela, from_=6, to=32, orient="horizontal", variable=tamanho_senha, bg="#2C2F33", fg="#FFFFFF")
scale_tamanho.pack()

resultado = tk.Label(janela, text="Sua senha aparecerá aqui", font=("Arial", 18, "bold"), fg="#7289DA", bg="#2C2F33")
resultado.pack(pady=20)

botao_gerar = tk.Button(
    janela, text="Gerar Senha", command=gerar_senha_gui,
    font=("Arial", 14, "bold"), bg="#2C2F33", fg="#7289DA",
    padx = 10, pady = 5, relief="raised", borderwidth=3
)
botao_gerar.pack(pady=10)

janela.mainloop()