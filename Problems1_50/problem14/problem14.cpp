#include <iostream>

using namespace std;

long Collatz(long n);

int main (int argc, char* argv[]) {

	int longest = 0;
	long longestN;
	long n;
	int chain;
	
	for (int i=1; i<1e6; i++)
	{
		chain = 0;
		n = i;
		while (n != 1)
		{
			n = Collatz(n);
			chain++;
		}
		if (chain > longest)
		{
			longest = chain;
			longestN = i;
		}
	}
	
	cout << longestN << " " << longest << "\n";

	return 0;
}

long Collatz(long n)
{
	long new_n;
	if (n%2 == 0){new_n = n/2;}
	else {new_n = 3*n + 1;}
	return new_n;
}
