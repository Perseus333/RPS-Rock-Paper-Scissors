import random
machine_attack,player_attack,table=random.choice(['r','p','s']),input('>'),{'r':1,'p':2,'s':3}
if table[player_attack]>table[machine_attack]or player_attack=='r'and machine_attack=='s':print(f'{machine_attack},win')
elif player_attack==machine_attack:print('draw')
else:print(f'{machine_attack},lose')
