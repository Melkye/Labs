#pragma once
#include "LinkedListNode.h"

class LinkedList
{
public:
	LinkedList();
	LinkedList(float headValue);
	
	void Add(float addValue);//destructor?
	void Remove(float removeValue);
	void RemoveAllLesser(float targetValue);
	int GetLargerCount(float targetNumber);

private:
	LinkedListNode* _head;
};

