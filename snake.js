let gameBoard = document.querySelector(".gameBoard");
let scoredisplay = document.querySelector(".scores");
let snakeDirection = {x:0 , y:0};
let lastPaintTime = 0;
let speed = 4;
let score = 0;
let snake = [
    {x:9, y:9}, 
    { x: 2, y: 16 },
];

food = {x:5,y:10};

// FUNCTION TO CREATE SNAKE
function displaySnake(){
    gameBoard.innerHTML = "";
    snake.forEach((e,index)=> {
        snakeElement = document.createElement("div");
        snakeElement.style.gridRowStart = e.x;
        snakeElement.style.gridColumnStart = e.y;
        if(index === 0){
            snakeElement.classList.add('head')
        }
        else{
            snakeElement.classList.add('snake')
        }
        gameBoard.appendChild(snakeElement);
    });
}
// FUNCTION TO CREATE FOOD
function displayFood(){
    foodElement = document.createElement("div");
    foodElement.style.gridRowStart = food.x;
    foodElement.style.gridColumnStart = food.y;
    console.log("food = ",food.x,food.y)
    foodElement.classList.add('food');
    gameBoard.appendChild(foodElement);

}
displayFood();

// FUNCTION TO MOVE SNAKE 
function moveSnake(){
    
    for(let i = (snake.length-2);i>=0;i--){
        snake[i+1]= {...snake[i]}
    }
    snake[0].x += snakeDirection.x;
    snake[0].y += snakeDirection.y;
    console.log("Snake coordinates",snake[0].x,snake[0].y);    
}

// FUNCTION TO CHECK IF THE COLLISION HAPPENS
function iscollision(snake){
    for(i=2 ;i<snake.length;i++){
        if(snake[i].x === snake[0].x && snake[i].y === snake[0].y){
            return true;
        }
    }
    if(snake[0].x >= 18 || snake[0].x <=0 || snake[0].y >= 18 || snake[0].y <=0){
        return true;
    }
    return false;
}

// MAIN GAME SEQUENCE 
function gameLogic(){
    
    if(iscollision(snake)){
        snakeDirection = {x: 0,y:0};
        alert("Game over");
        snake = [{x: 13, y: 15}];
        score = 0;
        speed = 4;
        scoredisplay.innerHTML = "Score"+score;
    }
    if(food.x === snake[0].x  && food.y ===snake[0].y){
        score =score+10;
        scoredisplay.innerHTML = "Score"+score;
        snake.unshift({x: snake[0].x + snakeDirection.x, y: snake[0].y + snakeDirection.y});
        let a=2;
        let b=16;
        foodElement = document.createElement("div");
        food = {x: Math.round(a+(b-a)*Math.random()) , y : Math.round(a+(b-a)*Math.random())}
    }
    moveSnake();   
    displaySnake();
    displayFood();
}

//This creates the game loop
function main(ctime){
    if(score > 30 && speed < 60){
        speed = speed + 1;
    
    }
    else if(speed >= 60){
        speed = speed + 2;
    }
    window.requestAnimationFrame(main);
    if((ctime-lastPaintTime)/1000 < 1/speed){
        return;
    }
    lastPaintTime = ctime;
    gameLogic();
}
window.requestAnimationFrame(main)

window.addEventListener('keydown',e =>{
    // Here if the key is press then only game will start
    snakeDirection ={x:0,y:0};
    switch(e.key){
        case 'ArrowDown':snakeDirection.x = 1 ;snakeDirection.y = 0;
            break;
        case 'ArrowUp':snakeDirection.x = -1 ;snakeDirection.y = 0;
            break;
        case 'ArrowLeft':snakeDirection.x = 0 ;snakeDirection.y = -1;
            break;
        case 'ArrowRight':snakeDirection.x = 0;snakeDirection.y = 1;
            break;
        default:
            break;
        
    }
});