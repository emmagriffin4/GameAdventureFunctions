#fortune.py
#Emma Griffin
#2/9/2025

#The fortune teller's I used growing up included colors
#so my code includes colors and numbers!

player_color = input('Pick a color: red, green, blue, or yellow\n')

if player_color == 'red' or player_color == 'green':
    player_num = int(input('Pick a number: 2, 4, 6, or 8\n'))
    if player_num == 2 and player_color == 'red':
        print('You are going to be rich!')
    elif player_num == 2 and player_color == 'green':
        print('You are going to be poor.')
    elif player_num == 4 and player_color == 'red':
        print('You are going to be President of Mars!')
    elif player_num == 4 and player_color == 'green':
        print ('You are going to live in a cave with wolves.')
    elif player_num == 6 and player_color == 'red':
        print ('ou make a joke and everyone thinks you are funny and wants to be your friend!')
    elif player_num == 6 and player_color == 'green':
        print ('You are going to be eaten by lions at the zoo!')
    elif player_num == 8 and player_color == 'red':
        print ('You will be offered your dream job!')
    elif player_num == 8 and player_color == 'green':
        print ('You will win the lottery, but then get robbed and lose all the money.')
    else:
        print('Error: restart program and be sure to select a number from the given list!')
elif player_color == 'blue' or player_color == 'yellow':
    player_num = int(input('Pick a number: 1, 3, 5, or 7\n'))
    if player_num == 1 or 3 or 5 or 7:
        if player_num == 1 and player_color == 'blue':
            print('You will win the lottery, but then get robbed and lose all the money.')
        elif player_num == 1 and player_color == 'yellow':
            print('You will be offered your dream job!')
        elif player_num == 3 and player_color == 'blue':
            print('You are going to be eaten by lions at the zoo!')
        elif player_num == 3 and player_color == 'yellow':
            print('You make a joke and everyone thinks you are funny and wants to be your friend!')
        elif player_num == 5 and player_color == 'blue':
            print('You are going to be rich!')
        elif player_num == 5 and player_color == 'yellow':
            print('You are going to be poor.')
        elif player_num == 7 and player_color == 'blue':
            print('You are going to be President of Mars!')
        elif player_num == 7 and player_color == 'yellow':
            print ('You are going to live in a cave with wolves.')
        else:
            print('Error: restart program and be sure to select a number from the given list!')
else:
    print('Error: restart program and be sure to select a color from the given list!')

         
            

