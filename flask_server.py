from flask import Flask, request,send_file, make_response
from codigo_esteganografia.codificador import enviar_mensagem
from codigo_esteganografia.decodificador import decodificar_mensagem
import requests
import random
import os
app = Flask(__name__)

dataPath = os.path.join(app.instance_path, 'serverFiles')
os.makedirs(dataPath, exist_ok=True )

@app.route('/')
def hello():
    return 'Programa de Estenografia sonora'

@app.route('/encodeWAV', methods = ['POST'] )
def codificar_mensagem():
    if request.method == 'POST':
        data = request.json
        if 'encodeMsg' in data:
            messageToEncode = data['encodeMsg']
            mode = data['mode']

            if mode == 0: # light mode
                fi,fm,numCar,dc = 20, 22000, 255, 0.02
            elif mode == 1: # Heavy mode
                fi,fm,numCar,dc = 20050, 21000, 255, 0.36
            # fileName = f'encodeFile{int(round(random.random()*100))}.wav'
            fileName = f'encodeFile.wav'
            filePath = f'{dataPath}\{fileName}'
            audioFile = enviar_mensagem(entrada = messageToEncode, filename=filePath, fi = fi, fm = fm, numCar = numCar, dc =dc)
            
            sendFile = send_file(
            filePath, 
            mimetype="audio/wav", 
            as_attachment=True, 
            download_name =fileName)

            return sendFile
        else:
            return 'Formato incorreto no POST ! Deve haver 1.encodeMsg = texto para codificar  ; 2.mode = modo de codificação(0: Light ; 1:Heavy)'

@app.route('/decodeWAV', methods = ['POST'])

def decodificar_mensagem():
    if request.method == 'POST':
        requestJson = request.json

        rawWavFile = request.data
        mode = requestJson['mode']

        if mode == 0: # light mode
            fi,fm,numCar,dc = 20, 22000, 255, 0.02
        elif mode == 1: # Heavy mode
            fi,fm,numCar,dc = 20050, 21000, 255, 0.36

        fileName = f'decodeFile.wav'
        filePath = f'{dataPath}\{fileName}'
        with open(filePath, mode='bx') as f:
            f.write(rawWavFile)
        message = decodificar_mensagem(fileName = fileName,fi = fi, fm = fm, numCar = numCar, dc = dc)

        return make_response(message)

    return 'AQUILO'