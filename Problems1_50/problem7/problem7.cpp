#include <iostream>
#include <armadillo>

using namespace std;
using namespace arma;

int main (int argc, char* argv[]) {

	ivec Primes;
	Primes.load("../../HelpPrograms/PrimeNumbers.dat");
	
	cout << Primes[10000] << "\n";

	return 0;
}
