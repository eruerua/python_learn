def validSolution(board):
    for i in range(9):
        m = board[i]
        n = [a[i] for a in board]
        if 0 in m or 0 in n or len(set(m)) != 9 or len(set(n)) != 9:
            return False
    for k in range(3):
        for i in range(3):
            l=[]
            for j in range(3):
                l+=board[j+k*3][i*3:i*3+3]
            print(l)
            if len(set(l))!=9:
                return False
    return True


print(validSolution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                     [4, 9, 8, 2, 6, 1, 3, 7, 5],
                     [7, 5, 6, 3, 8, 4, 2, 1, 9],
                     [6, 4, 3, 1, 5, 8, 7, 9, 2],
                     [5, 2, 1, 7, 9, 3, 8, 4, 6],
                     [9, 8, 7, 4, 2, 6, 5, 3, 1],
                     [2, 1, 4, 9, 3, 5, 6, 8, 7],
                     [3, 6, 5, 8, 1, 7, 9, 2, 4],
                     [8, 7, 9, 6, 4, 2, 1, 3, 5]]))

