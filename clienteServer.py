from codigo_esteganografia.decodificador import decodificar_mensagem
from codigo_esteganografia.codificador import enviar_mensagem
import requests, json
import base64
from scipy.io import wavfile

# Definir frequência inicial, frequência máxima e número de caracteres
# permitidos a partir do primeiro ASCII
fi = 50 ; fm = 21000 ; numCar = 255 ; dc = 0.02

# mensagem_env = "Eles estão na transilvânia!"
mensagem_env = "Eles estao na transilvania!"

mode = 0
# encodeJSON = {"encodeMsg":mensagem_env , "mode" : mode}
# codificar_msg = requests.post("http://127.0.0.1:5000/encodeWAV", json= encodeJSON) #2
# attachment_data = codificar_msg.content # Arquivo de áudio wav em bytes.


# Opening the binary file in binary mode as rb(read binary)
# f = open("instance\serverFiles\encodeFile.wav", mode="rb")
f = open("audioGiovanni.wav", mode="rb")

 
# Reading file data with read() method
data = f.read()

# print(data)

wavEncoded = base64.b64encode(data).decode("utf-8")

#print(wavEncoded)

data = {"mode" : mode, "wavFile" : wavEncoded}
# files = {"wavFile" : attachment_data}
# print(type(attachment_data))
# arquivo_wav = {"wavFile": ("myfile", attachment_data)}
#print(arquivo_wav)
decodif_msg = requests.post("http://127.0.0.1:5000/decodeWAV", data = data ).content

decodif_msg = str(decodif_msg)[2:-1]
print(decodif_msg)





#enviar_mensagem(mensagem_env, filename= "myfile.wav",fi = fi, fm = fm, numCar = numCar, dc = dc)

#mensagem_recebida = decodificar_mensagem(fileName= "myfile.wav",fi = fi, fm = fm, numCar = numCar, dc = dc)

#print(f"Mensagem recebida: {mensagem_recebida}")

#print(f"Igual = {mensagem_recebida == mensagem_env}")

