#pragma once
#include "CustomString.h"
class CustomDigitString : public CustomString
{
public:
    CustomDigitString();
    CustomDigitString(char* line);

    void SetLine(char* line); //overrides base class method?
    void Flip();
};

