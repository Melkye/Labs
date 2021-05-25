using System;
using System.Collections.Generic;

using LibraryBack.Library;
using LibraryBack.Library.Accounts;
using LibraryBack.Library.Exceptions;
using LibraryBack.Publications;

namespace Application
{
    /// <summary>
    /// contains Library class and methods to operate it in console
    /// </summary>
    public static partial class LibraryFront 
    {
        private static Library _lib;
        public static string LibraryName => _lib.Name;

        public static void CreateLibrary(string name)
        {
            _lib = new Library(name);
        }
        public static void ListAllBooks()
        {
            Console.WriteLine("\n" + "\t" + "All available books:");
            List < Book > bookList = _lib.BookList;
            Console.WriteLine($"{"ID", 3} {"Title", -25} {"Author", -31} {"Genre", -15}");
            foreach (Book book in bookList)
            {
                Console.WriteLine(book.ToString());
            }
        }
        public static void ListAllSPs()
        {
            Console.WriteLine("\n" + "\t" + "All available serial publications:");
            List<SerialPublication> spList = _lib.SerialPublicationList;
            Console.WriteLine($"{"ID", 3} {"Title", -25} {"Author", -31}");
            foreach (SerialPublication sp in spList)
            {
                Console.WriteLine(sp.ToString());
            }
        }
        public static void ListPublications(List<Publication> pubs)
        {
            Console.WriteLine($"{"ID",3} {"Title",-25} {"Author",-31} {"Genre (for books)",-15}");
            foreach (Publication pub in pubs)
            {
                Console.WriteLine(pub.ToString());
            }
        }

        public static void CreateUserAccount(string login)
        {
            _lib.CreateUserAccount(login);
        }
        public static void DeleteUserAccount(int userID)
        {
            _lib.DeleteUserAccount(userID);
        }
        public static void ListAllPubsTaken(int userID)
        {
            UserAccount user = _lib.FindUserAccount(userID);
            if (user != null)
            {
                if (user.PublicationsTaken.Count == 0)
                {
                    Console.WriteLine("No publications taken");
                }
                else
                {
                    Console.WriteLine($"{"ID",3} {"Title",-25} {"Author",-31} {"Genre (for books)",-15}");
                    foreach (Publication pub in user.PublicationsTaken)
                    {
                        if (pub is Book)
                        {
                            Console.WriteLine((pub as Book).ToString());
                        }
                        else
                        {
                            Console.WriteLine((pub as SerialPublication).ToString());
                        }
                    }
                }
            }
            else
            {
                Console.WriteLine("User not found"); // need this? (LogInMenu checks if user != null)
            }
        }
    }
}
