import whisper
import os
import customtkinter as ctk
import tkinter.messagebox as msgbox
from tkinter import filedialog

# Variáveis que armazenam caminhos e resultados durante o uso da aplicação
caminho = None
nome_arquivo = None
texto = None

# Configuração da janela principal da interface (cor, tamanho, título)
tela = ctk.CTk()
tela.title("transcrever audio")
tela.geometry("400x400")
tela.configure(fg_color = "#FEFAED")

# Lista de modelos disponíveis do Whisper para seleção pelo usuário
lista_models = ["tiny", "base", "small", "medium", "large"]
opcao_models = ctk.CTkOptionMenu(master= tela, values= lista_models)
opcao_models.pack(pady = 20)

# Funções principais: selecionar arquivo, transcrever e salvar resultado
# Abre janela para o usuário selecionar o arquivo de áudio
def buscar_arquivo():
    global caminho
    global nome_arquivo
    caminho = filedialog.askopenfilename()
    nome_arquivo = os.path.basename(caminho)
    print(f'O arquivo selecionado é: {nome_arquivo}')

# Carrega o modelo escolhido e realiza a transcrição do áudio selecionado
def transcrever():
    global caminho
    global texto
    nome_do_modelo = opcao_models.get()
    print(f'Carregando o modelo: {nome_do_modelo} ...')
    # Carrega o modelo selecionado pelo usuário (ex: base, small...)
    modelo = whisper.load_model(nome_do_modelo)
    print("Iniciando a transcrição...")
    texto = modelo.transcribe(caminho)
    print (f'Transcrição Concluida! \n {texto['text']}')

# Salva o conteúdo transcrito em um arquivo .txt no local escolhido pelo usuário
def salvar():
    global nome_arquivo
    global texto

# Verifica se o usuário já selecionou um arquivo e realizou a transcrição
    if nome_arquivo is None or texto is None:
        msgbox.showerror("Erro ao Salvar", "Por favor, selecione e transcreva um arquivo de áudio primeiro.")
        return

    nome_base, _ = os.path.splitext(nome_arquivo)
    nome_salvar = nome_base + "_transcricao.txt"

    caminho_salvar = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        initialfile=nome_salvar
    )

    if not caminho_salvar:
        return

    try:
        with open(caminho_salvar, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto['text'])
        msgbox.showinfo("Sucesso", f"O arquivo foi salvo com sucesso em: {caminho_salvar}")
    except Exception as e:
        msgbox.showerror("Erro ao Salvar", f"Ocorreu um erro ao tentar salvar o arquivo: {e}")

# Botões da interface: selecionar, transcrever e salvar

# Botão que abre o seletor de arquivos
btn_selecionar = ctk.CTkButton(master = tela, text = "Selecione o arquivo", command = buscar_arquivo)
btn_selecionar.pack(pady = 20)

# Botão que inicia a transcrição
btn_transcrever = ctk.CTkButton(master= tela, text = 'transcrever arquivo', command= transcrever)
btn_transcrever.pack(pady = 20)

# Botão que salva o texto transcrito
btn_salvar = ctk.CTkButton(master = tela, text = "Salvar", command= salvar)
btn_salvar.pack(pady = 20)

# Inicia o loop principal da interface gráfica
tela.mainloop()