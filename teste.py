import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def salvar_dados():
    nome = campo_nome.get()
    idade = campo_idade.get()
    cargo = campo_cargo.get()
    departamento = combo_departamento.get()

    mensagem = f"""
    Dados informados:

    Nome: {nome}
    Idade: {idade}
    Cargo: {cargo}
    Departamento: {departamento}
    """

    messagebox.showinfo("Dados salvos", mensagem)


def limpar_campos():
    campo_nome.delete(0, tk.END)
    campo_idade.delete(0, tk.END)
    campo_cargo.delete(0, tk.END)
    combo_departamento.set("")


# Janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro")
janela.geometry("1500x350")


# -------- MENU SUPERIOR --------

barra_menu = tk.Menu(janela)

menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(label="Novo")
menu_arquivo.add_command(label="Salvar")
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)

barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_ajuda = tk.Menu(barra_menu, tearoff=0)
menu_ajuda.add_command(label="Sobre")

barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)

janela.config(menu=barra_menu)


# -------- FORMULÁRIO --------

frame = ttk.Frame(janela, padding=20)
frame.pack(fill="both", expand=True)


ttk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w")
campo_nome = ttk.Entry(frame, width=30)
campo_nome.grid(row=0, column=1, pady=5)


ttk.Label(frame, text="Idade:").grid(row=1, column=0, sticky="w")
campo_idade = ttk.Entry(frame)
campo_idade.grid(row=1, column=1, pady=5)


ttk.Label(frame, text="Cargo:").grid(row=2, column=0, sticky="w")
campo_cargo = ttk.Entry(frame)
campo_cargo.grid(row=2, column=1, pady=5)


ttk.Label(frame, text="Departamento:").grid(row=3, column=0, sticky="w")
combo_departamento = ttk.Combobox(frame, values=[
    "Financeiro",
    "RH",
    "TI",
    "Operações"
])
combo_departamento.grid(row=3, column=1, pady=5)


# -------- BOTÕES --------

frame_botoes = ttk.Frame(janela)
frame_botoes.pack(pady=10)

ttk.Button(frame_botoes, text="Salvar", command=salvar_dados).grid(row=0, column=0, padx=10)
ttk.Button(frame_botoes, text="Limpar", command=limpar_campos).grid(row=0, column=1, padx=10)


# Loop principal
janela.mainloop()