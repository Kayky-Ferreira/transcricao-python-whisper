import whisper
import os
import customtkinter as ctk
import tkinter.messagebox as msgbox
from tkinter import filedialog

# VariÃ¡veis globais
caminho = None
nome_arquivo = None
texto = None

# ConfiguraÃ§Ã£o da janela
tela = ctk.CTk()
tela.title("Transcrever Ãudio")
tela.geometry("400x400")
tela.configure(fg_color="#FEFAED")

# Modelos disponÃ­veis
lista_models = ["tiny", "base", "small", "medium", "large"]
opcao_models = ctk.CTkOptionMenu(master=tela, values=lista_models)
opcao_models.pack(pady=20)


# ==========================
# Selecionar arquivo
# ==========================
def buscar_arquivo():
    global caminho
    global nome_arquivo

    caminho = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=[
            ("Arquivos de Ã¡udio", "*.mp3 *.wav *.m4a *.mp4"),
            ("Todos os arquivos", "*.*")
        ]
    )

    # UsuÃ¡rio cancelou
    if not caminho:
        return

    # Verifica extensÃ£o
    if not caminho.lower().endswith((".mp3", ".wav", ".m4a", ".mp4")):
        msgbox.showwarning(
            "Arquivo invÃ¡lido",
            "Selecione um arquivo MP3, WAV, M4A ou MP4."
        )
        caminho = None
        return

    nome_arquivo = os.path.basename(caminho)

    print(f"Arquivo selecionado: {nome_arquivo}")


# ==========================
# Transcrever
# ==========================
def transcrever():
    global caminho
    global texto

    if not caminho:
        msgbox.showwarning("Aviso", "Selecione um arquivo primeiro.")
        return

    nome_do_modelo = opcao_models.get()

    print("1 - Carregando modelo")
    modelo = whisper.load_model(nome_do_modelo)

    print("2 - Modelo carregado")

    print("3 - Iniciando transcriÃ§Ã£o")

    texto = modelo.transcribe(
        caminho,
        language="pt",
        verbose=True
    )

    print("4 - TranscriÃ§Ã£o finalizada")

    print(texto["text"])

# ==========================
# Salvar
# ==========================
def salvar():
    global nome_arquivo
    global texto

    if nome_arquivo is None or texto is None:
        msgbox.showerror(
            "Erro",
            "Selecione e transcreva um arquivo antes de salvar."
        )
        return

    nome_base, _ = os.path.splitext(nome_arquivo)
    nome_salvar = nome_base + "_transcricao.txt"

    caminho_salvar = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de Texto", "*.txt")],
        initialfile=nome_salvar
    )

    if not caminho_salvar:
        return

    try:
        with open(caminho_salvar, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto["text"])

        msgbox.showinfo(
            "Sucesso",
            f"Arquivo salvo com sucesso!\n\n{caminho_salvar}"
        )

    except Exception as erro:
        msgbox.showerror(
            "Erro",
            f"Erro ao salvar:\n\n{erro}"
        )


# ==========================
# BotÃµes
# ==========================
btn_selecionar = ctk.CTkButton(
    master=tela,
    text="Selecionar Arquivo",
    command=buscar_arquivo
)
btn_selecionar.pack(pady=20)

btn_transcrever = ctk.CTkButton(
    master=tela,
    text="Transcrever",
    command=transcrever
)
btn_transcrever.pack(pady=20)

btn_salvar = ctk.CTkButton(
    master=tela,
    text="Salvar TranscriÃ§Ã£o",
    command=salvar
)
btn_salvar.pack(pady=20)

# Inicia interface
tela.mainloop()
