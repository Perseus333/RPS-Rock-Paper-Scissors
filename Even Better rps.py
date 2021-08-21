import random


table = {'r': 1, 'p': 2, 's': 3}


def attack_value(choice):
    return table[choice]


machine_attack = random.choice(['r', 'p', 's'])
player_attack = input('> ')

print(f'machine: {machine_attack}')


if attack_value(player_attack) > attack_value(machine_attack) or player_attack == 'r' and machine_attack == 's':
    print('you win')
    quit()

elif machine_attack == player_attack:
    print('draw')
    quit()

print('you lose')
