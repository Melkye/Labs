using System;

namespace LibraryBack.Publications
{
    public class Book : Publication, IComparable<Book>
    {
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
        public int CompareTo(Book comparedBook)
        {
            if (comparedBook == null)
                return 0;
            else
                return ID.CompareTo(comparedBook.ID);
        }
        public override string ToString()
        {
            return $"{ID, 3} {Title, -30} {Author.givenName, -15} {Author.familyName, -15} {Genre, -15}";
        }

    }
}
