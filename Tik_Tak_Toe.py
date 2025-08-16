from random import randrange

def display_board(board):
    print("+-------" *3 , "+" , sep="") #top line
    for row in range (3):
        print("|       "*3 , "|" , sep="")#three rows 
        for col in range(3):
            print("|   " + str(board[row][col])+ "   ", end="") #adding numbers in them 
        print("|")
        print("|       "*3 , "|" , sep="")
        print("+-------" *3 , "+" , sep="")
def enter_move(board):
    ok=False #assuming to enter in the loop 
    while not ok:
        move = input("Enter your move : ") # take input until its correct 
        ok=len(move)==1 and move >='1' and move <= '9' #length check and number in range check 
        if not ok:
            print("Bad move - rpeat your input!")
            continue
        move=int(move)-1 #for correct indexing 
        row=move // 3 # for positioning row 
        col=move % 3 # for column
        done=board[row][col]
        ok = done not in ['o','x'] #check if not already occupied
        if not ok : 
            print("Field already occupied - try again ")
            continue #if already occupied than again enter your move 
        board[row][col]='o' # if not , so occupied by you 
    
def make_list_of_free_fields(board):
    free=[]    
    for i in range (3): #checking all rows 
        for j in range (3): # all cols 
            if board[i][j] not in ['x' , 'o' ]: # check if free or ocuupied 
                free.append((i,j))  #if free so make tuple of free boxes 
    return free
def victory_for(board,sgn):
    if sgn=='x':
        who="me"
    elif sgn=='o':
        who="you"
    else:
         who=None
    dig1 = dig2 = True #digonal
    for rc in range(3):
         if board[rc][0]==sgn and board[rc][1]==sgn and board[rc][2]==sgn: #all rows check 
             return who
         if board[0][rc]==sgn and board[1][rc]==sgn and board[2][rc]==sgn: #all cols check
             return who
         if board[rc][rc]!=sgn: #main diagonal check , if any box is not sgn so make it false 
              dig1= False
         if board[rc][2-rc]!=sgn: #secondary digonal check , if any box is not equal to sgn , make dig2 false 
              dig2=False
    if dig1 or dig2 : # check if any diagonal is remained true 
         return who
    return None   
         
    
 
def draw_move(board): # move of comp aka me 
    free=make_list_of_free_fields(board) # so check is there is any remaining free box 
    count=len(free) # count how many are free 
    if count > 0: # if count is more than zero 
        move = randrange(count) #select any number from available count 
        row , col = free[move] #select that free box using that count number 
        board[row][col]='x' #and occupy with x 
board=[]
k=0
for i in range(3): # rows of board 
    row=[]
    for j in range(3): #cols of board 
        k+=1
        row.append(k) #number them 

    board.append(row) #qppend to final board 
    
board[1][1]='x'  #fixed first x at the center    

free=make_list_of_free_fields(board) #checking free boxes 

human_turn=True #starting from human's turn
while free: #means while True , until free boxes available 
    display_board(board) #display the board 
    if human_turn:
        enter_move(board) #humans turn to enter move 
        victory=victory_for(board,'o') #after every move check for victory 
    else :
        draw_move(board) #if human turn is false then its computer's turn 
        victory=victory_for(board,'x') #ahm ahm , check for my victory 
    if victory!=None: #if none so break this loop 
        break
    human_turn = not human_turn #cheanging the flag to continue 
    free=make_list_of_free_fields(board) #checing remianing free boxes 


display_board(board)
if victory == 'you':
    print('You won!') #if human won so display the message 
elif victory == 'me' :
    print('I won') #and computer won 
else:
    print('Tie!')

    
    
