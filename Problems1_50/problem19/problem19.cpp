#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main(int argc, char const* argv[]) {

	bool done = false;
	int day = 2;
	int Date[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	int DateLimit;
	int sundays = 0;
	
	for (int year=1901; year<=2000; year++)
	{
		for (int month=1; month<=12; month++)
		{
			if (year%4 == 0){ DateLimit = 29; }
			 else { DateLimit = Date[month]; }
			 
			for (int date=1; date<=DateLimit; date++)
			{
				
				
	
	
	
	
	return 0;
}
