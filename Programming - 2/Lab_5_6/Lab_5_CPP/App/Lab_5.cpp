#include "Lab_5.h"


int main()
{
    char word[] = "questions?\0";
    CustomString S1 = CustomString(word);

    char nums[] = "123\0";
    CustomDigitString D1 = CustomDigitString(nums);

    CustomDigitString D2 = CustomDigitString();

    char mix[] =  "qu1e2s\0";
    D2.SetLine(mix);
    D2.Flip();

	return 0;
}