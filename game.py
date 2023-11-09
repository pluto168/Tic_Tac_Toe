counter = 0

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)
    
def user_choice():
    choice = input("Please enter your number(1~9): ")
    while not choice.isdigit() or (int(choice) not in range(1,10)):
        if not choice.isdigit(): 
            print("Sorry, your choice is not a valid")
    
        else:
            print("Your choice is not within the range of 1 - 9.") 
        choice = input("Please enter your number(1~9): ")
    return int(choice ) 
        
# display(row1, row2, row3)

# user_choice()

def getCurrentSymbol():
    global counter 
    symbol_list = ['X','O'] 
    
    counter += 1
    return symbol_list[counter % 2 ]

# print (getCurrentSymbol())

def update_table(index):
    global row1, row2, row3
    if index in range(1,4):
        if row1[index - 1] == ' ':
            row1[index - 1] = getCurrentSymbol()
            return  True
        else:
            return False
    elif index in range(4,7):
        if row2[index % 3 - 1 ] == ' ':
            row2[index % 3 - 1 ] = getCurrentSymbol()
            return True
        else:
            return False
    else:
        if row3[index % 3 - 1 ] == ' ':
            row3[index % 3 - 1 ] = getCurrentSymbol()
            return True
        else:
            return False

def check_winning():
    player_1_win = False
    player_2_win = False
    if (row1[0] == row1[1] and row1[1] == row1[2] and (" " not in row1)):
        if(row1[0] == "X"):
            player_2_win = True
        else:
            player_1_win = True
    elif (row2[0] == row2[1] and row2[1] == row2[2] and (" " not in row2)):
        if(row2[0] == "X"):
            player_2_win = True
        elif(row2[0] == "O"):
            player_1_win = True
    elif (row3[0] == row3[1] and row3[1] == row3[2] and (" " not in row3)):
        if(row3[0] == "X"):
            player_2_win = True
        elif(row3[0] == "O"):
            player_1_win = True
            
    elif (row1[0] == row2[0] and row2[0] == row3[0] and (row1[0] != " " and row2[0] != " " and row3[0] != " ")):
        if(row1[0] == "X"):
            player_2_win = True
        elif(row1[0] == "O"):
            player_1_win = True
    elif (row1[1] == row2[1] and row2[1] == row3[1] and (row1[1] != " " and row2[1] != " " and row3[1] != " ")):
        if(row1[1] == "X"):
            player_2_win = True
        elif(row1[1] == "O"):
            player_1_win = True    
    elif (row1[2] == row2[2] and row2[2] == row3[2] and (row1[2] != " " and row2[2] != " " and row3[2] != " ")):
        if(row1[2] == "X"):
            player_2_win = True
        elif(row1[2] == "O"):
            player_1_win = True   
                
    #對角            
    elif (row1[0] == row2[1] and row2[1] == row3[2] and (row1[0] != " " and row2[1] != " " and row3[2] != " ")):
        if(row1[0] == "X"):
            player_2_win = True
        elif(row1[0] == "O"):
            player_1_win = True              
    elif (row1[2] == row2[1] and row2[1] == row3[0] and (row1[2] != " " and row2[1] != " " and row3[0] != " ")):
        if(row1[2] == "X"):
            player_2_win = True
        elif(row1[2] == "O"):
            player_1_win = True      
            
            
    if player_1_win:
        return "player_1_win"
    elif player_2_win:
        return "player_2_win"
    else:
        return "no one wins"
            
def start_game():
    while True:
        display(row1, row2, row3)
        while True:
            choice = user_choice()
            if update_table(choice):
                break
            else:
                print("Wrong position to put your choice")
                
        result = check_winning()
        if result == "player_1_win":
            display(row1, row2, row3)
            print("Player 1 wins!! congrats")
            return 
        elif result == "player_2_win":
            display(row1, row2, row3)
            print("Player 2 wins!! congrats")
            return 
        

start_game()