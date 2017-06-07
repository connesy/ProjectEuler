#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int numberOfDigits = 3;

int main (int argc, char* argv[]) {

	int prod;	 // Product to check
	string s;	 // string version of product
	string s_r;  // reversed string of product
	int maxProd; // max palindromic product found so far
	// 3 digit factors, so i,j<1000
	for (int i=pow(10, numberOfDigits-1); i<pow(10, numberOfDigits); i++)
	{
		for (int j=i; j<pow(10, numberOfDigits); j++)
		{
			prod = i*j;
			if (prod > maxProd)
			{
				s = to_string(prod);
				s_r = s;
				reverse(s_r.begin(), s_r.end());
				
				// Returns 0 if strings are equal
				if (s.compare(s_r) == 0)
				{
					maxProd = prod;
				}
			}
		}
	}
	
	cout << maxProd << "\n";

	return 0;
}
