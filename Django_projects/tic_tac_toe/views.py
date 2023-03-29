from django.shortcuts import render

# Create your views here.

def show_hardcode_board(request):
    board = [[(1, 'X'), (2, 'X'), (3, 'X')], [(4, 'O'), (5, 'O'), (6, 'O')], [(7, 'X'), (8, 'X'), (9, 'X')]] 
    context = {'board': board, 'current_player': 'Aruvi'}
    return render(request, 'tic_tac_toe/hardcodeboard.html', context)    

def is_winning (vals):
    #[(1, 'x'), (2, 'x'), (3, 'x')]
    print(vals)
    return len(set([item[1] for item in vals])) == 1

def winner(board):
    #check rows
    for i in range(0, 3):
        if is_winning([board[i][0], board[i][1], board[i][2]]):
            return board[i][0][1]
    #check columns
    for i in range(0, 3):
        if is_winning([board[0][i], board[1][i], board[2][i]]):
            return board[0][i][1]
    #check negative diagonal
    if is_winning([board[0][0], board[1][1], board[2][2]]):
        return board[1][1][1]
    #check positive diagonal
    if is_winning([board[0][2], board[1][1], board[2][0]]):
        return board[1][1][1]
    return False

def show_board(request):
    players = [True, False]
    if request.method == 'GET':
        board = [[(1, ''), (2, ''), (3, '')], 
                 [(4, ''), (5, ''), (6, '')], 
                 [(7, ''), (8, ''), (9, '')]] 
        context = {'board': board}
    elif request.method == 'POST':
        board = [[(i, request.POST.get(str(i))) for i in range(1, 4)], 
                 [(i, request.POST.get(str(i))) for i in range(4, 7)], 
                 [(i, request.POST.get(str(i))) for i in range(7, 10)]]
        
        context = {'board': board, 'winner': winner(board)}
    return render(request, 'tic_tac_toe/board.html', context)