import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import soundfile as sf

# Carregue a imagem que você deseja usar como modelo
direct_dados = 'Base_dados'
imagem = Image.open(f'{direct_dados}/A.png')
imagem = np.array(imagem)  # Converta a imagem para um array NumPy

# Crie um espectrograma a partir da imagem
espectrograma = np.mean(imagem, axis=2)  # Converta a imagem colorida em escala de cinza
espectrograma = espectrograma / np.max(espectrograma)  # Normalize os valores entre 0 e 1

# Defina os parâmetros do áudio
taxa_de_amostragem = 44100  # Taxa de amostragem em Hz
duracao = 5  # Duração do áudio em segundos
frequencia = 440  # Frequência do áudio em Hz

# Gere o áudio
tempo = np.linspace(0, duracao, int(taxa_de_amostragem * duracao), endpoint=False)
audio = np.sin(2 * np.pi * frequencia * tempo)  # Um tom simples, você pode personalizar isso

# Salve o áudio em um arquivo
sf.write('audio_com_espectrograma.wav', audio, taxa_de_amostragem)

# Plote o espectrograma
plt.figure(figsize=(12, 4))
# plt.ylim(2048,17000)
librosa.display.specshow(espectrograma, sr=taxa_de_amostragem, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma da Imagem')
plt.show()
