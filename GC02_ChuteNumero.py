import random
from time import sleep
import emoji
w = l = 0

print('\033[1;31m==\033[m' * 15)
print(emoji.emojize('\033[1mGAME - CHUTE UM NÚMERO :video_game:\033[m'))
print('\033[1;31m==\033[m' * 15)

while True:
    cont = False
    resp = 1
    cond = 'X'
    n = random.randint(1, 10)
    #print(n)

    resp = int(input('\033[1mDigite um número de\033[m \033[1;31m1 a 10\033[1m: '))
    if resp >= 1 and resp <= 10:
        cont = True
    else:
        print('\033[1mErro! Digite um número entre 1 e 10\033[m')

    if cont == True:
        print('\033[1mSorteando número...\033[m')
        sleep(2)
        print('\033[1;35m=-\033[m' * 15)
        if resp == n:
            print(f'\033[1mNuméro sortido:\033[m {n}')
            print('\033[1mParabéns! Você acertou.\033[m')
            w += 1
            print('\033[1;35m=-\033[m' * 15)
        else:
            print(f'\033[1mNuméro sortido:\033[m {n}')
            print('\033[1mVocê errou! Mais sorte na proxima vez.\033[m')
            l += 1
            print('\033[1;35m=-\033[m' * 15)
        while cond != 'S' and cond !='N':
            cond = str(input('\033[1mDeseja continuar?\033[m \033[1;34m[S/N]\033[m ')).upper().rstrip().lstrip()
        if cond == 'N':
            print('\033[1;31m==\033[m' * 15)
            print('\033[1mPLACAR\033[m')
            print(f'\033[1mVocê jogou {w+l} vezes. Ganhou\033[m \033[1;34m{w}\033[m e perdeu \033[1;31m{l}\033[m')
            print('\033[1mPrograma encerrado. Volte sempre!\033[m')
            print('\033[1;31m==\033[m' * 15)
            break
