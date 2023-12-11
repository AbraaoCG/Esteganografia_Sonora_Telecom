from codigo_esteganografia.decodificador_bench import decodificar_mensagem
from codigo_esteganografia.codificador_bench import enviar_mensagem
# Definir frequência inicial, frequência máxima e número de caracteres
# permitidos a partir do primeiro ASCII
mensagem_env = 'Olá pessoal, esse é um teste do programa!! @!? > . < @#$%&* '
print(f'Mensagem enviada: {mensagem_env} \n')
fi = 20050 ; fm = 21000 ; numCar = 256 ; ta = 44100 ; dc = 0.46
while(1):
    
    enviar_mensagem(mensagem_env,fi = fi, fm = fm, numCar = numCar, dc= dc, ta= ta)

    mensagem_recebida = decodificar_mensagem(fi = fi, fm = fm, numCar = numCar,sg = dc)

    if(mensagem_env == mensagem_recebida):
        print(f'OK : fi = {fi} ; fm = {fm} ; numCar = {numCar} ; Hz/Caract = {(fm - fi) / numCar}, dc = {dc}, ta = {ta}')
    else:
        print(f'Not OK : fi = {fi} ; fm = {fm} ; numCar = {numCar}; Hz/Caract = {(fm - fi) / numCar} , dc = {dc}, ta = {ta}')
        
        print(f'Mensagem recebida: {mensagem_recebida} \n')
        break
    # fi += 1000
    #fi += 1000 ; fm += 1000
    # dc -= 0.01
    #fm -= 100
#print(f'Mensagem recebida: {mensagem_recebida}')