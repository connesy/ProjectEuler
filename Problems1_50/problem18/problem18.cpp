#include <iostream>
#include <fstream>
#include <cmath>
#include <armadillo>

using namespace std;
using namespace arma;

int main(int argc, char const* argv[]) {
	
	// -------------------------------------------------
	// Load triangle numbers into imat
	// -------------------------------------------------
	int N = 15;
	imat Triangle = zeros<imat>(N,N);
	ifstream read_file("TriangleNumbers.dat");
	
	int x;
	for (int i=0; i<N; i++)
	{
		for (int j=0; j<=i; j++)
		{
			if (!read_file.eof())
			{
				read_file >> Triangle(i,j);
			}
		}
	}
	read_file.close();
			
	// -------------------------------------------------
	// 
	// -------------------------------------------------
	
	
	
	
	return 0;
}
