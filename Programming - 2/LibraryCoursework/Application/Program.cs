using System;
using Library;

namespace Application
{
    class Program
    {
        static void Main(string[] args)
        {
            Book book1 = new Book(1, "abuba", ("Me", "Myself"), Book.BookGenre.NonFiction);
            Console.WriteLine(book1.ToString());
            Console.ReadKey();
        }
    }
    // add method ListAllPubs here that gets (const?) list of pubs as input
}
