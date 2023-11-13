board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(board):
    find = find_empty(board)
    if not find:
        print_board(board)
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if validate(board, i, row, col):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False


def validate(board, num, row, col):
    # check row
    for i in range(len(board[0])):
        '''
        If the position we're looking in has the number, and it's not in the position we specify
        This means the number exists in the row already and is not a valid answer
        '''
        if board[row][i] == num and col != i:
            return False
        
    # check col
    for j in range(len(board)):
        '''
        Follows same pattern:
        If the position we're looking for has the number, and it's not in the position we want to put the number in
        The number exists in the column, therefore it's not a valid answer.
        '''
        if board[j][col] == num and row != j:
            return False
        
    # check box
    
    # Calibrate what box you're in
    box_x = col // 3
    box_y = row // 3

    # Cycle through the boxes
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            '''
            If the number in that position has the number we want to input, but is not in the row and column we want it in
            It's not the right answer and we just return False
            '''
            if board[i][j] == num and i != row and j != col:
                return False
    
    # If all tests pass, we return True
    return True

def print_board(board):
    for i in range(0, len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(0, len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(f"{str(board[i][j])} ", end="")

def find_empty(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == 0:
                return (i, j) #Row, Column

print_board(board)
print()
solve(board)