#include <iostream>
#include "../../HelpPrograms/Memoization.hpp"

using namespace std;

long Granny(int a, int b);

int main (int argc, char* argv[]) {

	mem<long, Granny> mem_Granny;
	long N = mem_Granny(20,20);
	//long N = Granny(20,20);
	
	cout << N << "\n";
	
	return 0;
}

long Granny(int a, int b)
{
	long val;
	if ((a == 1) || (b == 1)) 
		{val = a+b;}
	else if (a == b)
		{val = 2*Granny(a, b-1);}
	else
		{val = Granny(a-1, b) + Granny(a, b-1);}
	return val;
}
