import random

start_game = 'p'
player_score = 0
com_score = 0

while start_game == 'p':
    input_text = input("Rock (r), Paper (p) ,Scissor (s)").lower()
    while input_text not in ('r','p','s'):
        print('Wrong input')
        input_text = input("Rock (r), Paper (p) ,Scissor (s)").lower()

#####################################################################################################################
# Computer turn
#####################################################################################################################
    rand = random.randint(1,3)
    if rand == 1:
        com = 'p'
    elif rand == 2:
        com = 'r'
    else:
        com ='s'

#####################################################################################################################
# Game Result
#####################################################################################################################

    if input_text == com:
        print(input_text,'VS',com)
        print('Draw!!')
        print('Player: ',player_score,' ','Com: ',com_score)
    elif input_text =='p' and com == 's':
        print(input_text,'VS',com)
        com_score = com_score +1
        print('You Lose')
        print('Player: ', player_score, ' ', 'Com: ', com_score)
    elif input_text =='r' and com == 'p':
        print(input_text,'VS',com)
        com_score = com_score +1
        print('You Lose')
        print('Player: ', player_score, ' ', 'Com: ', com_score)
    elif input_text =='s' and com == 'r':
        print(input_text,'VS',com)
        com_score = com_score +1
        print('You Lose')
        print('Player: ', player_score, ' ', 'Com: ', com_score)
    elif input_text =='s' and com == 'p':
        print(input_text,'VS',com)
        print('You Win')
        player_score = player_score +1
        print('Player: ', player_score, ' ', 'Com: ', com_score)
    elif input_text =='p' and com == 'r':
        print(input_text,'VS',com)
        print('You Win')
        player_score = player_score +1
        print('Player: ', player_score, ' ', 'Com: ', com_score)
    elif input_text =='r' and com == 's':
        print(input_text,'VS',com)
        print('You Win')
        player_score = player_score +1
        print('Player: ', player_score, ' ', 'Com: ', com_score)

    start_game = input('Play again (P) or Quit (Q): ').lower()
    if start_game == 'q':
        print('Good Bye!')


        

