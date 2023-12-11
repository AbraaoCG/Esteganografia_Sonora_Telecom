from codigo_esteganografia.decodificador import decodificar_mensagem
from codigo_esteganografia.codificador import enviar_mensagem
import requests, json

# Definir frequência inicial, frequência máxima e número de caracteres
# permitidos a partir do primeiro ASCII
fi = 20050 ; fm = 21000 ; numCar = 255

mensagem_env = "Eles estão na transilvânia!"

#payload = json.load() #1

resposta = requests.post("http://127.0.0.1:5000/encodeWAV", json={'encodeMsg':mensagem_env , 'mode' : 0}) #2

print(resposta)

# mensagem_recebida = decodificar_mensagem(fi = fi, fm = fm, numCar = numCar)

# print(f'Mensagem recebida: {mensagem_recebida}')

# print(f'Igual = {mensagem_recebida == mensagem_env}')