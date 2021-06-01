
namespace DataStructures
{
    public class LinkedList
    {
        private LinkedListNode _head;
        public LinkedList(params float[] values)
        {
            Add(values);
        }
        public int Count
        {
            get
            {
                int count = 0;
                LinkedListNode currentNode = _head;
                while (currentNode != null)
                {
                    count++;
                    currentNode = currentNode.next;
                }
                return count;
            }
        }
        public void Add(params float[] addValues)
        {
            if (addValues.Length > 0)
            {
                int indexShift = 0;
                if (_head == null)
                {
                    _head = new LinkedListNode(addValues[0]);
                    indexShift = 1;
                }
                LinkedListNode currentNode = _head;
                while (currentNode.next != null)
                {
                    currentNode = currentNode.next;
                }
                for (int i = 0; i < addValues.Length - indexShift; i++)
                {
                    currentNode.next = new LinkedListNode(addValues[i + indexShift]);
                    currentNode = currentNode.next;
                }
            }
        }
        public void Remove(float removeValue)
        {
            if (_head != null)
            {
                if (_head.value.Equals(removeValue))
                {
                    _head = _head.next;
                }
                else
                {
                    LinkedListNode currentNode = _head.next;
                    LinkedListNode prevNode = _head;
                    while (currentNode != null)
                    {
                        if (currentNode.value.Equals(removeValue))
                        {
                            prevNode.next = currentNode.next;
                            break;
                        }
                        prevNode = currentNode;
                        currentNode = currentNode.next;
                    }
                }
            }
        }
        public void RemoveAllLesser(float targetValue)
        {
            LinkedListNode currentNode = _head;
            bool isHead = true;
            LinkedListNode prevNode = null;
            while (currentNode != null)
            {
                if (isHead)
                {
                    if (currentNode.value < targetValue)
                    {
                        currentNode = currentNode.next;
                    }
                    else
                    {
                        isHead = false;
                        prevNode = _head;
                        currentNode = _head.next;
                    }
                }
                else
                {
                    if (currentNode.value < targetValue)
                    {
                        currentNode = currentNode.next;
                        prevNode.next = currentNode;
                    }
                    else
                    {
                        prevNode = currentNode;
                        currentNode = currentNode.next;
                    }
                }
            }
        }
        public int GetLargerCount(float targetValue)
        {
            int count = 0;
            LinkedListNode currentNode = _head;
            while (currentNode != null)
            {
                if (currentNode.value > targetValue)
                    count++;
                currentNode = currentNode.next;
            }
            return count;
        }

        private class LinkedListNode // store this in a separate file?
        {
            public float value;
            public LinkedListNode next;
            public LinkedListNode(float value)
            {
                this.value = value;
            }
        }
    }
}
