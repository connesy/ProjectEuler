#include <iostream>
#include <cmath>

using namespace std;

int main (int argc, char* argv[]) {

	int number = 100;
	int sum = 0;
	// Clever summation
	for (int i=1; i<=number; i++)
	{
		for(int j=i; j<=number; j++)
		{
			if (i != j)
			{
				sum += i*j;
			}
		}
	}
	
	sum *= 2;
	cout << sum << "\n";
	
	// --------------------
	// Mathsy way of doing it:
	// Sum of first n numbers: n(n+1)/2
	// Sum of squares of first n numbers: n(n+1)(2n+1)/6
	
	int n = number;
	int sum_n = pow(n,2)*pow((number+1),2) / 4;
	int sum_sq_n = n*(n+1)*(2*n+1) / 6;
	int diff = sum_n - sum_sq_n;
	
	cout << diff << "\n";

	return 0;
}
