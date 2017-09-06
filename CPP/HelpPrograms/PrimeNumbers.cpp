#include <iostream>
#include <fstream>
#include <cmath>
#include <armadillo>

/* This program produces an output file 'PrimeNumbers.dat' with all prime numbers from 2 up to and including (if prime) the number 'maxNumber' */

using namespace std;
using namespace arma;

void printVector(ivec V);
int maxNumber = 1e7;	// >= 2

int main(int argc, char const* argv[]) {
	
	// Keeps count of the number of primes
	int nPrimes = 0;
	ivec PrimeNumbers;
	// Loop runs code two times: first to calculate number of primes to 
	// correctly allocate vector size, second to fill vector with primes
	for (int iteration=0; iteration<2; iteration++)
	{
		// Only initialize vector on second run
		if (iteration == 1)
		{
			PrimeNumbers.set_size(nPrimes+1);
			PrimeNumbers(0) = 2; // First prime is 2
		}
		int index = 1;
		bool isPrime;
		// Only loop over odd numbers
		for (int i=3; i<maxNumber; i+=2)
		{
			isPrime = true;
			// No need to go higher 
			for (int j=3; j<=ceil(sqrt(i)); j+=2)
			{
				if (i%j == 0)
				{
					isPrime = false;
					break;
				}
			}
			if (isPrime == true)
			{
				if (iteration == 0)
				{
					nPrimes++;
				}
				else
				{
					PrimeNumbers(index) = i;
					index++;
				}
			}
		}
	}
	
	PrimeNumbers.save("PrimeNumbers.dat", arma_ascii);

	return 0;
}
