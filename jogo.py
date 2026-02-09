from random import randint
from time import sleep

computador = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

try:
    jogador = int(input('Em que número eu pensei? '))
except ValueError:
    print('Por favor, digite um número válido!')
    exit()

if jogador < 0 or jogador > 5:
    print('Digite um número entre 0 e 5!')
    exit()

print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador}!')
