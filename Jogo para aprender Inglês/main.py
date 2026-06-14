import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import random

# ====================== CONFIGURAÇÕES ======================
tentativas = 3
pontos = 0
duration = 5  # segundos de gravação
sample_rate = 44100

# Probabilidade de mostrar a tradução na fase MÉDIO (50%)
PROBABILIDADE_MOSTRAR_MEDIO = 0.5

# ====================== LISTA DE PALAVRAS ======================
words_by_level = {
    "fácil": {
        "gato": "cat",
        "cachorro": "dog",
        "maçã": "apple",
        "leite": "milk",
        "sol": "sun",
        "água": "water"          # 6ª palavra
    },
    
    "médio": {
        "casa": "house",
        "escola": "school",
        "amigo": "friend",
        "janela": "window",
        "amarelo": "yellow",
        "livro": "book",
        "carro": "car",
        "família": "family"      # 8 palavras
    },
    
    "difícil": {
        "tecnologia": "technology",
        "universidade": "university",
        "informação": "information",
        "pronúncia": "pronunciation",
        "imaginação": "imagination",
        "desenvolvimento": "development",
        "conhecimento": "knowledge",
        "responsabilidade": "responsibility",
        "comunicação": "communication",
        "experiência": "experience"   # 10 palavras
    }
}

# ====================== ESCOLHA DA FASE ======================
while True:
    fase = input("Escolha a fase (fácil, médio ou difícil): ").strip().lower()
    if fase in words_by_level:
        break
    print("Fase inválida! Digite 'fácil', 'médio' ou 'difícil'.")

# Cria lista de palavras restantes (evita repetição)
palavras_restantes = list(words_by_level[fase].items())

print(f"\n🎮 Iniciando fase {fase.upper()}!")
print(f"Total de palavras: {len(palavras_restantes)}\n")

recognizer = sr.Recognizer()

# ====================== LOOP PRINCIPAL DO JOGO ======================
while tentativas > 0 and palavras_restantes:
    # Sorteia uma palavra
    palavra_pt, traducao_correta = random.choice(palavras_restantes)
    
    print(f"\n📝 Palavra escolhida: **{palavra_pt.upper()}**")
    
    # Decide se mostra a tradução (só na fácil e às vezes na médio)
    mostrar_traducao = False
    if fase == "fácil":
        mostrar_traducao = True
    elif fase == "médio":
        mostrar_traducao = random.random() < PROBABILIDADE_MOSTRAR_MEDIO
    
    if mostrar_traducao:
        print(f"Tente falar a tradução: **{traducao_correta.upper()}**")
    else:
        print("Fale a tradução em inglês agora...")
    
    print(f"\n🎤 Gravando... (você tem {duration} segundos)")

    # Gravação de áudio
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    # Salva o arquivo de áudio
    wav.write("output.wav", sample_rate, recording)

    # Reconhecimento de voz
    try:
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio, language="en-US")
        text = text.lower().strip()

        print(f"\nVocê disse: {text}")

        if text == traducao_correta.lower():
            print("✅ Acertou!\n")
            pontos += 1
        else:
            print(f"❌ Errou! A tradução correta era: {traducao_correta}\n")
            tentativas -= 1

        # Remove a palavra para não repetir
        palavras_restantes.remove((palavra_pt, traducao_correta))

    except sr.UnknownValueError:
        print("❌ Não consegui entender o que você falou.\n")
        tentativas -= 1
    except Exception as e:
        print(f"Erro: {e}\n")
        tentativas -= 1

    print(f"Pontos: {pontos} | Tentativas restantes: {tentativas}")
    print(f"Palavras restantes: {len(palavras_restantes)}\n")

# ====================== FIM DO JOGO ======================
print("\n" + "="*50)
print("🎮 FIM DE JOGO!")
print(f"Pontuação final: {pontos} ponto(s)")

if len(palavras_restantes) == 0:
    print("🏆 PARABÉNS! Você completou todas as palavras da fase!")
else:
    print(f"Você acertou {pontos} de {len(words_by_level[fase])} palavras.")