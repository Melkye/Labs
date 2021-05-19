using System;
using System.Collections.Generic;
using System.Text;

namespace Library
{
    public class Book : Publication//, IEquatable<Book>//IComparable<Book> //??
    {
        // override sn?
        public Book() { } // do I need this?
        public Book(Book copyBook)
            : this(copyBook.ID, copyBook.Title, copyBook.Author, copyBook.Genre)
        {  }
        public Book(int id, string title, (string givenName, string familyName) author, BookGenre genre)
        {
            ID = id;
            Title = title;
            Author = author;
            Genre = genre;
        }

        public BookGenre Genre { get; private set; }
        public bool Equals(Book comparedBook)
        {
            if (comparedBook == null) return false;
            return ID.Equals(comparedBook.ID);
        }
        public override string ToString()
        {
            return $"{Title} {Author.givenName} {Author.familyName} {Genre} {ID}";
        }
        public enum BookGenre { Fantasy, Horror, Thriller, SciFi, NonFiction};

    }
}
