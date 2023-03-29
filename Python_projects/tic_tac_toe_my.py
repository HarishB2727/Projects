class Tic_Tac_Toe:
    value_ = True
    k = 0
    
    def __init__(self):
        print("instruction:")
        
        self.dict1_= {11:'11', 12:'12',13:'13',21:'21',22:'22',23:'23',31:'31',32:'32',33:'33'}
        
        print(f"""- -- -- -- -- -- -- -\n|  {self.dict1_[11]}  |  {self.dict1_[12]}  |  {self.dict1_[13]} |\n- -- -- -- -- -- -- -\n|  {self.dict1_[21]}  |  {self.dict1_[22]}  |  {self.dict1_[23]} |\n- -- -- -- -- -- -- -\n|  {self.dict1_[31]}  |  {self.dict1_[32]}  |  {self.dict1_[33]} |\n- -- -- -- -- -- -- -""")
        print('place your coins at given locations above ^^^^^\n')
        
        self.dict_ = {11:' ', 12:' ',13:' ',21:' ',22:' ',23:' ',31:' ',32:' ',33:' '}
        
        print(f"""- -- -- -- -- -- -\n|  {self.dict_[11]}  |  {self.dict_[12]}  |  {self.dict_[13]} |\n- -- -- -- -- -- -\n|  {self.dict_[21]}  |  {self.dict_[22]}  |  {self.dict_[23]} |\n- -- -- -- -- -- -\n|  {self.dict_[31]}  |  {self.dict_[32]}  |  {self.dict_[33]} |\n- -- -- -- -- -- -""")
    
    
    def design(self): 
        print(f"""- -- -- -- -- -- -\n|  {self.dict_[11]}  |  {self.dict_[12]}  |  {self.dict_[13]} |\n- -- -- -- -- -- -\n|  {self.dict_[21]}  |  {self.dict_[22]}  |  {self.dict_[23]} |\n- -- -- -- -- -- -\n|  {self.dict_[31]}  |  {self.dict_[32]}  |  {self.dict_[33]} |\n- -- -- -- -- -- -""")
        
    
    def check(self):
        self.k += 1
        
        for i in range(1,4):

            row = int(str(i)+str(1))
            coloumn = int(str(1)+str(i))

            row_count = 0
            coloumn_count = 0

            for j in range(2,4):

                row_ = int(str(i)+str(j))
                if  self.dict1_[row] == self.dict1_[row_]:
                    row_count += 1
                    if row_count == 2:
                        Tic_Tac_Toe.value_ = False
                        return f"game over row"

                coloumn_ = int(str(j)+str(i))
                if self.dict1_[coloumn] == self.dict1_[coloumn_]:
                    coloumn_count += 1
                    if coloumn_count == 2:
                        Tic_Tac_Toe.value_ = False
                        return "game over coloumn"
        
        if (self.dict1_[11] == self.dict1_[22] and self.dict1_[11] == self.dict1_[33]) or (self.dict1_[13] == self.dict1_[22] and self.dict1_[13] == self.dict1_[31]):
            Tic_Tac_Toe.value_ = False
            return "game over diagonal"
        
        else:
            if self.k == 9:
                return "draw"
            return "continue"




    def start(self):
        for i in range(9):
            if i%2 == 0:
                k = input("player 1:")
                j = int(k)
                self.dict_[j] = 'X'
                self.dict1_[j] = 'X'
                # print(self.dict_)
                self.design()
                print(self.check())
                if Tic_Tac_Toe.value_ == False:
                    print("player '1' wins")
                    break
                
                
            else:
                p = input("player 2:")
                j_ = int(p)
                self.dict_[j_] = 'O'
                self.dict1_[j_] = 'O'
                self.design()
                print(self.check())
                if Tic_Tac_Toe.value_ == False:
                    print("player 2 wins")
                    break
            


    

tic_tac_toe = Tic_Tac_Toe()
tic_tac_toe.start()

