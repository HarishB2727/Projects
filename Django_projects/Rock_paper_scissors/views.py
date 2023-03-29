from django.shortcuts import render


def game_function(request):
    # if request.method == "POST" and 'txt' in request.POST:
    #     print(request.POST.get('txt'))
    player1 = request.POST.get('player1')
    player2 = request.POST.get('player2')
    print(player1,player2)
    context = {'winner': winner(player1,player2), 'player1':player1, 'player2':player2}
    return render(request, 'Rock_paper_scissors/RPS_game.html', context)

def winner(player1,player2):
    if player1 == player2:
        return "Draw Match"
    else:
        if player1 == "rock" and player2 == "scissor":
            return "player 1 Won"
        elif player1 == "rock" and player2 == "paper":
            return "player 2 won"
        elif player1 == "scissor" and player2 == "paper":
            return "player 1 won"
        elif player1 == "paper" and player2 == "scissor":
            return "player 2 won"
        elif player1 == "paper" and player2 == "rock":
            return "player 1 won"
        elif player1 == "scissor" and player2 == "rock":
            return "player 2 won"
        else:
            return "waiting for condition"

# Create your views here.
