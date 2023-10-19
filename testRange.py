from codigo_esteganografia.decodificador import decodificar_mensagem
from codigo_esteganografia.codificador import enviar_mensagem

fi = 15000 ; fm = 16000 ; numCar = 256 ; ta = 44100 ; dc = 0.5
while(1):
    # Definir frequência inicial, frequência máxima e número de caracteres
    # permitidos a partir do primeiro ASCII
    
    mensagem_env = 'Olá pessoal, esse é um teste do programa!! @!? > . < @#$%&* '

    #print(f'Mensagem enviada: {mensagem_env} \n')
    enviar_mensagem(mensagem_env,fi = fi, fm = fm, numCar = numCar)

    mensagem_recebida = decodificar_mensagem(fi = fi, fm = fm, numCar = numCar)

    if(mensagem_env == mensagem_recebida):
        print(f'OK : fi = {fi} ; fm = {fm} ; numCar = {numCar} ; Hz/Caract = {(fm - fi) / numCar}')
    else:
        print(f'Not OK : fi = {fi} ; fm = {fm} ; numCar = {numCar}; Hz/Caract = {(fm - fi) / numCar}')
        break
    fm -= 100
#print(f'Mensagem recebida: {mensagem_recebida}')