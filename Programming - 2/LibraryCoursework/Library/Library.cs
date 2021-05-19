using System;
using System.Collections.Generic;

namespace Library
{
    public class Library//<T> where T : IAccount//?????????????
    {
        private int _uniqueBooksCount = 0;
        private int _uniqueSerialPublicationsCount = 0;
        public List<Book> books;                                //change access modif's!!!!
        public List<SerialPublication> serialPublications;
        public List<IAccount> accounts;
        public Library(string name) // pass lists of books ans SPs?
        {
            Name = name;
            books = new List<Book>();
            serialPublications = new List<SerialPublication>();
            accounts = new List<IAccount>();
        }
        public string Name { get; private set; }

        public void AddPublication(Publication pub)
        {
            if (pub is Book)
            {
                books.Add(new Book(_uniqueBooksCount + 1, pub.Title, pub.Author, (pub as Book).Genre));
                _uniqueBooksCount++;
            }
            else if (pub is SerialPublication)
            {
                serialPublications.Add(new SerialPublication(_uniqueSerialPublicationsCount + 1,
                    pub.Title, pub.Author));
                _uniqueSerialPublicationsCount++;
            }
            else // can this even exist? if so? change UserAccount.TakePublication method
            {
                throw new ArgumentException("Impossible to add an item that's not a publication");
            }
        }
        public void RemoveBook(int bookID)
        {
            if (books.Exists(x => x.ID == bookID))
            {
                books.Remove(books.Find(x => x.ID == bookID));
            }
            else
                throw new ArgumentException("Library doesn't contain this book. Deletion is impossible.");
        }
        public void RemoveSP(int serialPublicationID)
        {
            if (serialPublications.Exists(x => x.ID == serialPublicationID))
            {
                serialPublications.Remove(serialPublications.Find(x => x.ID == serialPublicationID));
            }
            else
                throw new ArgumentException("Library doesn't contain this serial publication. Deletion is impossible.");
        }
        public void TakePublication(int userID, PublicationType pubType, int publicationID)
        {
            switch (pubType)
            {
                case PublicationType.Book:
                    if (books.Exists(x => x.ID == publicationID))
                    {
                        Book book = books.Find(x => x.ID == publicationID);
                        UserAccount user = FindUserAccount(userID);
                        if (user != null)
                        {
                            user.TakePublication(book);
                        }
                        else
                            throw new ArgumentException("Invalid user ID");
                    }
                    else
                        throw new ArgumentException("Book not found");
                    break;
                case PublicationType.SerialPublication:
                    if (serialPublications.Exists(x => x.ID == publicationID))
                    {
                        SerialPublication serialPublication = serialPublications.Find(x => x.ID == publicationID);
                        UserAccount user = FindUserAccount(userID);
                        if (user != null)
                        {
                            user.TakePublication(serialPublication);
                        }
                        else
                            throw new ArgumentException("Invalid user ID");
                    }
                    else
                        throw new ArgumentException("SerialPublication not found");
                    break;

            }
        }

        public UserAccount FindUserAccount(int userID)
        {
            foreach (UserAccount user in accounts)
            {
                if (user.ID == userID)
                {
                    return user;
                }
            }
            throw new ArgumentException("User not found"); //??
            return null;
        }
        public enum PublicationType { Book, SerialPublication }
    }
}
