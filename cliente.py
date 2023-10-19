from codigo_esteganografia.decodificador import decodificar_mensagem
from codigo_esteganografia.codificador import enviar_mensagem


mensagem_env = 'Olá pessoal, esse é um teste do programa!! @!? > . < @#$%&* '


print(f'Mensagem enviada: {mensagem_env} \n')
enviar_mensagem(mensagem_env)

mensagem_recebida = decodificar_mensagem()

print(f'Mensagem recebida: {mensagem_recebida}')