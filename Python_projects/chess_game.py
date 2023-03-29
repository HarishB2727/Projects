class Chess_game:
    chess_board_coins = {}
    def __init__(self):
        for i in range(1,9):
            for j in range(1,9):
                k = i*10 + j
                if i == 2:
                    Chess_game.chess_board_coins[k] = "p"
                elif i == 7:
                    Chess_game.chess_board_coins[k] = "P"
                else:
                    Chess_game.chess_board_coins[k] = " "
        Chess_game.chess_board_coins[11] = "h"
        Chess_game.chess_board_coins[12] = "l"
        Chess_game.chess_board_coins[13] = "c"
        Chess_game.chess_board_coins[14] = "k"
        Chess_game.chess_board_coins[15] = "m"
        Chess_game.chess_board_coins[16] = "c"
        Chess_game.chess_board_coins[17] = "l"
        Chess_game.chess_board_coins[18] = "h"
        Chess_game.chess_board_coins[81] = "H"
        Chess_game.chess_board_coins[82] = "L"
        Chess_game.chess_board_coins[83] = "C"
        Chess_game.chess_board_coins[84] = "M"
        Chess_game.chess_board_coins[85] = "K"
        Chess_game.chess_board_coins[86] = "C"
        Chess_game.chess_board_coins[87] = "L"
        Chess_game.chess_board_coins[88] = "H"

    def design(self):
        print(Chess_game.chess_board_coins)
        print('    1   2   3   4   5   6   7   8  ')
        for i in range(1,9):
            c = 0
            print(f'''   --- --- --- --- --- --- --- --- \n{i} | {Chess_game.chess_board_coins[i*10+(c+1)]} | {Chess_game.chess_board_coins[i*10+(c+2)]} | {Chess_game.chess_board_coins[i*10+(c+3)]} | {Chess_game.chess_board_coins[i*10+(c+4)]} | {Chess_game.chess_board_coins[i*10+(c+5)]} | {Chess_game.chess_board_coins[i*10+(c+6)]} | {Chess_game.chess_board_coins[i*10+(c+7)]} | {Chess_game.chess_board_coins[i*10+(c+8)]} | {i}''')
        print('   --- --- --- --- --- --- --- --- ')
        print('    1   2   3   4   5   6   7   8  ')
    
    
    def rules(self,coin_,position_):

        available_positions = []
        if Chess_game.chess_board_coins[coin_] in ['p', 'P']:
            # available_positions.append(coin_+10)
            if Chess_game.chess_board_coins[coin_] == 'p':
                if Chess_game.chess_board_coins[coin_+10] == " ":
                    available_positions.append(coin_+10)
                if available_positions.append(coin_+11) != " " and Chess_game.chess_board_coins[coin_+11].isupper():
                    available_positions.append(coin_+11)
                if available_positions.append(coin_+11-2) != " " and Chess_game.chess_board_coins[coin_+11].isupper():
                    available_positions.append(coin_+11-2)
            
            if Chess_game.chess_board_coins[coin_] == 'P':
                available_positions.append(coin_-10)
                if available_positions.append(coin_+11) != " " and Chess_game.chess_board_coins[coin_+11].islower():
                    available_positions.append(coin_-11)
            
            if position_ in available_positions:
                print(available_positions)
                return True
            else:
                print("give correct position")
                return False
                # available_positions.append(coin_+10)


            


        

    def start(self):

        player = 0
        
        while('k' in Chess_game.chess_board_coins.values() and 'K' in Chess_game.chess_board_coins.values()):
            coin_, position_ = input(f"Enter two values player{player%2 + 1}: ").split()
            if self.rules(int(coin_),int(position_)):
                Chess_game.chess_board_coins[int(position_)] =  Chess_game.chess_board_coins[int(coin_)]
                Chess_game.chess_board_coins[int(coin_)] = " "
            

            
            self.design()
            # print(x,y)
            player += 1
            

obj1 = Chess_game()

# obj1.design()
obj1.start()