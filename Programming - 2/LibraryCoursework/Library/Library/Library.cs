using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using LibraryBack.Publications;
using LibraryBack.Library.Accounts;
using LibraryBack.Library.Exceptions;


namespace LibraryBack.Library
{
    /// <summary>
    /// The main Library class.
    /// Contais books, serial publications (aggregation) and user accounts (composition)
    /// and methods to operate them.
    /// </summary>
    public class Library
    {
        private const int MaxTakenPubs = 10;
        private const int MinLoginLength = 3;
        private const int MaxLoginLength = 30;
        private int _uniqueBooksCount = 0;
        private int _uniqueSerialPublicationsCount = 0;
        private int _uniqueUsersCount = 0;
        private List<Book> _bookList;
        private List<SerialPublication> _serialPublicationList;
        private List<UserAccount> _accountList;
        public Library(string name)
        {
            Name = name;
            _bookList = new List<Book>();
            _serialPublicationList = new List<SerialPublication>();
            _accountList = new List<UserAccount>();

            AddPublication(new Book(0, "451° Farenheit", ("Ray", "Bradbury"), BookGenre.Dystopia));
            AddPublication(new Book(0, "To Kill a Mockingbird", ("Harper", "Lee"), BookGenre.Bildungsroman));
            AddPublication(new Book(0, "Winnie-the-Pooh", ("Alan", "Milne"), BookGenre.Children));
            AddPublication(new Book(0, "The House at Pooh Corner", ("Alan", "Milne"), BookGenre.Children));
            AddPublication(new Book(0, "1984", ("George", "Orwell"), BookGenre.Dystopia));
            AddPublication(new Book(0, "A Game of Thrones", ("George", "Martin"), BookGenre.Fantasy));
            AddPublication(new Book(0, "Thinking, Fast and Slow", ("Daniel", "Kahneman"), BookGenre.NonFiction));
            AddPublication(new Book(0, "I, Robot", ("Isaac", "Asimov"), BookGenre.SciFi));
            AddPublication(new Book(0, "The Silent Patient", ("Alex", "Michaelides"), BookGenre.Thriller));
            AddPublication(new Book(0, "When We Were Very Young", ("Alan", "Milne"), BookGenre.Children));
            AddPublication(new Book(0, "The Adventures of Tom Sawyer", ("Mark", "Twain"), BookGenre.Bildungsroman));

            AddPublication(new SerialPublication(0, "Vkluchaiemos nema choho", ("The Great", "Illusionist")));
            AddPublication(new SerialPublication(0, "Let’s learn about touch", ("Bethany", "Brookshire")));
            AddPublication(new SerialPublication(0, "Scientists Say: Pollen", ("Bethany", "Brookshire")));
            AddPublication(new SerialPublication(0, "What are cicadas?", ("Sid", "Perkins")));
            AddPublication(new SerialPublication(0, "Greening your digital life", ("Kathryn", "Hulick")));
        }

        public string Name { get; private set; }
        public List<Book> BookList => new List<Book>(_bookList);
        public List<SerialPublication> SerialPublicationList => new List<SerialPublication>(_serialPublicationList);
        public List<UserAccount> AccountList => new List<UserAccount>(_accountList);

        public void AddPublication(Publication pub)
        {
            if (pub is Book)
            {
                _uniqueBooksCount++;
                _bookList.Add(new Book(_uniqueBooksCount, pub.Title, pub.Author, (pub as Book).Genre));
            }
            else if (pub is SerialPublication)
            {
                _uniqueSerialPublicationsCount++;
                _serialPublicationList.Add(new SerialPublication(_uniqueSerialPublicationsCount, pub.Title, pub.Author));
            }
        }
        /// <exception cref="PublicationNotFoundException">
        /// Thrown when library doesn't have now and didn't have the desired publication before
        /// </exception>
        /// <exception cref="PublicationTakenException">
        /// Thrown when library doesn't have the desired publication because someone took it earlier
        /// </exception>
        /// <exception cref="InvalidIDException">
        /// Thrown when user account with the desired ID doesn't exist in the library
        /// </exception>
        /// <exception cref="PublicationsLimitReachedException">
        /// Thrown when user reached the limit of 10 publications and wants to take one more
        /// </exception>
        public void TakePublication(int userID, PublicationType pubType, int pubID)
        {
            if (pubType == PublicationType.Book)
            {
                if (pubID > 0 && pubID <= _uniqueBooksCount)
                {
                    if (_bookList.Exists(x => x.ID == pubID))
                    {
                        Book book = _bookList.Find(x => x.ID == pubID);
                        UserAccount user = FindUserAccount(userID);
                        if (user != null)
                        {
                            if (user.PublicationsTaken.Count < MaxTakenPubs)
                            {
                                user.TakePublication(book);
                                _bookList.Remove(book);
                            }
                            else
                                throw new PublicationsLimitReachedException("Max quantity of publications reached. Return a publication to take a new one");
                        }
                        else
                            throw new InvalidIDException("No user with such ID found");
                    }
                    else
                        throw new PublicationTakenException("Someone took this book");
                }
                else
                    throw new PublicationNotFoundException("No such books in library");
            }
            else if (pubType == PublicationType.SerialPublication)
            {
                if (_serialPublicationList.Exists(x => x.ID == pubID))
                {
                    SerialPublication serialPublication = _serialPublicationList.Find(x => x.ID == pubID);
                    UserAccount user = FindUserAccount(userID);
                    if (user != null)
                    {
                        if (user.PublicationsTaken.Count < MaxTakenPubs)
                        {
                            user.TakePublication(serialPublication);
                            _serialPublicationList.Remove(serialPublication);
                        }
                        else
                            throw new PublicationsLimitReachedException("Max quantity of publications reached. Return a publication to take a new one");
                    }
                    else
                        throw new InvalidIDException("No user with such ID found");
                }
                else if (pubID <= _uniqueSerialPublicationsCount)
                    throw new PublicationTakenException("Someone took this SP");
                else
                    throw new PublicationNotFoundException("No such SPs in library");
            }
        }
        /// <exception cref="InvalidIDException">
        /// Thrown when user account with the desired ID doesn't exist in the library
        /// </exception>
        /// <exception cref="PublicationNotFoundException">
        /// Thrown when user has no such publication taken as specified
        /// </exception>
        public void ReturnPublication(int userID, PublicationType pubType, int pubID)
        {
            UserAccount user = FindUserAccount(userID);
            if (user != null)
            {
                if (user.PublicationsTaken.Count == 0)
                    throw new PublicationNotFoundException("Nothing to return");
                Publication returnPub = user.ReturnPublication(pubType, pubID);
                if (returnPub != null)
                {
                    if (returnPub is Book)
                    {
                        _bookList.Add(returnPub as Book);
                        _bookList.Sort();
                    }
                    else
                    {
                        _serialPublicationList.Add(returnPub as SerialPublication);
                        _serialPublicationList.Sort();
                    }
                }
                else
                    throw new PublicationNotFoundException("User didn't take such publication");
            }
            else
                throw new InvalidIDException("Invalid user ID");
        }
        /// <exception cref="InvalidLoginException">
        /// Thrown when specified login already exists in other account; when login is too short or too long
        /// </exception>
        public void CreateUserAccount(string login)
        {
            if (login.Length < MinLoginLength || login.Length > MaxLoginLength)
            {
                throw new InvalidLoginException($"Inappropriate login length. Should be {MinLoginLength} to {MaxLoginLength} symbols long");
            }
            else if (_accountList.Exists(x => x.Login == login))
            {
                throw new InvalidLoginException("An account with such login already exists");
            }
            else
            {
                _uniqueUsersCount++;
                _accountList.Add(new UserAccount(_uniqueUsersCount, login));
            }
        }
        /// <exception cref="PublicationTakenException">
        /// Thrown when user has one or more publications taken and wants to delete their account
        /// </exception>
        public void DeleteUserAccount(int userID)
        {
            UserAccount user = FindUserAccount(userID);
            if (user != null)
            {
                if (user.PublicationsTaken.Count != 0)
                {
                    throw new PublicationTakenException("You must return all taken publications before deleting your account");
                }
                else
                {
                    _accountList.Remove(user);
                }
                   
            }
        }
        /// <summary>
        /// Searches for an account having specified ID
        /// </summary>
        /// <returns>
        /// UserAccount object. null if user wasn't found
        /// </returns>
        public UserAccount FindUserAccount(int userID)
        {
            foreach (UserAccount user in _accountList)
            {
                if (user.ID == userID)
                {
                    return user;
                }
            }
            return null;
        }
        /// <summary>
        /// Searches for an account having specified login
        /// </summary>
        /// <returns>
        /// UserAccount object. null if user wasn't found
        /// </returns>
        public UserAccount FindUserAccount(string login)
        {
            foreach (UserAccount user in _accountList)
            {
                if (user.Login == login)
                {
                    return user;
                }
            }
            return null;
        }
        /// <summary>
        /// Searches for all publications (both books and SPs) having specified ID 
        /// </summary>
        /// <returns>
        /// List of found publications. Empty list if no publication found.
        /// </returns>
        public List<Publication> SearchPublications(int id)
        {
            List<Publication> foundPublications = new List<Publication>();
            foundPublications.AddRange(_bookList.FindAll(x => x.ID == id));
            foundPublications.AddRange(_serialPublicationList.FindAll(x => x.ID == id));
            return foundPublications;
        }
        /// <summary>
        /// Searches for all publications (both books and SPs) containing specified string in title
        /// </summary>
        /// <returns>
        /// List of found publications. Empty list if no publication found.
        /// </returns>
        public List<Publication> SearchPublications(string title)
        {
            List<Publication> foundPublications = new List<Publication>();
            foundPublications.AddRange(_bookList.FindAll(x => x.Title.Contains(title)));
            foundPublications.AddRange(_serialPublicationList.FindAll(x => x.Title.Contains(title)));
            return foundPublications;
        }
        /// <summary>
        /// Searches for all publications (both books and SPs) having specified author
        /// </summary>
        /// <returns>
        /// List of found publications. Empty list if no publication found.
        /// </returns>
        public List<Publication> SearchPublications((string givenName, string familyName) author)
        {
            List<Publication> foundPublications = new List<Publication>();
            foundPublications.AddRange(_bookList.FindAll(x => x.Author == author));
            foundPublications.AddRange(_serialPublicationList.FindAll(x => x.Author == author));
            return foundPublications;
        }
    }
}