using System;
using System.Collections.Generic;

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
        private int _uniqueBooksCount = 0;
        private int _uniqueSerialPublicationsCount = 0;
        private int _uniqueUsersCount = 0;
        private List<Book> _bookList;                                //change access modif's!!!!
        private List<SerialPublication> _serialPublicationList;
        private List<UserAccount> _accountList;     //make List<UserAccount>?
        public Library(string name)
        {
            Name = name;
            _bookList = new List<Book>();
            _serialPublicationList = new List<SerialPublication>();
            _accountList = new List<UserAccount>();

            AddPublication(new Book(0, "451° Farenheit", ("Ray", "Bradbury"), BookGenre.Dystopia));
            AddPublication(new Book(0, "To Kill a Mockingbird", ("Harper", "Lee"), BookGenre.Bildungsroman));
            AddPublication(new Book(0, "Winnie-the-Pooh", ("Alan", "Milne"), BookGenre.Children));

            AddPublication(new SerialPublication(0, "Включаемось нама чого", ("The Great", "Illusionist")));
            AddPublication(new SerialPublication(0, "A name", ("An", "Author")));
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
                _bookList.Sort();
            }
            else if (pub is SerialPublication)
            {
                _uniqueSerialPublicationsCount++;
                _serialPublicationList.Add(new SerialPublication(_uniqueSerialPublicationsCount, pub.Title, pub.Author));
                _serialPublicationList.Sort();
            }
        }
        /// <exception cref="PublicationNotFoundException">
        /// Thrown when library doesn't have the book subjected to remove
        /// </exception>
        public void RemoveBook(int bookID)
        {
            if (_bookList.Exists(x => x.ID == bookID))
            {
                _bookList.Remove(_bookList.Find(x => x.ID == bookID));
            }
            else
                throw new PublicationNotFoundException("Library doesn't contain this book. Removal is impossible.");
        }
        /// <exception cref="PublicationNotFoundException">
        /// Thrown when library doesn't have the SP subjected to remove
        /// </exception>
        public void RemoveSP(int serialPublicationID)
        {
            if (_serialPublicationList.Exists(x => x.ID == serialPublicationID))
            {
                _serialPublicationList.Remove(_serialPublicationList.Find(x => x.ID == serialPublicationID));
            }
            else
                throw new PublicationNotFoundException("Library doesn't contain this serial publication. Removal is impossible.");
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
                else if (pubID <= _uniqueBooksCount)
                    throw new PublicationTakenException("Someone took this book");
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
            //else
            //    throw new InvalidPublicationTypeException("Invalid publication type");
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
                Publication returnPub = user.ReturnPublication(pubType, pubID);
                if (returnPub != null)
                {
                    if (returnPub is Book)
                        _bookList.Add(returnPub as Book);
                    else
                        _serialPublicationList.Add(returnPub as SerialPublication);
                }
                else
                    throw new PublicationNotFoundException("User didn't take such publication");
            }
            else
                throw new InvalidIDException("Invalid user ID");
        }
        public void CreateUserAccount(string login)
        {
            _uniqueUsersCount++;
            _accountList.Add(new UserAccount(_uniqueUsersCount, login));
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
                    throw new PublicationTakenException("You must return all taken publications before deleting your account");
                else
                    _accountList.Remove(user);
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
            foundPublications.AddRange(_serialPublicationList.FindAll(x => x.Title == title));
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