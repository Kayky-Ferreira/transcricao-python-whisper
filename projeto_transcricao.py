import whisper
import os

# Escolhendo o modelo base
modelo = whisper.load_model("base")

print("Aguarde um momento, transcrevendo o áudio... isso pode levar alguns segundos.")

# Transcrevendo o áudio
caminho_audio = "Audio_teste.mp4"
texto = modelo.transcribe(caminho_audio)

# Exibindo o resultado
print(f"Transcrição gerada:\n {texto['text']}")

#pegando o nome do arquivo sem extensão e Criando o nome do arquivo .txt
nome_arquivo_txt = f"{os.path.splitext(os.path.basename(caminho_audio))[0]}_transcricao.txt"

# Salvando a transcrição no arquivo .txt
with open (nome_arquivo_txt, 'w', encoding="utf-8") as arquivo:
    arquivo.write(texto['text'])
