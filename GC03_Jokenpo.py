import random
from time import sleep
import emoji

#HEADER
print('\033[1;31m==\033[m' * 15)
print(emoji.emojize(f'\033[1m{"GAME - JOKENPO! :video_game:":^40}\033[m'))

#BACK-END
while True:
    print('\033[1;31m==\033[m' * 15)
    n = int(input(emoji.emojize('\033[1mEscolha o que deseja jogar \n1- Pedra'
                  '\n2- Papel'
                  '\n3- Tesoura'
                  '\nOpção: \033[m')))

    if 1 <= n <= 3:
        print('\033[1;31m==\033[m' * 15)
        pc = random.randint(1, 3)

        print('\033[1mVocê escolheu:\033[m ', end='')
        if n == 1:
            print('\033[1mPedra\033[m')
        elif n == 2:
            print('\033[1mPapel\033[m')
        else:
            print('\033[1mTesoura\033[m')

        print('\033[1mA máquina escolheu:\033[m ', end='')
        if pc == 1:
            print('\033[1mPedra\033[m')
        elif pc == 2:
            print('\033[1mPapel\033[m')
        else:
            print('\033[1mTesoura\033[m')

        #SAIDA DE DADOS
        if n == 1 and pc == 3 or n == 2 and pc == 1 or n == 3 and pc == 2:
            print('\033[1mParabens! Você ganhou\033[m')
        elif n == pc:
            print('\033[1mWOW! Houve um empate\033[m')
        else:
            print('\033[1mVocê perdeu! Mais sorte na proxima vez.\033[m')
    else:
        print('\033[1mErro! Digite uma opção válida\033[m')

    #Deseja continuar?
    print('\033[1;31m==\033[m' * 15)
    cond = (input('\033[1mDeseja continuar?\033[m \033[1;34m[S/N]\033[m ')).upper().rstrip().lstrip()
    while cond != 'S' and cond != 'N':
        cond = (input('\033[1mErro!Digite uma opção válida: \033[m \033[1;34m[S/N]\033[m ')).upper().rstrip().lstrip()
        print('\033[1mErro! Digite uma opção válida\033[m')
    else:
        if cond == 'N':
            print('\033[1mPrograma encerrado. Volte sempre!\033[m')
            break