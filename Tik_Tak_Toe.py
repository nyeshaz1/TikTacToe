from random import randrange

def display_board(board):
    print("+-------" *3 , "+" , sep="")
    for row in range (3):
        print("|       "*3 , "|" , sep="")
        for col in range(3):
            print("|   " + str(board[row][col])+ "   ", end="")
        print("|")
        print("|       "*3 , "|" , sep="")
        print("+-------" *3 , "+" , sep="")
def enter_move(board):
    ok=False;
    while not ok:
        move = input("Enter your move : ")
        ok=len(move)==1 and move >='1' and move <= '9'
        if not ok:
            print("Bad move - rpeat your input!")
            continue
        move=int(move)-1
        row=move // 3
        col=move % 3
        done=board[row][col]
        ok = done not in ['o','x']
        if not ok :
            print("Field already occupied - try again ")
            continue
        board[row][col]='o'
    
def make_list_of_free_fields(board):
    free=[]    
    for i in range (3):
        for j in range (3):
            if board[i][j] not in ['x' , 'o' ]:
                free.append((i,j))
    return free
def victory_for(board,sgn):
    if sgn=='x':
        who="me"
    elif sgn=='o':
        who="you"
    else:
         who=None
    dig1 = dig2 = True
    for rc in range(3):
         if board[rc][0]==sgn and board[rc][1]==sgn and board[rc][2]==sgn:
             return who
         if board[0][rc]==sgn and board[1][rc]==sgn and board[2][rc]==sgn:
             return who
         if board[rc][rc]!=sgn:
              dig1= False
         if board[rc][2-rc]!=sgn:
              dig2=False
    if dig1 or dig2 :
         return who
    return None   
         
    
 
def draw_move(board):
    free=make_list_of_free_fields(board)
    count=len(free)
    if count > 0:
        move = randrange(count)
        row , col = free[move]
        board[row][col]='x'
board=[]
k=0
for i in range(3):
    row=[]
    for j in range(3):
        k+=1
        row.append(k)

    board.append(row)
    
board[1][1]='x'    
print(board)
free=make_list_of_free_fields(board)

human_turn=True
while free:
    display_board(board)
    if human_turn:
        enter_move(board)
        victory=victory_for(board,'o')
    else :
        draw_move(board)
        victory=victory_for(board,'x')
    if victory!=None:
        break
    human_turn = not human_turn
    free=make_list_of_free_fields(board)


display_board(board)
if victory == 'you':
    print('You won!')
elif victory == 'me' :
    print('I won')
else:
    print('Tie!')

    
    
