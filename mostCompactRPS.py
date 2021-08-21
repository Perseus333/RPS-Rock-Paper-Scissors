import random
table = {'r': 1, 'p': 2, 's': 3}
machine_attack = random.choice(['r', 'p', 's'])
player_attack = input('> ')
if table[player_attack] > table[machine_attack] or player_attack == 'r' and machine_attack == 's': print(f'{machine_attack}, you win')
elif player_attack == machine_attack: print('draw')
else: print(f'{machine_attack} you lose')