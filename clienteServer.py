from codigo_esteganografia.decodificador import decodificar_mensagem
from codigo_esteganografia.codificador import enviar_mensagem
import requests, json

# Definir frequência inicial, frequência máxima e número de caracteres
# permitidos a partir do primeiro ASCII
fi = 20050 ; fm = 21000 ; numCar = 255

mensagem_env = "Eles estão na transilvânia!"

#payload = json.load() #1

mode = 0
encodeJSON = {'encodeMsg':mensagem_env , 'mode' : mode}
codificar_msg = requests.post("http://127.0.0.1:5000/encodeWAV", json=encodeJSON) #2
attachment_data = codificar_msg.content # Arquivo de áudio wav em bytes.

print(attachment_data)

# Cabeçalhos necessários para indicar que está enviando dados binários
headers = {
    'Content-Type': 'application/octet-stream',  # Tipo de mídia para dados binários
}
decodeJSON = {'mode' : mode}
decodif_msg = requests.post("http://127.0.0.1:5000/decodeWAV", json=decodeJSON, data=attachment_data, headers=headers)

print(decodif_msg)

# with open('myfile.wav', mode='bx') as f:
#     f.write(attachment_data)

# mensagem_recebida = decodificar_mensagem(fi = fi, fm = fm, numCar = numCar)

# print(f'Mensagem recebida: {mensagem_recebida}')

# print(f'Igual = {mensagem_recebida == mensagem_env}')