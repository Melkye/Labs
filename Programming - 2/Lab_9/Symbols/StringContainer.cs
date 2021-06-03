using System;

namespace Symbols
{
    public delegate int SomeDelegate(char c);
    public class StringContainer
    {
        private static string classLine = "kukosiki";
        private string instanceLine;
        public StringContainer(string line)
        {
            instanceLine = line;
        }
        public static int StaticCharCount(char searchChar)
        {
            int count = 0;
            foreach(char c in classLine)
            {
                if (c == searchChar)
                    count++;
            }
            return count;
        }
        public int InstanceCharCount(char searchChar)
        {
            int count = 0;
            foreach (char c in instanceLine)
            {
                if (c == searchChar)
                    count++;
            }
            return count;
        }
    }
}
