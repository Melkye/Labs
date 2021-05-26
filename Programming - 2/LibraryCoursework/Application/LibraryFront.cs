using System;
using System.Collections.Generic;

using LibraryBack.Library;
using LibraryBack.Library.Accounts;
using LibraryBack.Library.Exceptions;
using LibraryBack.Publications;

namespace Application
{
    /// <summary>
    /// Contains Library class and methods to operate it in console
    /// </summary>
    public static partial class LibraryFront 
    {
        private static Library _lib;
        public static string LibraryName => _lib.Name;

        public static void CreateLibrary(string name)
        {
            _lib = new Library(name);
        }
        private static void ListAllBooks()
        {
            List<Book> bookList = _lib.BookList;
            if (bookList.Count == 0)
            {
                Console.WriteLine("\n" + "\t" + "No book available");
            }
            else
            {
                Console.WriteLine("\n" + "\t" + "All available books:");
                Console.WriteLine($"{"ID",3} {"Title",-30} {"Author",-31} {"Genre",-15}");
                foreach (Book book in bookList)
                {
                    Console.WriteLine(book.ToString());
                }
            }
            Console.WriteLine();
        }
        private static void ListAllSPs()
        {
            List<SerialPublication> spList = _lib.SerialPublicationList;
            if (spList.Count == 0)
            {
                Console.WriteLine("\n" + "\t" + "No serial publications available");
            }
            else
            {
                Console.WriteLine("\n" + "\t" + "All available serial publications:");
                Console.WriteLine($"{"ID",3} {"Title",-30} {"Author",-31}");
                foreach (SerialPublication sp in spList)
                {
                    Console.WriteLine(sp.ToString());
                }
            }
            Console.WriteLine();
        }
        private static void ListPublications(List<Publication> pubs)
        {
            Console.WriteLine($"{"ID",3} {"Title",-30} {"Author",-31} {"Genre (for books)",-15}");
            foreach (Publication pub in pubs)
            {
                Console.WriteLine(pub.ToString());
            }
        }
        /// <summary>
        /// Creates a new account prompting library to do this
        /// </summary>
        /// <returns> true if creation successful, false otherwise</returns>
        private static bool CreateUserAccount(string login)
        {
            bool creationSuccessful = false;
            try
            {
               _lib.CreateUserAccount(login);
                creationSuccessful = true;
                Console.WriteLine("New account created");
            }
            catch (InvalidLoginException e)
            {
                PrintErrorMessage(e.Message);
            }
            catch (Exception e)
            {
                PrintErrorMessage("Error happened: " + e.Message);
            }
            return creationSuccessful;
        }
        private static void DeleteUserAccount(int userID)
        {
            try
            {
                _lib.DeleteUserAccount(userID);
                Console.WriteLine("Account deleted" + "\n");
            }
            catch (PublicationTakenException e)
            {
                PrintErrorMessage(e.Message);
            }
            catch (Exception e)
            {
                PrintErrorMessage("Error happened: " + e.Message);
            }
        }
        private static void TakePublication(int userID, PublicationType pubType, int pubID)
        {
            try
            {
                _lib.TakePublication(userID, pubType, pubID);
            }
            catch (PublicationNotFoundException e)
            {
                PrintErrorMessage(e.Message);
            }
            catch (PublicationTakenException e)
            {
                PrintErrorMessage(e.Message);
            }
            catch (InvalidIDException e)
            {
                PrintErrorMessage(e.Message);
            }
            catch (PublicationsLimitReachedException e)
            {
                PrintErrorMessage(e.Message);
            }
            catch (Exception e)
            {
                PrintErrorMessage("Error happened: " + e.Message);
            }
        }
        private static void ReturnPublication(int userID, PublicationType pubType, int pubID)
        {
            try
            {
                _lib.ReturnPublication(userID, pubType, pubID);
            }
            catch (InvalidIDException e)
            {
                PrintErrorMessage(e.Message);
            }
            catch (PublicationNotFoundException e)
            {
                PrintErrorMessage(e.Message);
            }
            catch (Exception e)
            {
                PrintErrorMessage("Error happened: " +  e.Message);
            }
        }
        private static void ListAllPubsTaken(int userID)
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
                    Console.WriteLine("\n" + "\t" + $"All publications taken by user {user.Login}:");
                    Console.WriteLine($"{"ID",3} {"Title",-30} {"Author",-31} {"Genre (for books)",-15}");
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
                    Console.WriteLine();
                }
            }
            else
            {
                PrintErrorMessage("User not found");
            }
        }
        private static void PrintErrorMessage(string message)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(message);
            Console.ForegroundColor = ConsoleColor.White;
        }
    }
}
