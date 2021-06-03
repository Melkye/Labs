#include "StringContainer.h"
string StringContainer::classLine = "kukosiki";

StringContainer::StringContainer(string line)
{
	instanceLine = line;
}

int StringContainer::StaticCharCount(char searchChar)
{
    int count = 0;
    for (int i = 0; i < classLine.length(); i++ )
    {
        if (classLine[i] == searchChar)
            count++;
    }
    return count;
}

int StringContainer::InstanceCharCount(char searchChar)
{
    int count = 0;
    for (int i = 0; i < instanceLine.length(); i++)
    {
        if (instanceLine[i] == searchChar)
            count++;
    }
    return count;
}