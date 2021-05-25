using System;
using System.Collections.Generic;

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

        public static void StartMenu()
        {
            bool startMenuWorking = true;
            while (startMenuWorking)
            {
                Console.ForegroundColor = ConsoleColor.Magenta;
                Console.Title = LibraryFront.LibraryName;
                Console.WriteLine("\n" + "\t" + LibraryFront.LibraryName + " welcomes you");

                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.WriteLine(
                    "\t" + "Select an option:" + "\n" +
                    "1. Log in"      + "\t\t" + "4. List all available books " + "\n" +
                    "2. Register"    + "\t\t" + "5. List all serial available publications" + "\n" +
                    "3. Search "     + "\t\t" + "6. Exit" + "\n");
                Console.ForegroundColor = ConsoleColor.White;
                Console.Write("Your choice: ");

                bool correctInput = int.TryParse(Console.ReadLine(), out int choice);
                while (correctInput == false)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Wrong choice input.  Should be integer 1 to 6");
                    Console.ForegroundColor = ConsoleColor.White;
                }

                switch (choice)
                {
                    case 1:
                        Console.Write("Enter account ID:");
                        correctInput = int.TryParse(Console.ReadLine(), out int userID);
                        if (correctInput)
                        {
                            UserMenu(userID);
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine("Wrong input of account ID");
                            Console.ForegroundColor = ConsoleColor.White;
                        }
                        break;
                    case 2:
                        Console.Write("Enter new login: ");
                        string login = Console.ReadLine();
                        
                        Console.WriteLine("New account created" + "\n");
                        _lib.CreateUserAccount(login);
                        UserMenu(_lib.FindUserAccount(login).ID);
                        break;
                    case 3:
                        SearchMenu();
                        break;
                    case 4:
                        ListAllBooks();
                        break;
                    case 5:
                        ListAllSPs();
                        break;
                    case 6:
                        startMenuWorking = false; ///?
                        break;
                    default:
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Wrong choice input. No such option number exists. Should be integer 1 to 6");
                        Console.ForegroundColor = ConsoleColor.White;
                        break;
                }
            }
        }
        public static void UserMenu(int userID)
        {
            UserAccount user = _lib.FindUserAccount(userID);
            if (user != null)
            {
                Console.WriteLine($"User: {user.Login} \t ID: {user.ID}");
                bool userMenuWorking = true;
                while (userMenuWorking)
                {
                    Console.ForegroundColor = ConsoleColor.Blue;
                    Console.WriteLine(
                        "\n" +
                        "Select an option:" + "\n" +
                        "1. Take a publication"      + "\t\t" + "5. List all taken publications" + "\n" +
                        "2. Return a publication"    + "\t\t" + "6. List all available books" + "\n" +
                        "3. Search " + "\t"          + "\t\t" + "7. List all available serial publications" + "\n" +
                        "4. Delete account"          + "\t\t" + "8. Exit" + "\n\n");
                    Console.ForegroundColor = ConsoleColor.White;
                    Console.Write("Your choice: ");
                    bool correctChoiceInput = int.TryParse(Console.ReadLine(), out int choice);
                    if (correctChoiceInput)
                    {
                        switch (choice)
                        {
                            case 1:
                                Console.WriteLine(
                                    "\n" +
                                    "\t" + "Select publication type:" + "\n" +
                                    "1. Book" + "\n" +
                                    "2. Serial publication" + "\n");
                                Console.Write("Your choice: ");
                                bool correctPubTypeInput = int.TryParse(Console.ReadLine(), out int choicePubType);
                                if (correctPubTypeInput)
                                {
                                    PublicationType pubType;
                                    if (choicePubType == 1)
                                    {
                                        pubType = PublicationType.Book;
                                    }
                                    else if (choicePubType == 2)
                                    {
                                        pubType = PublicationType.SerialPublication;
                                    }
                                    else
                                    {
                                        Console.ForegroundColor = ConsoleColor.Red;
                                        Console.WriteLine("Wrong input of publication type");
                                        Console.ForegroundColor = ConsoleColor.White;
                                        break;/////?? exit from switch block
                                    }
                                    Console.WriteLine($"Enter {pubType.GetType()} ID:"); ///
                                    bool correctIDInput = int.TryParse(Console.ReadLine(), out int pubID);
                                    if (correctIDInput)
                                    {
                                        _lib.TakePublication(userID, pubType, pubID);  // try/catch here
                                    }
                                    else
                                    {
                                        Console.ForegroundColor = ConsoleColor.Red;
                                        Console.WriteLine($"Wrong input of {pubType.GetType()} ID");
                                        Console.ForegroundColor = ConsoleColor.White;
                                    }
                                }
                                else
                                {
                                    Console.ForegroundColor = ConsoleColor.Red;
                                    Console.WriteLine($"Wrong input of publication type");
                                    Console.ForegroundColor = ConsoleColor.White;
                                }
                                break;
                            case 2:
                                Console.WriteLine(
                                    "\n" +
                                    "\t" + "Select publication type:" + "\n" +
                                    "1. Book" + "\n" +
                                    "2. Serial publication" + "\n");
                                Console.Write("Your choice: ");
                                correctPubTypeInput = int.TryParse(Console.ReadLine(), out choicePubType); // why vars are defined already?
                                if (correctPubTypeInput)
                                {
                                    PublicationType pubType;
                                    if (choicePubType == 1)
                                    {
                                        pubType = PublicationType.Book;
                                    }
                                    else if (choicePubType == 2)
                                    {
                                        pubType = PublicationType.SerialPublication;
                                    }
                                    else
                                    {
                                        Console.ForegroundColor = ConsoleColor.Red;
                                        Console.WriteLine("Wrong input of publication type");
                                        Console.ForegroundColor = ConsoleColor.White;
                                        break;/////?? exit from switch block
                                    }
                                    Console.WriteLine($"Enter {pubType.GetType()} ID:"); ///
                                    bool correctIDInput = int.TryParse(Console.ReadLine(), out int pubID);
                                    if (correctIDInput)
                                    {
                                        _lib.ReturnPublication(userID, pubType, pubID);  // try/catch here
                                    }
                                    else
                                    {
                                        Console.ForegroundColor = ConsoleColor.Red;
                                        Console.WriteLine($"Wrong input of {pubType.GetType()} ID");
                                        Console.ForegroundColor = ConsoleColor.White;
                                    }
                                }
                                else
                                {
                                    Console.ForegroundColor = ConsoleColor.Red;
                                    Console.WriteLine("Wrong input of publication type");
                                    Console.ForegroundColor = ConsoleColor.White;
                                }
                                break;
                            case 3:
                                SearchMenu();
                                break;
                            case 4:
                                    _lib.DeleteUserAccount(userID);  // try/catch here
                                break;
                            case 5:
                                Console.WriteLine("\n" + "\t" + $"All publications taken by user {user.Login}:");
                                ListAllPubsTaken(userID);
                                break;
                            case 6:
                                ListAllBooks();
                                break;
                            case 7:
                                ListAllSPs();
                                break;
                            case 8:
                                userMenuWorking = false;
                                break;
                            default:
                                Console.ForegroundColor = ConsoleColor.Red;
                                Console.WriteLine("Wrong choice input. No such option number exists. Should be integer 1 to 8");
                                Console.ForegroundColor = ConsoleColor.White;
                                break;
                        }
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Wrong choice input. Should be integer 1 to 8");
                        Console.ForegroundColor = ConsoleColor.White;
                    }
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("User not found");
                Console.ForegroundColor = ConsoleColor.White;
            }
        }

        public static void SearchMenu()
        {
            Console.ForegroundColor = ConsoleColor.DarkCyan;
            Console.WriteLine(
                "\n" +
                "\t" + "Select search parameter:" + "\n" +
                "1. Title" + "\n" +
                "2. ID" + "\n" +
                "3. Author" + "\n");
            Console.ForegroundColor = ConsoleColor.White;
            Console.Write("Your choice: ");
            bool correctSearchParamInput = int.TryParse(Console.ReadLine(), out int choiceSearchParam);
            if (correctSearchParamInput)
            {
                switch (choiceSearchParam)
                {
                    case 1:
                        Console.WriteLine("Enter publication title:");
                        string title = Console.ReadLine();
                        List < Publication > foundPubs= _lib.SearchPublications(title);
                        if (foundPubs.Count == 0)
                        {
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine("No publications found");
                            Console.ForegroundColor = ConsoleColor.White;
                        }
                        else
                        {
                            ListPublications(foundPubs);
                        }
                        break;
                    case 2:
                        Console.WriteLine("Enter publication ID:");
                        bool correctIDInput = int.TryParse(Console.ReadLine(), out int pubID);
                        if (correctIDInput)
                        {
                            foundPubs = _lib.SearchPublications(pubID);
                            if (foundPubs.Count == 0)
                            {
                                Console.ForegroundColor = ConsoleColor.Red;
                                Console.WriteLine("No publications found");
                                Console.ForegroundColor = ConsoleColor.White;
                            }
                            else
                            {
                                ListPublications(foundPubs);
                            }
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine("Wrong input of publication ID");
                            Console.ForegroundColor = ConsoleColor.White;
                        }
                        break;
                    case 3:
                        Console.Write("Enter author's given name: ");
                        string givenName = Console.ReadLine();
                        Console.Write("Enter author's family name: ");
                        string familyName = Console.ReadLine();
                        foundPubs = _lib.SearchPublications((givenName, familyName));
                        if (foundPubs.Count == 0)
                        {
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine("No publications found");
                            Console.ForegroundColor = ConsoleColor.White;
                        }
                        else
                        {
                            ListPublications(foundPubs);
                        }
                        break;
                    default:
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Wrong choice input. Should be integer 1 to 3");
                        Console.ForegroundColor = ConsoleColor.White;
                        break;
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Wrong input of search parameter. Should be integer 1 to 4");
                Console.ForegroundColor = ConsoleColor.White;
            }
        }
    }
}
