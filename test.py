import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import soundfile as sf

# Parâmetros gerais
taxa_de_amostragem = 44100  # Taxa de amostragem em Hz
duracao = 5  # Duração do áudio em segundos

# Suponha que você tenha uma matriz de relação Frequência X Tempo
# Substitua esta matriz pela sua matriz real
tam = 100
Relacao = np.zeros(shape=(tam, tam))
Relacao[:(int(tam/2)),int(tam * 0.3)] = 1
#Relacao[(int(tam/2)):,int(tam * 0.6)] = 1
# Calcule as dimensões da matriz de relação
num_frequencias, num_tempo = Relacao.shape

# Defina a faixa de frequências desejada
frequencia_minima = 40  # Hz
frequencia_maxima = 20000  # Hz
amp_min = -60 ; amp_max = -10
referencia = 1000

# Gere o áudio com base na matriz de relação mapeada para a faixa de frequências
tempo = np.linspace(0, duracao, int(taxa_de_amostragem * duracao), endpoint=False)
audio = np.zeros_like(tempo)

for f in range(num_frequencias):
    frequencia = frequencia_minima + (frequencia_maxima - frequencia_minima) * (f/num_frequencias)
    power_temp = [0 * len(tempo)]
    for t in range(num_tempo):
        valor_relacao = Relacao[t,f]
        

# Salve o áudio em um arquivo WAV
sf.write('audio_espectrograma_mapeado.wav', audio, taxa_de_amostragem)