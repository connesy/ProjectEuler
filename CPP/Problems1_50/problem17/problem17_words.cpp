#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main(int argc, char const* argv[]) {

	string onesArray[10] = {"", "one", "two", "three", "four", 
							"five", "six", "seven", "eight", "nine"};
	string teensArray[10] = {"ten", "eleven", "twelve", "thirteen", "fourteen", 
								"fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
	string tensArray[10] = {"", "", "twenty", "thirty", "forty", 
							"fifty", "sixty", "seventy", "eighty", "ninety"};
	string hundredsArray[10] = {"", "one hundred", "two hundred", "three hundred", 
								"four hundred", "five hundred", "six hundred",
								"seven hundred", "eight hundred", "nine hundred"};
	
	int number;
	string And;
	string hundredsString;
	int hundreds;
	string tensString;
	int tens;
	string teensString;
	int teens;
	string onesString;
	int ones;
	
	for (int i=1; i<1000; i++)
	{
		number = i;
		// Hundreds
		hundreds = floor(number/100.0);
		hundredsString = hundredsArray[hundreds];

		number -= hundreds*100;
		// And
		if ((hundreds != 0) and (number != 0)) { And = " and "; }
		 else { And = ""; }
		// Tens
		tens = floor(number/10.0);
		tensString = tensArray[tens];
		
		// Teens
		if ((number >= 10) && (number < 20))
		{
			teens = number - 10;
			teensString = teensArray[teens];
		}
		 else{ teensString = ""; }
		
		number -= tens*10;
		// Ones
		if (teensString != "") { onesString = ""; }
		 else { onesString = onesArray[number]; }
		
		
		cout << i << ": " << hundredsString << And << tensString << teensString 
				<< " " << onesString << "\n";
			
	}

	cout << "1000: one thousand" << "\n";
	
	return 0;
}
