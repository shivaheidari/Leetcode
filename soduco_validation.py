def validation(board):
    valid=True

    #checking the rows
    for i in range(0,9):
        seen=set()
        for j in range(0,9):
            if board[i][j]!=".": 
                
               if not board[i][j] in seen:
                  seen.add(board[i][j])
               else: 
                  return False

    #checking the columns 
    for i in range(0,9):
            seen=set()
            for j in range(0,9):
              if board[j][i]!=".": 
                if not board[j][i] in seen:
                    seen.add(board[j][i])
                    print("seen",seen)
                else: 
                    return False

        
    #checking the squares
    for i in range(0,9,3):
            print(i,"i")
            for j in range(0,9,3):
                print("j",j)
                seen=set()
                for it in range(0,3):
                    for jt in range(0,3):
                        number=board[i+it][j+jt]
                        if number != ".": 
                            if number not in seen:
                                seen.add(number)
                                print(seen)
                            else: 
                                 return False


    return valid



print(validation([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))
def board_print(board):
    for i in range(0,9):
            print(board[i])

board_print(board_print([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))