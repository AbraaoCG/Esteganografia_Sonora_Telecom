from codigo_esteganografia.decodificador import decodificar_mensagem
from codigo_esteganografia.codificador import enviar_mensagem

# Definir frequência inicial, frequência máxima e número de caracteres
# permitidos a partir do primeiro ASCII
fi = 50 ; fm = 661 ; numCar = 256

mensagem_env = 'Olá pessoal, esse é um teste do programa!! @!? > . < @#$%&* '


print(f'Mensagem enviada: {mensagem_env} \n')
enviar_mensagem(mensagem_env,fi = fi, fm = fm, numCar = numCar)

mensagem_recebida = decodificar_mensagem(fi = fi, fm = fm, numCar = numCar)

print(f'Mensagem recebida: {mensagem_recebida}')