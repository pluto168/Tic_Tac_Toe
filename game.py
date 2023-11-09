counter = 0

row1 = ['','','']
row2 = ['','','']
row3 = ['','','']

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
        row1[index - 1] = getCurrentSymbol()
    elif index in range(4,7):
        row2[index % 3 - 1 ] = getCurrentSymbol()
    else:
        row3[index % 3 - 1 ] = getCurrentSymbol()

# update_table(1) #O
# update_table(4) #X
# update_table(7) #O
# update_table(8) #X
# update_table(2) #O

# display(row1, row2, row3)
    

def start_game():
    while True:
        display(row1, row2, row3)
        choice = user_choice()
        update_table(choice)
        

start_game()