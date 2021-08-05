import random
machine_table = {
    1: 'p',
    2: 's',
    3: 'r'
}


def victory():
    print('player wins')


def defeat():
    print('machine wins')


machine_attack = machine_table[random.randint(1, 3)]

player_attack = str(input('> ').lower())

if machine_attack == 'p' and player_attack == 'r':
    defeat()

elif machine_attack == 'p' and player_attack == 's':
    victory()

elif machine_attack == 'r' and player_attack == 'p':
    victory()

elif machine_attack == 'r' and player_attack == 's':
    defeat()

elif machine_attack == 's' and player_attack == 'p':
    defeat()

elif machine_attack == 's' and player_attack == 'r':
    victory()

elif machine_attack == player_attack:
    print('draw')

else:
    print('you messed up something...')
