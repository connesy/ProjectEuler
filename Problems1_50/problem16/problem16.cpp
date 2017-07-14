#include <iostream>
#include <cmath>
#include <cassert>
#include <armadillo>

using namespace std;
using namespace arma;

//vec vec::operator*(double x) const;

int main (int argc, char* argv[]) {

	ivec NumberOld = zeros<ivec>(310);
	ivec NumberNew = zeros<ivec>(310);
	//NumberOld.zeros();
	//NumberNew.zeros();
	NumberOld(0) = 1;
	NumberNew(0) = 1;
	
	int tempProd;
	int tempRest;
	
	for (int i=1; i<=1000; i++)
	{
		tempRest = 0;
		for (int j=0; j<NumberOld.size(); j++)
		{
			tempProd = NumberOld(j) * 2 + tempRest;
			if (tempProd >= 10)
			{
				tempRest = 1;
				NumberNew(j) = tempProd - 10;
			} 
			 else
			{
				tempRest = 0;
				NumberNew(j) = tempProd;
			}
			NumberOld(j) = NumberNew(j);
		}
		assert(NumberNew(309) == 0);
	}
	
	long Sum = 0;
	for (int i=0; i<NumberNew.size(); i++)
	{
		Sum += NumberNew(i);
	}
	
	cout << "Sum = " << Sum << "\n";


	return 0;
}

/*
vec vec::operator*(double x) const
{
	double temp;
	vec V(this->size());
	
	for (int i=0; i<V.size(); i++)
	{
		temp = V(i)*x;
		if (x > 10)
		{
			V(i) = 
*/
