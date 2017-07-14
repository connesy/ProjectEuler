#include <iostream>
#include <fstream>
#include <armadillo>

using namespace std;
using namespace arma;

int main (int argc, char* argv[]) {

	int N = 65*1e3;
	ivec TNumbers(N);
	long sum = 0;
	
	for (int i=0; i<N; i++)
	{
		sum += (i+1);
		TNumbers[i] = sum;
	}
	
	TNumbers.save("TriangleNumbers.dat", arma_ascii);

	return 0;
}
