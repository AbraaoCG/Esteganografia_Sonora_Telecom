from flask import Flask, request, redirect, url_for, jsonify, flash
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

@app.route('/encodeWAV', methods = ['GET','POST'] )
def codificar_mensagem():
    if request.method == 'POST':
        
        data = request.json
        messageToEncode = data['encodeMsg']
        mode = data['mode']

        if mode == 0: # light mode
            fi,fm,numCar = 20, 21000, 255
        elif mode == 1: # Heavy mode
            fi,fm,numCar = 20050, 21000, 255
        fileName = f'file{int(round(random.random()*100))}.wav'
        filePath = f'{dataPath}\{fileName}'
        enviar_mensagem(entrada = messageToEncode, filename=filePath, fi = fi, fm = fm, numCar = numCar)

        print(mode)
        return 'CARAI VIADO'

@app.route('/decodeWAV')

def hello3():
    return 'AQUILO'