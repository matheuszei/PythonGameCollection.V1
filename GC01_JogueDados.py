import random
from time import sleep
import emoji

print('\033[1;31m==\033[m' * 15)
print(emoji.emojize('\033[1mGAME - JOGANDO DADOS :video_game: :\033[m'))
print('\033[1;31m==\033[m' * 15)

while True:
    resp = 'X'
    while resp != 'S' and resp !='N':
        resp = str(input('\033[1mDeseja jogar o dado?\033[m \033[1;34m[S/N] \033[m')).upper().rstrip().lstrip()
        if resp != 'S' and resp !='N':
            print('\033[1mDigite uma informação válida!\033[m')
        if resp == 'S':
            n = random.randint(1, 6)
            print('\033[1;35m=-\033[m' * 15)
            print(emoji.emojize('\033[1mJOGANDO O DADO... :game_die: \033[m'))
            sleep(2)
            print(f'\033[1mNúmero sortido: \033[m\033[1;31m{n}\033[m')
            print('\033[1;35m=-\033[m' * 15)
    if resp == 'N':
         break

print('\033[1mPrograma encerrado. Volte sempre!\033[m')



