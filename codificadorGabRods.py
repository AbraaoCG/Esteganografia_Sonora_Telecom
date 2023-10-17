import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

# Frequência inicial para o caractere 'A'
frequencia_inicial = 1000

# Função para calcular a frequência com base no caractere.
# Recebe um caractere como entrada e calcula a frequência 
# correspondente com base na distância entre o caractere e 'A' 
# no alfabeto
def calcular_frequencia(char):
    return frequencia_inicial + 500 * (ord(char) - ord('A'))

# Recebe a string de entrada e transforma em maiúsculo
entrada = input("Digite uma sequência de caracteres (A-Z): ").upper()

# Duração de cada caractere em segundos
duracao_caractere = 0.5

# Lista para armazenar as frequências de cada caractere
frequencias = [calcular_frequencia(char) for char in entrada]
frequencias.append(frequencias[-1]+duracao_caractere)

# Lista para armazenar o tempo de início de cada caractere
tempos_inicio = [i * duracao_caractere for i in range(len(entrada))]
tempos_inicio.append(tempos_inicio[-1]+duracao_caractere)

# Plot da frequência em relação ao tempo
plt.figure(figsize=(12, 4))
plt.step(tempos_inicio, frequencias, where='post')
plt.xlabel('Tempo (s)')
plt.ylabel('Frequência (Hz)')
plt.title('Frequência x Tempo para os caracteres {}'.format(entrada))
plt.grid(True)

# Salva o gráfico em um arquivo de imagem (opcional)
plt.savefig('fxt_{}.png'.format(entrada))

# Gera o sinal de áudio
tempo_total = len(entrada) * duracao_caractere

# Cada caractere deve ter duração de 0.5 s.
# Taxa de amostragem fixa em 44100 Hz (44100 amostras por segundo)
# num_amostras = D x S -> N = 0.5 x 44100 = 22050 amostras
num_amostras = int(duracao_caractere * 44100)
tempo = np.linspace(0, duracao_caractere, num_amostras, endpoint=False)
sinal = np.concatenate([np.sin(2 * np.pi * f * tempo) for f in frequencias])
print(sinal)
# Salva o sinal em um arquivo WAV
wavfile.write('{}.wav'.format(entrada), 44100, sinal.astype(np.float32))

# Exibe o gráfico
plt.show()
