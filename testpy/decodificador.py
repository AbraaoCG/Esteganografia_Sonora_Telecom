import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Frequência inicial para o caractere inicial unicode, frequencia máxima e número de caracteres representados.
frequencia_inicial = 50
freq_maxima = 20000
numCaracteresMax = 256

# Leitura do arquivo de audio.
samplerate, data = wavfile.read('message.wav')



# time = np.linspace(0, (length * samplerate) - 1, data.shape[0])
# plt.plot(np.arange(data.shape[0]), data[:], label="Main Channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
