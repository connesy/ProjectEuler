#include <iostream>
#include <fstream>
#include <armadillo>

using namespace std;
using namespace arma;

int main (int argc, char* argv[]) {

	ivec FibNumbers;
	int N = 1;
	
	for (int iteration=0; iteration<2; iteration++)
	{
		int Old = 1;
		int New = 1;
		int temp;
		int i=0;
		if (iteration==1)
		{
			FibNumbers.resize(N);
			FibNumbers(0) = 1;
		}
		
		while (New < 1e7)
		{
			temp = Old;
			Old = New;
			New += temp;
			if (iteration == 0)
			{
				N++;
			}
			else if (iteration == 1)
			{
				FibNumbers[i+1] = Old;
				i++;
			}
		}
	}
	
	FibNumbers.save("FibonacciNumbers.dat", arma_ascii);

	return 0;
}
