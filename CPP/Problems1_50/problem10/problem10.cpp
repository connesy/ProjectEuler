#include <iostream>
#include <cmath>
#include <armadillo>

using namespace std;
using namespace arma;

int main (int argc, char* argv[]) {

	ivec Primes;
	Primes.load("../../HelpPrograms/PrimeNumbers.dat");
	
	int limit = 2*1e6;
	int i=0;
	long sum = 0;
	while (Primes[i] < limit)
	{
		sum += Primes[i];
		i++;
	}
	
	cout << sum << "\n";

	return 0;
}
