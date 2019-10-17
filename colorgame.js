var numsquare=6;
var squares=document.querySelectorAll(".square"); 
var statuss=document.querySelector("#status");
var plays=document.querySelector("#play");
var guesses=document.querySelector("#guess");
var hh=document.querySelector("h1");
var btn=document.querySelector("button");
var btneasy=document.querySelector("#easy");
var btnhard=document.querySelector("#hard");
var colors=generate(numsquare);
var pickedcolor=pickcolor();


guesses.textContent=pickedcolor;

btneasy.addEventListener("click",function()
	{
		btneasy.classList.add("selected");
		btnhard.classList.remove("selected");
		numsquare=3;
		colors=generate(numsquare);
		pickedcolor=pickcolor();
		guesses.textContent=pickedcolor;
		for(var i=0;i<squares.length;i++)
		{	
			if(i<3)
				squares[i].style.background=colors[i];
			else 
				squares[i].style.display="none";
		}
		statuss.textContent="";
		hh.style.background="steelblue";
		plays.style.color="steelblue";
		btnhard.style.color="steelblue";
		btneasy.style.color="steelblue";
	}
);

btnhard.addEventListener("click",function()
	{
		btnhard.classList.add("selected");
		btneasy.classList.remove("selected");
		numsquare=6;
		colors=generate(numsquare);
		pickedcolor=pickcolor();
		guesses.textContent=pickedcolor;
		for(var i=0;i<squares.length;i++)
		{
			squares[i].style.background=colors[i];
			squares[i].style.display="block";
		}
		statuss.textContent="";
		hh.style.background="steelblue";
		plays.style.color="steelblue";
		btnhard.style.color="steelblue";
		btneasy.style.color="steelblue";
	}
);



btn.addEventListener("click",function()
	{
		colors=generate(numsquare);
		pickedcolor=pickcolor();
		guesses.textContent=pickedcolor;
		for(var i=0;i<squares.length;i++)
			squares[i].style.background=colors[i];
		statuss.textContent="";
		hh.style.background="steelblue";
		plays.style.color="steelblue";
		btnhard.style.color="steelblue";
		btneasy.style.color="steelblue";
	}
);



for(var i=0;i<squares.length;i++)
{
	squares[i].style.background=colors[i];
	squares[i].addEventListener("click",function()
	{
		if(this.style.background===pickedcolor)
			{			
				statuss.textContent="Correct";
				statuss.style.color=pickedcolor;
				plays.style.color=pickedcolor;
				btnhard.style.color=pickedcolor;
				btneasy.style.color=pickedcolor;
				hh.style.background=pickedcolor;
				btn.textContent="Play Again?"
				color();


			}	
		else
			{
				this.style.background="#232323";
				statuss.textContent="Try Again";
			}

	} 
	);

}


function color()
{
	for(var j=0;j<squares.length;j++)
		squares[j].style.background=pickedcolor;
}

function pickcolor()
{
	var col=Math.floor(Math.random() * colors.length);
	return colors[col];
}

function generate(num)
{
	var arr = [];
	for(var i=0;i<num;i++)
		arr.push(random());
	return arr;
}

function random()
{
	var red =Math.floor(Math.random() * 255);
	var green =Math.floor(Math.random() * 255);
	var blue =Math.floor(Math.random() * 255);

	return "rgb(" + red +", " + green + ", " + blue + ")";
}