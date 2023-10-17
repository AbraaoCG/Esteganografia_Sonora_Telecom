import numpy as np
import soundfile as sf



def variacao_quadratica(tempo, duracao, frequencia_inicial, frequencia_final, para_baixo=True):
    """
    Gera um valor que representa a variação quadrática de frequência ao longo do tempo.

    Argumentos:
    - tempo: array NumPy representando o tempo.
    - duracao: duração total do áudio em segundos.
    - frequencia_inicial: frequência inicial em Hz.
    - frequencia_final: frequência final em Hz.
    - para_baixo: booleano que determina se a variação é para baixo (True) ou para cima (False).

    Retorna:
    - Um array NumPy contendo os valores a serem adicionados à frequência do áudio.
    """
    if para_baixo:
        frequencia = -((frequencia_final - frequencia_inicial) / (2 * duracao) * tempo**2 ) + frequencia_inicial
    else:
        frequencia = ((frequencia_final - frequencia_inicial) / (2 * duracao) * tempo**2  ) + frequencia_inicial
    
    return frequencia


# Parâmetros gerais
taxa_de_amostragem = 44100  # Taxa de amostragem em Hz
duracao = 5  # Duração do áudio em segundos

# Frequências desejadas
frequencia1 = 440  # Primeira frequência em Hz
frequencia2 = 4000  # Segunda frequência em Hz

# Gere o áudio com uma janela que transite suavemente entre as frequências
frames = int(taxa_de_amostragem * duracao)
tempo = np.linspace(0, duracao,frames , endpoint=False)
audio = np.zeros(frames)

t1,t2 = 0,int(frames/2)
variacao = variacao_quadratica(tempo[t1:t2], duracao, frequencia1, frequencia2, para_baixo=False)
audio[t1:t2] = np.sin(2 * np.pi * variacao * tempo[t1:t2])

t1,t2 = int(frames/3), int(2*frames/3)
audio[t1:t2] += np.sin(2 * np.pi * 1200 * tempo[t1:t2])

t1,t2 = int(frames/2)+1, int(frames)
variacao = variacao_quadratica(tempo[t1:t2], duracao, frequencia1, frequencia2, para_baixo=True)
audio[t1:t2] += np.sin(2 * np.pi * variacao * tempo[t1:t2])

# Salve o áudio em um arquivo WAV
sf.write('audio_dual_freq2.wav', audio, taxa_de_amostragem)