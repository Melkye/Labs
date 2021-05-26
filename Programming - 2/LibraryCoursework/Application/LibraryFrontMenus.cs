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
                    PrintErrorMessage("Wrong choice input.  Should be integer 1 to 6");
                }
                switch (choice)
                {
                    case 1:
                        Console.Write("Enter account ID: ");
                        correctInput = int.TryParse(Console.ReadLine(), out int userID);
                        if (correctInput)
                        {
                            UserMenu(userID);
                        }
                        else
                        {
                            PrintErrorMessage("Wrong input of account ID");
                        }
                        break;
                    case 2:
                        Console.Write("Enter new login: ");
                        string login = Console.ReadLine();
                        if (CreateUserAccount(login))
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
                        startMenuWorking = false;
                        break;
                    default:
                        PrintErrorMessage("Wrong choice input. No such option number exists. Should be integer 1 to 6");
                        break;
                }
            }
        }
        private static void UserMenu(int userID)
        {
            if (userID > 0)
            {
                UserAccount user = _lib.FindUserAccount(userID);
                if (user != null)
                {
                    bool userMenuWorking = true;
                    while (userMenuWorking)
                    {
                        Console.WriteLine("\n" + $"User: {user.Login} \t ID: {user.ID}");
                        Console.ForegroundColor = ConsoleColor.Blue;
                        Console.WriteLine(
                            "\t" + "Select an option:" + "\n" +
                            "1. Take a publication" + "\t\t" + "5. List all taken publications" + "\n" +
                            "2. Return a publication" + "\t\t" + "6. List all available books" + "\n" +
                            "3. Search " + "\t" + "\t\t" + "7. List all available serial publications" + "\n" +
                            "4. Delete account" + "\t\t" + "8. Exit" + "\n\n");
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
                                            ListAllBooks();
                                            Console.Write("Enter book's ID: ");
                                        }
                                        else if (choicePubType == 2)
                                        {
                                            pubType = PublicationType.SerialPublication;
                                            ListAllSPs();
                                            Console.Write("Enter SP's ID: ");
                                        }
                                        else
                                        {
                                            PrintErrorMessage("Wrong input of publication type. Should be integer 1 or 2");
                                            break;
                                        }
                                        bool correctIDInput = int.TryParse(Console.ReadLine(), out int pubID);
                                        if (correctIDInput)
                                        {
                                            TakePublication(userID, pubType, pubID);
                                        }
                                        else
                                        {
                                            PrintErrorMessage("Wrong input of ID. Should be integer greater than 0");
                                        }
                                    }
                                    else
                                    {
                                        PrintErrorMessage("Wrong input of publication type. Should be 1 or 2");
                                    }
                                    break;
                                case 2:
                                    if (user.PublicationsTaken.Count == 0)
                                    {
                                        Console.WriteLine("Nothing to return");
                                        break;
                                    }
                                    else
                                    {
                                        ListAllPubsTaken(userID);
                                    }
                                    Console.WriteLine(
                                        "\n" +
                                        "\t" + "Select publication type:" + "\n" +
                                        "1. Book" + "\n" +
                                        "2. Serial publication" + "\n");
                                    Console.Write("Your choice: ");
                                    correctPubTypeInput = int.TryParse(Console.ReadLine(), out choicePubType);
                                    if (correctPubTypeInput)
                                    {
                                        PublicationType pubType;
                                        if (choicePubType == 1)
                                        {
                                            pubType = PublicationType.Book;
                                            Console.Write("Enter book's ID: ");
                                        }
                                        else if (choicePubType == 2)
                                        {
                                            pubType = PublicationType.SerialPublication;
                                            Console.Write("Enter SP's ID: ");
                                        }
                                        else
                                        {
                                            PrintErrorMessage("Wrong input of publication type. Should be 1 or 2");
                                            break;
                                        }
                                        bool correctIDInput = int.TryParse(Console.ReadLine(), out int pubID);
                                        if (correctIDInput)
                                        {
                                            ReturnPublication(userID, pubType, pubID);
                                        }
                                        else
                                        {
                                            PrintErrorMessage("Wrong input of ID. Should be integer greater than 0");
                                        }
                                    }
                                    else
                                    {
                                        PrintErrorMessage("Wrong input of publication type. Should be integer 1 or 2");
                                    }
                                    break;
                                case 3:
                                    SearchMenu();
                                    break;
                                case 4:
                                    DeleteUserAccount(userID);
                                    userMenuWorking = false;
                                    break;
                                case 5:
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
                                    PrintErrorMessage("Wrong choice input. No such option number exists. Should be integer 1 to 8");
                                    break;
                            }
                        }
                        else
                        {
                            PrintErrorMessage("Wrong choice input. Should be integer 1 to 8");
                        }
                    }
                }
                else
                {
                    PrintErrorMessage("User not found");
                }
            }
            else
            {
                PrintErrorMessage("Wrong user ID input. Must be integer greater than 0");
            }
            
        }
        private static void SearchMenu()
        {
            Console.ForegroundColor = ConsoleColor.DarkCyan;
            Console.WriteLine(
                "\n" +
                "\t" + "Select search parameter:" + "\n" +
                "1. Title"  + "\t" + "- searches for publications that contain specified symbols" + "\n" +
                "2. ID   "  + "\t" + "- searches for publications that have specified ID" + "\n" +
                "3. Author" + "\t" + "- searches for publications that have specified author" + "\n");
            Console.ForegroundColor = ConsoleColor.White;
            Console.Write("Your choice: ");
            bool correctSearchParamInput = int.TryParse(Console.ReadLine(), out int choiceSearchParam);
            if (correctSearchParamInput)
            {
                switch (choiceSearchParam)
                {
                    case 1:
                        Console.Write("Enter publication title: ");
                        string title = Console.ReadLine();
                        List < Publication > foundPubs= _lib.SearchPublications(title);
                        if (foundPubs.Count == 0)
                        {
                            PrintErrorMessage("No publications found");
                        }
                        else
                        {
                            Console.WriteLine("\n" + "\t" + "All found publications: ");
                            ListPublications(foundPubs);
                        }
                        break;
                    case 2:
                        Console.Write("Enter publication ID: ");
                        bool correctIDInput = int.TryParse(Console.ReadLine(), out int pubID);
                        if (correctIDInput)
                        {
                            foundPubs = _lib.SearchPublications(pubID);
                            if (foundPubs.Count == 0)
                            {
                                PrintErrorMessage("No publications found");
                            }
                            else
                            {
                                Console.WriteLine("\n" + "\t" + "All found publications: ");
                                ListPublications(foundPubs);
                            }
                        }
                        else
                        {
                            PrintErrorMessage("Wrong input of publication ID");
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
                            PrintErrorMessage("No publications found");
                        }
                        else
                        {
                            Console.WriteLine("\n" + "\t" + "All found publications: ");
                            ListPublications(foundPubs);
                        }
                        break;
                    default:
                        PrintErrorMessage("Wrong choice input. Should be integer 1 to 3");
                        break;
                }
            }
            else
            {
                PrintErrorMessage("Wrong input of search parameter. Should be integer 1 to 4");
            }
        }
    }
}
