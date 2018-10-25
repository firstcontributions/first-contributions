# Hi!
*I am so glad to be one of the contributors of your repository.*   
*My name is yash and I have just started with git.*
## here are some empowering texts for you all...
> Well it's my belief that anyone who believes he can code, he surely can.  
> Infuse your life with action. Don't wait for it to happen. Make it happen. Make your own future. Make your own hope. Make your own love. And whatever your beliefs, honor your creator, not by passively waiting for grace to come down from upon high, but by doing what you can to make grace happen... yourself, right now, right down here on Earth. 
> Read more at. [Brainlyquote](https://www.brainyquote.com/quotes/bradley_whitford_410518).



* A translation in Swedish

# Hej!
*Jag är så glad att vara en av bidragsgivarna till ditt förråd.*
*Jag heter yash och jag har just börjat med git.*
## Här är några bemyndigande texter till er alla...
> Jo det är min tro att alla som tror att han kan koda, det kan han säkert.
> Tillfoga ditt liv med handling. Vänta inte på att det ska hända. Få det att hända. Gör din egen framtid. Gör ditt eget hopp. Gör din egen kärlek. Och oavsett din tro, hedra din skapare, inte genom att passivt vänta på nåd att komma ner från högt, men genom att göra vad du kan för att få nåd att hända ... själv, just nu, precis här nere på jorden.
> Läs mer på. [Brainlyquote](https://www.brainyquote.com/quotes/bradley_whitford_410518)

![Believe That](https://cdn.lifehack.org/wp-content/uploads/2016/12/15070638/17.jpg). 

# Let's code. 
```c++
#include <iostream>

unsigned int ackermann(unsigned int m, unsigned int n) {
	if (m == 0) {
		return n + 1;
	}
	if (n == 0) {
		return ackermann(m - 1, 1);
	}
	return ackermann(m - 1, ackermann(m, n - 1));
}

int main() {
	for (unsigned int m = 0; m < 4; ++m) {
		for (unsigned int n = 0; n < 10; ++n) {
			std::cout << "A(" << m << ", " << n << ") = " << ackermann(m, n) << "\n";
		}
	}
}
```
* just an example- Ackermann function
