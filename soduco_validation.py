def validation(board):
    valid=True
    #checking the rows
    
    for i in range(0,9):
        
        seen=set()
        for j in range(0,9):
            print("Number",board[i][j])
            if board[i][j]==".": 
                continue
            if not board[i][j] in seen:
                seen.add(board[i][j])
            else: 
                return False

    #checking the columns 
        for i in range(0,9):
            seen=set()
            for j in range(0,9):
                  if board[j][i]==".": 
                     continue
            if not board[i][j] in seen:
                seen.add(board[j][i])
            else: 
                return False
        
    #checking the squires
        i_limit=0
        for i in range(0,9,4):
            print(i,"i")
            for j in range(0,9,4):
                print("j",j)
                seen=set()
                for it in range(0,3):
                    for jt in range(0,3):
                        print("It",it,"jt",jt,"Number",board[i+it][j+jt])
                        print("Seen",seen)
                        if board[i+it][j+jt]==".":
                            continue
                        if board[i+it][j+jt] not in seen:
                            print("in")
                            seen.add(board[i+it][j+it])
                        else: 
                            return False


    return valid



print(validation([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))