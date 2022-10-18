const playerChoice = document.getElementById("playerChoice");
const computerChoice= document.getElementById("computerChoice");
const result = document.getElementById("result");
const userChoice = document.querySelectorAll(".userChoice");
let player;
let computer;
let finalResult ;
userChoice.forEach(user => user.addEventListener("click",()=>{
                player = user.textContent;
                computerTurn();
                playerChoice.textContent = `Player  : ${player}`;
                computerChoice.textContent = `Computer  : ${computer}`;
                calculateResult();
                result.textContent = `Result : ${finalResult}`;

}));
function computerTurn(){
    
    const randomNumber = Math.floor(Math.random()*3) +1;

    switch (randomNumber) {
        case 1: computer = "Rock"
            
            break;
            case 2: computer = "Paper"
            
            break;
            case 3: computer = "Scissor"
            
            break;
    }

}

function calculateResult(){
    if (player == computer) {
        finalResult = "Draw";
    }
    else {
        if(player == "Rock"){
            if (computer =="Paper") {
                finalResult = "Computer won"
            } else {
                finalResult = "Player won"
            }
        }
        else if(player == "Paper"){
            if (computer =="Scissor") {
                finalResult = "Computer won"
            } else {
                finalResult = "Player won"
            }
        }

        else{
            if (computer =="Rock") {
                finalResult = "Computer won"
            } else {
                finalResult = "Player won"
            }
        }
    }
}
console.log("hi")