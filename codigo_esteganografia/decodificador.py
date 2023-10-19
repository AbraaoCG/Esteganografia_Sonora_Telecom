import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Função para remontar mensagem baseado nas frequências ordenadas.
def decodificar_frequencias(list_freq):
    
    # Frequência inicial para o caractere inicial unicode, frequencia máxima e número de caracteres representados.
    frequencia_inicial = 50
    freq_maxima = 20000
    numCaracteresMax = 256
    freqRange = freq_maxima - frequencia_inicial
    difFreq = freqRange / numCaracteresMax # Diferença de frequência entre dois caracteres.

    msg_decodificada = []        
    for f in list_freq:
            posicao = int( round( (f - frequencia_inicial) / difFreq) )
            char = chr(posicao)
            msg_decodificada.append(char)
    return ''.join(msg_decodificada)


def decodificar_mensagem(filename = 'message.wav'):
    # Carregue o arquivo de áudio
    sample_rate, audio_data = wavfile.read(filename)

    # Defina o tamanho do segmento( 1 caractere ) em segundos (0.5 segundos)
    segment_duration = 0.5
    segment_samples = int(segment_duration * sample_rate)


    lista_frequencias = []
    # Para cada segmento, calcule a frequência dominante utilizando FFT.
    for i in range(0, len(audio_data) - 1, segment_samples):
        segment = audio_data[i:i+segment_samples]
        # Use a Transformada de Fourier para calcular as frequências
        frequencies = np.fft.fftfreq(len(segment), 1 / sample_rate)
        #print(len(frequencies))
        magnitudes = np.abs(np.fft.fft(segment))
        
        # Encontre a frequência dominante no segmento
        dominant_frequency = np.abs(frequencies[np.argmax(magnitudes)]) # Frequência é espelhada, então se aparecer uma frequência negativa na verdade a gerada foi positiva.
        lista_frequencias.append(dominant_frequency)

    return decodificar_frequencias(lista_frequencias)


