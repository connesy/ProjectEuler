#include <cmath>
#include <iostream>

using namespace std;

int maxVal = 1000;

int main(int argc, char const* argv[]) {

	int sum = 0;
	for (int i=0; i<maxVal; i++)
	{
		if ((i%3 == 0) || (i%5 == 0))
		{
			sum += i;
		}
	}
	
	cout << "Sum: " << sum << "\n";
	
	return 0;
}
