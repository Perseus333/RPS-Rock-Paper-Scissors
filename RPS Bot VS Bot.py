import random
player_score = 0
bot_score = 0
play_round = 0
tries = 0


class Dice:
    def roll(self):
        return random.randint(1, 3)


player_bot = Dice()
bot = Dice()
allowed_tries = int(input('Select the rounds of the game: '))

table = {
    '1': 'S',
    '2': 'P',
    '3': 'R'
}
print('                      Player Bot')
while tries < allowed_tries:
    tries += 1

    action_player = player_bot.roll()
    action_bot = bot.roll()

    bot_output = table[str(action_bot)]
    player_output = table[str(action_player)]


    play_round += 1
    if action_bot == action_player:
        print(f'Round {play_round} was a draw      | {player_output} - {bot_output}')

    elif action_bot == 1 and action_player == 3:
        print(f'Player won the round: {play_round} | {player_output} - {bot_output}')
        player_score += 1

    elif action_bot == 2 and action_player == 3:
        print(f'Bot won the round: {play_round}    | {player_output} - {bot_output}')
        bot_score += 1

    elif action_bot == 1 and action_player == 2:
        print(f'Player won the round: {play_round} | {player_output} - {bot_output}')
        player_score += 1

    elif action_bot == 3 and action_player == 2:
        print(f'Bot won the round: {play_round}    | {player_output} - {bot_output}')
        bot_score += 1

    elif action_bot == 2 and action_player == 1:
        print(f'Bot won the round: {play_round}    | {player_output} - {bot_output}')
        bot_score += 1

    elif action_bot == 3 and action_player == 1:
        print(f'Player won the round: {play_round} | {player_output} - {bot_output}')
        player_score += 1

print('==============================')
print(f'Player total score is: {player_score}')
print(f'Bot total score is: {bot_score}')
if player_score > bot_score:
    print(f'You won!')
elif player_score == bot_score:
    print('It was a draw!')
else:
    print('You lost')
