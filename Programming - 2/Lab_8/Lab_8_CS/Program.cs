using DataStructures;

namespace Lab_8_CS
{
    class Program
    {
        static void Main()
        {
            LinkedList list1 = new LinkedList(0.5f, 1, 1.5f);
            list1.Add(-5, 0.5f, 50, 100);
            list1.Remove(100);
            list1.RemoveAllLesser(2.6f);
            int n = list1.GetLargerCount(2);
        }
    }
}
