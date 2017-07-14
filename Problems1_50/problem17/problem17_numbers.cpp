#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main(int argc, char const* argv[]) {

	int onesArray[10] = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4};
	int teensArray[10] = {3, 6, 6, 8, 8, 7, 7, 9, 8, 8};
	int tensArray[10] = {0, 0, 6, 6, 5, 5, 5, 7, 6, 6};
	int hundredsArray[10] = {0, 10, 10, 12, 11, 11, 10, 12, 12, 11};
	
	int number;
	int And;
	int hundredsString;
	int hundreds;
	int tensString;
	int tens;
	int teensString;
	int teens;
	int onesString;
	int ones;
	
	int Sum = 0;
	
	for (int i=1; i<1000; i++)
	{
		number = i;
		// Hundreds
		hundreds = floor(number/100.0);
		hundredsString = hundredsArray[hundreds];

		number -= hundreds*100;
		// And
		if ((hundreds != 0) and (number != 0)) { And = 3; }
		 else { And = 0; }
		// Tens
		tens = floor(number/10.0);
		tensString = tensArray[tens];
		
		// Teens
		if ((number >= 10) && (number < 20))
		{
			teens = number - 10;
			teensString = teensArray[teens];
		}
		 else{ teensString = 0; }
		
		number -= tens*10;
		// Ones
		if (teensString != 0) { onesString = 0; }
		 else { onesString = onesArray[number]; }
		
		Sum += hundredsString + And + tensString + teensString + onesString;
			
	}

	Sum += 11;
	
	cout << "Sum = " << Sum << "\n";
	
	return 0;
}
