#include <iostream>

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

	return 0;
}
