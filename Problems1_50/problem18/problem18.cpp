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
	imat Triangle_Val = zeros<imat>(N,N);
	imat Triangle_Sum = zeros<imat>(N,N);
	ivec iQ = zeros<ivec>(int(N*(N+1)/2.0));
	ivec jQ = zeros<ivec>(int(N*(N+1)/2.0));
	
	ifstream read_file("TriangleNumbers.dat");
	
	int x;
	for (int i=0; i<N; i++)
	{
		for (int j=0; j<=i; j++)
		{
			if (!read_file.eof())
			{
				read_file >> Triangle_Val(i,j);
			}
		}
	}
	read_file.close();
			
	// -------------------------------------------------
	// 
	// -------------------------------------------------
	
	bool done = false;
	while (done != true)
	{
		
	
	
	
	
	return 0;
}
