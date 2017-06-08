#include <iostream>
#include <cmath>

using namespace std;

int main (int argc, char* argv[]) {

	int a;
	int b;
	int c;
	bool found;
	int prod;
	
	for (a=1; a<350; a++)
	{
		for (b=a+1; b<500; b++)
		{
			for (c=b+1; c<(1000-a-b+1); c++)
			{
				if ((pow(a,2) + pow(b,2) == pow(c,2)) && (a + b + c == 1000))
				{
					found = true;
					prod = a*b*c;
					break;
				}
			}
			if (found) {break;}
		}
		if (found) {break;}
	}
	
	cout << a << " " << b << " " << c << "\n";
	cout << prod << "\n";

	return 0;
}
