import random
player_score = 0
bot_score = 0
try:
    while 4 > 1:
        class Dice:
            def roll(self):
                return str(random.randint(1, 3))
        table = {
            '1': 'rock',
            '2': 'paper',
            '3': 'scissors'
        }

        dice = Dice()
        player = Dice()
        bot = Dice()
        player = input('> ')
        player_table = {
            'p': 'paper',
            'r': 'rock',
            's': 'scissors'
        }
        player = player_table[player]
        bot = dice.roll()

        if player == table[bot]:
            print(f'You both got: {table[bot]}, and nothing happens.')
            print(f'You: {player_score}')
            print(f'Bot: {bot_score}')

        elif player == 'paper' and table[bot] == 'scissors':
            print(f'Their scissors cut through your paper')
            bot_score += 1
            print(f'You: {player_score}')
            print(f'Bot {bot_score}')

        elif player == 'paper' and table[bot] == 'rock':
            print(f'You catch his rock')
            player_score += 1
            print(f'You: {player_score}')
            print(f'Bot {bot_score}')

        elif player == 'scissors' and table[bot] == 'paper':
            print('You cut through his paper')
            player_score += 1
            print(f'You: {player_score}')
            print(f'Bot {bot_score}')

        elif player == 'scissors' and table[bot] == 'rock':
            print('Its rock smashes your fragile blades')
            bot_score += 1
            print(f'You: {player_score}')
            print(f'Bot {bot_score}')

        elif player == 'rock' and table[bot] == 'scissors':
            print('Your rock crashes into pieces their weak scissors')
            player_score += 1
            print(f'You: {player_score}')
            print(f'Bot {bot_score}')

        elif player == 'rock' and table[bot] == 'paper':
            print('Its paper surrounds your rock ')
            bot_score += 1
            print(f'You: {player_score}')
            print(f'Bot {bot_score}')
        else:
            print(f'{player} is not a valid play. Try typing rock, paper or scissors')
except KeyError:
    print('You messsed up something...')
