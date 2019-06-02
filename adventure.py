import time
import random

player_choices = {'NOME': 1809, 'ARMA': 1642, 'XP': 0}
#FUNÇÕES
def choice_arma():
    arma = input('''1 - ESPADA\n2 - ARCO\n3 - MACHADO
    ''')
    if arma == '1':
        arma = 'Espada'
        player_choices['ARMA'] = arma
    elif arma == '2':
        arma ='Arco'
        player_choices['ARMA'] = arma
    elif arma == '3':
        player_choices['ARMA']=arma
    else:
        print('Digite um valor correto')
        choice_arma()

def perfil():
    print('NOME: ', player_choices['NOME'])
    print('ARMA: ', player_choices['ARMA'])
    print('XP: ', player_choices['XP'])

def local1():
    print('='*40,'\nLOCAL: Vilazinha Pequena')
    print('O QUE FAZER?')
    escolha = input('''1 - VER PERFIL
2 - PROCURAR MONSTROS
3 - AVANÇAR
    ''')
    if escolha == '1':
        perfil()
    else:
        print('ERRO')

print('Seja bem-vindo(a) ao Simple Python Adventure Game')
time.sleep(0.5)
xp = 0
nome = input('Qual seu nome?')
player_choices['NOME'] = nome
time.sleep(0.5)
choice_arma()
local1()
