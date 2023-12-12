from codigo_esteganografia.decodificador import decodificar_mensagem
from codigo_esteganografia.codificador import enviar_mensagem

# Definir frequência inicial, frequência máxima e número de caracteres
# permitidos a partir do primeiro ASCII
fi = 20 ; fm = 21000 ; numCar = 255 ; dc = 0.02

# mensagem_env = "Eles estão na transilvânia!"


# print(f'Mensagem enviada: {mensagem_env} \n tamanho = {len(mensagem_env)}')
# enviar_mensagem(mensagem_env,fi = fi, fm = fm, numCar = numCar)


filepath = 'audioGiovanni.wav'
mensagem_recebida = decodificar_mensagem(fileName=filepath,fi = fi, fm = fm, numCar = numCar)

print(f'Mensagem recebida: {mensagem_recebida}')

# print(f'Igual = {mensagem_recebida == mensagem_env}')