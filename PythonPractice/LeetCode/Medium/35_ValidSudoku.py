def isValidSudoku(board):
    if(not board):
        return False
    
    for i in range(9):
        dict_row = {}
        dict_column = {}
        for j in range(9):
            if(board[i][j] != "." and board[i][j] in dict_row):
                return False
            else:
                dict_row[board[i][j]] = 1
            
            if(board[j][i] != "." and board[j][i] in dict_column):
                return False
            else:
                dict_column[board[j][i]] = 1
    
    
    outer_mul = 1
    while(outer_mul <= 3):
        s = 3*(outer_mul - 1)
        e = 3*(outer_mul)
        multiplier = 1
        while(multiplier <= 3):
            start = 3*(multiplier - 1)
            end = 3*multiplier
            dict = {}
            for i in range(s,e):
                for j in range(start,end):
                    if(board[i][j] != "." and board[i][j] in dict):
                        return False
                    else:
                        dict[board[i][j]] = 1

            multiplier += 1
        outer_mul += 1
    
    return True

board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))