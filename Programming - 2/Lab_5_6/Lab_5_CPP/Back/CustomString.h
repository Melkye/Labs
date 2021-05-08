#pragma once
class CustomString
{
public:
    CustomString();
    CustomString(char* line);
    ~CustomString();

    int GetLength();
    char* GetLine();
    void SetLine(char* line);
protected:
    char* Line;
    int Length;
};


