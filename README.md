🎮 # Jogo-para-aprender-Inglês
Um jogo interativo de aprendizado de inglês que utiliza reconhecimento de voz para praticar a pronúncia e tradução de palavras. O jogador deve falar a tradução correta em inglês das palavras sorteadas em português.

✨ Funcionalidades

Três níveis de dificuldade: Fácil, Médio e Difícil

Fácil: Mostra a tradução em inglês para o aluno repetir

Médio: Às vezes mostra a tradução (aleatório) e às vezes não

Difícil: Não mostra a tradução (exige conhecimento)

Palavras não se repetem durante a partida

Finaliza quando todas as palavras da fase são completadas ou as tentativas acabam

6 palavras no Fácil | 8 palavras no Médio | 10 palavras no Difícil

📋 Requisitos

Python 3.8 ou superior
Microfone funcionando

🛠️ Instalação

Clone o repositório: 
git clone https://github.com/seuusuario/vocab-english-game.git
cd vocab-english-game

Instale as dependências: 
pip install sounddevice numpy scipy speechrecognition pyaudio

▶️ Como Executar

Execute o script: 

python main.py

Escolha a fase (fácil, médio ou difícil)

Quando aparecer a palavra, fale a tradução em inglês claramente dentro dos 5 segundos

🎯 Como Jogar

O jogo sorteia uma palavra em português.

Você deve falar a tradução em inglês.

Tem 3 tentativas (erros) por partida.

Quanto mais palavras você acertar, melhor sua pontuação!

⚙️ Configurações (Opcionais)

duration = 5 → Tempo de gravação em segundos
PROBABILIDADE_MOSTRAR_MEDIO = 0.5 → Chance de mostrar a tradução na fase médio (0.0 a 1.0)
