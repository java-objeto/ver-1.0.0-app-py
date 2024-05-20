import tkinter as tk
from tkinter import ttk
import os

def salvar_informacoes():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    # Criar pasta para armazenar os arquivos se ainda não existir
    if not os.path.exists("informacoes"):
        os.makedirs("informacoes")

    # Criar um arquivo com as informações do usuário
    with open(f"informacoes/{nome}.txt", "w") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Email: {email}\n")
        arquivo.write(f"Telefone: {telefone}\n")

    print("Informações salvas com sucesso!")

def visualizar_informacoes():
    # Criar janela para exibir a tabela
    janela_tabela = tk.Toplevel()
    janela_tabela.title("Informações Cadastradas")
    janela_tabela.geometry("400x300")

    # Criar tabela
    tabela = ttk.Treeview(janela_tabela, columns=("Nome", "Email", "Telefone"), show="headings")
    tabela.heading("Nome", text="Nome")
    tabela.heading("Email", text="Email")
    tabela.heading("Telefone", text="Telefone")

    # Carregar dados da pasta "informacoes" para a tabela
    if os.path.exists("informacoes"):
        for arquivo in os.listdir("informacoes"):
            if arquivo.endswith(".txt"):
                with open(os.path.join("informacoes", arquivo), "r") as f:
                    dados = f.readlines()
                    nome = dados[0].split(":")[1].strip()
                    email = dados[1].split(":")[1].strip()
                    telefone = dados[2].split(":")[1].strip()
                    tabela.insert("", "end", values=(nome, email, telefone))

    tabela.pack(padx=10, pady=10, fill="both", expand=True)

# Criar janela
janela = tk.Tk()
janela.title("Inserir e Visualizar Informações")
janela.geometry("400x200")
janela.configure(bg="#f0f0f0")

# Criar e posicionar widgets
label_nome = tk.Label(janela, text="Nome:", bg="#f0f0f0")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(janela, text="Email:", bg="#f0f0f0")
label_email.grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_telefone = tk.Label(janela, text="Telefone:", bg="#f0f0f0")
label_telefone.grid(row=2, column=0, padx=10, pady=5)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=2, column=1, padx=10, pady=5)

botao_salvar = tk.Button(janela, text="Salvar Informações", command=salvar_informacoes)
botao_salvar.grid(row=3, column=0, columnspan=2, pady=10)

botao_visualizar = tk.Button(janela, text="Visualizar Informações", command=visualizar_informacoes)
botao_visualizar.grid(row=4, column=0, columnspan=2, pady=10)

# Executar aplicação
janela.mainloop()
