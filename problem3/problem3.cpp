#include <iostream>
#include <cmath>
#include <armadillo>

using namespace std;
using namespace arma;

void printVector(ivec V);
int Number = 100;

int main(int argc, char const* argv[]) {

	ivec PrimeNumbers;
	PrimeNumbers(0) = 2;
	int index = 1;
	bool isPrime;
	for (int i=3; i<Number; i+=2)
	{
		isPrime = true;
		for (int j=3; j<=ceil(sqrt(i)); j+=2)
		{
			if (i%j == 0)
			{
				isPrime = false;
			}
		}
		if (isPrime == true)
		{
			PrimeNumbers(index) = i;
			index++;
		}
	}
	
	//printVector(PrimeNumbers);
	//PrimeNumbers.print();
	cout << PrimeNumbers.n_elem << "\n";
	cout << PrimeNumbers.size() << "\n";
	//cout << PrimeNumbers[0] << " " << PrimeNumbers[1] << " " << PrimeNumbers[2] << "\n";
	
	
	return 0;
}

void printVector(ivec V)
{
	for (int i=0; i<V.n_elem; i++)
	{
		cout << V[i] << "\n";
	}
}
