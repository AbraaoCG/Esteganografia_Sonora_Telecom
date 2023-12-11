import numpy as np
from scipy.io import wavfile

# Função para calcular a frequência com base no caractere.
# Recebe um caractere como entrada e calcula a frequência 
# correspondente com base na distância entre o caractere de primeira numeração --> chr(1).
# no alfabeto
def calcular_frequencia(char,difFreq,frequencia_inicial,numCar):
    if(ord(char) > numCar):
        print('Erro: mensagem deve ser utilizar caracteres na formatação Unicode')
        print(f'Caractere fora dos padrões: {char}')
    return frequencia_inicial + difFreq * (ord(char))


def enviar_mensagem(entrada,filename = 'message.wav', fi = 50, fm = 1000, numCar = 255, dc = 0.8):
    ## Definir argumentos
    # Argumento para plot ou não do gráfico esperado no espectrometro
    plotFlag = False
    # Frequência inicial para o caractere inicial unicode, frequencia máxima e número de caracteres representados.
    frequencia_inicial = fi # 50
    freq_maxima = fm # 1000
    numCaracteresMax = numCar # 256
    # Duração de cada caractere em segundos
    duracao_caractere = dc
    # Taxa de amostragem fixa em 'ta' Hz ('ta' amostras por segundo)
    ta = 44100
    
    freqRange = freq_maxima - frequencia_inicial
    difFreq = freqRange / numCaracteresMax

    # print(f'A dif de frequencia para cada caractere é de {difFreq}')

    # Recebe a string de entrada e transforma em maiúsculo / A principio argumento da função.
    #entrada = input("Digite uma mensagem: ")

    # Lista para armazenar as frequências de cada caractere
    frequencias = [calcular_frequencia(char,difFreq,frequencia_inicial,numCar) for char in entrada]

    # Lista para armazenar o tempo de início de cada caractere
    tempos_inicio = [i * duracao_caractere for i in range(len(entrada))]

    # Cada caractere deve ter duração de 0.5 s.
    # num_amostras = D x S
    num_amostras = int(duracao_caractere * ta)

    # Criando array com valores igualmente espaçados que representa o tempo 
    # total de um caractere no sinal, variando de 0 até a duração de
    # um caractere (duracao_caractere), com ( duracao_caractere * ta ) amostras por caractere.
    tempo = np.linspace(0, duracao_caractere, num_amostras, endpoint=False)


    # Agora ocorre a geração do sinal de áudio.

    # Para cada caractere, geramos um sinal senoidal com frequência
    # correspondente ao caractere e, por fim, concatenamos todos eles 
    # para gerar um sinal final composto por N senoides de frequências
    # distintas.
    sinal = np.concatenate([np.sin(2 * np.pi * f * tempo) for f in frequencias])


    # Por fim, salvamos o sinal em um arquivo WAV, definindo a taxa de
    # amostragem como ta Hz e converte o sinal para o formato float32.
    # Isso é necessário porque os arquivos de áudio WAV costumam usar amostras 
    # de ponto flutuante de 32 bits para armazenar os dados do sinal. 
    wavfile.write(filename, ta, sinal.astype(np.float32))

    
    if (plotFlag):
        import matplotlib.pyplot as plt
        # Plot da frequência em relação ao tempo
        plt.figure(figsize=(12, 4))
        plt.step(tempos_inicio, frequencias, where='post')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Frequência (Hz)')
        plt.title('Frequência x Tempo para os caracteres {}'.format(entrada))
        plt.grid(True)

        # Salva o gráfico em um arquivo de imagem (opcional)
        plt.savefig('fxt_{}.png'.format(entrada))
        # Exibe o gráfico f x t
        plt.show()
