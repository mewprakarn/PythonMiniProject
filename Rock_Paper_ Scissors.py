import random
input_text = input("Rock (r), Paper (p) ,Scissor (s)")
while input_text not in ('r','p','s'):
    print('Wrong input')
    input_text = input("Rock (r), Paper (p) ,Scissor (s)")

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
elif input_text =='p' and com == 's':
    print(input_text,'VS',com)
    print('You Lose')
elif input_text =='r' and com == 'p':
    print(input_text,'VS',com)
    print('You Lose')
elif input_text =='s' and com == 'r':
    print(input_text,'VS',com)
    print('You Lose')
elif input_text =='s' and com == 'p':
    print(input_text,'VS',com)
    print('You Win')
elif input_text =='p' and com == 'r':
    print(input_text,'VS',com)
    print('You Win')
elif input_text =='r' and com == 's':
    print(input_text,'VS',com)
    print('You Win')
            

        

