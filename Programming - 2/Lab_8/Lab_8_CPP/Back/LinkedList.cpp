#include "LinkedList.h"

LinkedList::LinkedList(float headValue)
{
	_head = new LinkedListNode(headValue);
}

void LinkedList::Add(float addValue)
{
    if (_head == nullptr)
    {
        _head = new LinkedListNode(addValue);
    }
    else
    {
        LinkedListNode* currentNode = _head;
        while (currentNode->next != nullptr)
        {
            currentNode = currentNode->next;
        }
        currentNode->next = new LinkedListNode(addValue);
    }
}

void LinkedList::Remove(float removeValue)
{
    if (_head != nullptr)
    {
        if (_head->value == removeValue)
        {
            LinkedListNode* currentNode = _head;
            _head = _head->next;
            delete currentNode;
        }
        else
        {
            LinkedListNode* currentNode = _head->next;
            LinkedListNode* prevNode = _head;
            while (currentNode != nullptr)
            {
                if (currentNode->value == removeValue)
                {
                    prevNode->next = currentNode->next;
                    delete currentNode;
                    break;
                }
                prevNode = currentNode;
                currentNode = currentNode->next;
            }
        }
    }
}
void LinkedList::RemoveAllLesser(float targetValue)
{
    LinkedListNode* currentNode = _head;
    bool isHead = true;
    LinkedListNode* prevNode = nullptr;
    while (currentNode != nullptr)
    {
        if (isHead)
        {
            if (currentNode->value < targetValue)
            {
                currentNode = _head;
                _head = _head->next;
                delete currentNode;
                currentNode = _head;
            }
            else
            {
                isHead = false;
                prevNode = _head;
                currentNode = _head->next;
            }
        }
        else
        {
            if (currentNode->value < targetValue)
            {
                delete currentNode;
                currentNode = currentNode->next;
                prevNode->next = currentNode;
            }
            else
            {
                prevNode = currentNode;
                currentNode = currentNode->next;
            }
        }
    }
}
int LinkedList::GetLargerCount(float targetValue)
{
    int count = 0;
    LinkedListNode* currentNode = _head;
    while (currentNode != nullptr)
    {
        if (currentNode->value > targetValue)
            count++;
        currentNode = currentNode->next;
    }
	return count;
}