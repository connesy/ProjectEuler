#include <iostream>
#include <cmath>
#include <vector>
#include <armadillo>

using namespace std;
using namespace arma;

long Number = 600851475143;

int main(int argc, char const* argv[]) {
	
	ivec Primes;
	Primes.load("../HelpPrograms/PrimeNumbers.dat");
	
	vector<int> Factors;
	long tempNumber = Number;
	int i;
	bool foundFactor;
	
	// Keep running track of Number, divided by already found prime factors, 
	// until all factors are found (so tempNumber == 1)
	while (tempNumber > 1)
	{
		i = 0;
		foundFactor = false;
		while (foundFactor == false)
		{
			if (tempNumber % Primes(i) == 0)
			{
				// Add new factor to Factor
				Factors.push_back(Primes(i));
				foundFactor = true;
				// Divide tempNumber by newly found factor
				tempNumber /= Primes(i);
				break;
			}
			i++;
		}
	}
	
	ivec armaFactors(Factors);
	armaFactors = sort(armaFactors);
	
	cout << armaFactors << "\n";
	double maxFactor = max(armaFactors);
	
	cout << maxFactor << "\n";
	
	
	return 0;
}


