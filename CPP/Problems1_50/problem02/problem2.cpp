#include <iostream>
#include <cmath>

int main(int argc, char const* argv[]) {

	int Old=1;
	int New=2;
	int temp;
	int sum = 0;
	
	
	while (New < 4*pow(10,6))
	{
		if (New%2 == 0)
		{
			sum += New;
		}
		temp = New;
		New += Old;
		Old = temp;
	}
	
	std::cout << "Sum: " << sum << "\n";	
	
	return 0;
}

