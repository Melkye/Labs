using System;
using System.Text;

namespace Application
{
    class Program
    {
        static void Main()
        {
            Console.OutputEncoding = Encoding.UTF8;
            LibraryFront.CreateLibrary("Remote Library 451°");
            LibraryFront.StartMenu();
        }
    }
    
}
