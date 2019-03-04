#include <iostream>
#include <vector>

using namespace std;

int main (int argc, char* argv[]) {

	int number = 21;
	vector<int> divisors;
	for (int i=20; i>10; i--)
	{
		divisors.push_back(i);
	}
	
	int factors;
	bool found = false;
	while (found == false)
	{
		factors = 0;
		for (int i=0; i<divisors.size(); i++)
		{
			if ((number % divisors[i] == 0) && (factors < divisors.size()-1))
			{
				factors++;
			}
			else if ((number % divisors[i] == 0) && (factors == divisors.size()-1))
			{
				found = true;
			}
		}
		if (found == true)
		{
			break;
		}
		else if (found == false)
		{
			number++;
		}
	}
	
	cout << number << "\n";

	return 0;
}
