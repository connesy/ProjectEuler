#include <iostream>
#include <cmath>
#include <armadillo>

using namespace std;
using namespace arma;

int main (int argc, char* argv[]) {

	ivec TNumbers;
	TNumbers.load("../../HelpPrograms/TriangleNumbers.dat");
	
	int firstNumber = 0;
	int nFactors;
	
	for (int i=0; i<TNumbers.n_elem; i++)
	{
		nFactors = 0;
		
		for (int factor=1; factor<=ceil(sqrt(TNumbers[i])); factor++)
		{
			if (TNumbers[i] % factor == 0)
			{
				if (factor != sqrt(TNumbers[i]))
				{
					nFactors += 2;
				}
				else
				{
					nFactors++;
				}
			}
		}
		if (nFactors > 500)
		{
			//cout << "Factors: " << nFactors;
			firstNumber = TNumbers[i];
			break;
		}
	}
	
	cout << firstNumber << "\n";
	
	return 0;
}
