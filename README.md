# 🎙️ Projeto de Transcrição de Áudio com Whisper

Este projeto utiliza o modelo **Whisper** da OpenAI para converter arquivos de áudio em texto automaticamente.

## 📁 Estrutura atual do projeto

```
PROJETO_TRANSCRICAO/
├── Audio_teste.mp4              # Arquivo de áudio de entrada
├── Audio_teste_transcricao.txt  # Transcrição gerada
├── projeto_transcricao.py       # Código principal
├── requirements.txt             # Dependências
├── .gitignore                   # Arquivos ignorados pelo Git
└── README.md                    # Este arquivo
```

## ▶️ Como usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Certifique-se de ter o `ffmpeg` instalado no sistema.

3. Rode o script:
   ```bash
   python projeto_transcricao.py
   ```

4. O texto transcrito será salvo em um arquivo `.txt` com o mesmo nome do áudio.

## ✅ Requisitos

- Python 3.8 ou superior
- `ffmpeg` instalado e no PATH
- Biblioteca `openai-whisper`

## 📌 Observações

- O arquivo de áudio deve estar na raiz do projeto.
- O nome da transcrição será gerado automaticamente a partir do nome do áudio, sem a extensão.

## 📄 Licença

Este projeto é livre para uso pessoal e educacional.
