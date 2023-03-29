let count_ = 0;
let array_ = ['1','2','3','4','5','6','7','8','9','10'];
let win = false;
var coin = "X";
function hi(id){
    if(win == false){


    if (count_% 2 == 0){
        document.getElementById("player").innerHTML = "Player-2 : O";
        var coin = "X";
    }
    else{
        document.getElementById("player").innerHTML = "Player-1 : X";
        var coin = "O";
    }
    let x = document.getElementById(id);
    x.innerHTML = coin;
    array_[id] = coin;
    console.log(array_);
    validation(array_);
    count_ += 1;}
    else{
       document.getElementById("win").innerHTML = "better Luck nxt time";
    }
}






function validation(array_){
    for(i=0;i<3;i++){
        // row check
        if (array_[1+i] == array_[2+i] && array_[1+i] == array_[3+i]){
            document.getElementById("player").style.display = "none";
            document.getElementById("win").innerHTML = "player win row";
            console.log("Game Over row");
            win = true;
            // return True
        }
        // coloumn check
        else if (array_[1+i] == array_[4+i] && array_[1+i] == array_[7+i]){
            document.getElementById("player").style.display = "none";
            document.getElementById("win").innerHTML = "player win coloumn";
            
            console.log("Game Over coloumn");
            win = true;
            // return True

        }
        // diagonal check
        else if((array_[1] == array_[5] && array_[1] == array_[9]) || (array_[3] == array_[5] & array_[1] == array_[7])){
            document.getElementById("player").style.display = "none";
            document.getElementById("win").innerHTML = "player win diagonal";
            console.log("Game Over cross");
            win = true;
            // return True

        }
        else{

            if(count_ == 8){
                document.getElementById("win").innerHTML = "Draw-Match";
            console.log("Draw Match Play Again");}
        }
    }
}