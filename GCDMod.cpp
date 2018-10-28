#include <iostream>

using namespace std;

unsigned long long int calcGCD(unsigned long long int a, unsigned long long int b) {

	if(b == 0) {
		return a;
	}

	return calcGCD(b, a%b);	
}

unsigned long long int modExp(unsigned long long int a, unsigned long long int n, unsigned int M) {
	if( n == 0 ) {
		return 1;
	} else if(n % 2 == 0) {
		return modExp( (a*a) % M, n/2, M);
	} else {
		return ( a * modExp( (a*a) % M, (n-1)/2, M) ) % M;
	}
}

int main() {
	
	int t;
	cin >> t;

	unsigned long long int a, b, n, diff;

	unsigned int M = 1000000007;
	
	for(int i = 0; i < t; i++) {
	
		cin >> a >> b >> n;

		if(a > b){
			diff = a - b;
		} else {
			diff = b - a;
		}
		cout << calcGCD( modExp(a, n, M) + modExp(b, n, M) , diff ) << endl ; 
	}
}
