using System;

namespace LibraryBack.Publications
{
    public class SerialPublication : Publication, IComparable<SerialPublication>
    {
        public SerialPublication(SerialPublication copySP)
            : this(copySP.ID, copySP.Title, copySP.Author)
        { }
        public SerialPublication(int id, string title, (string givenName, string familyName) author)
        {
            ID = id;
            Title = title;
            Author = author;
        }
        public int CompareTo(SerialPublication comparedSP)
        {
            if (comparedSP == null)
                return 0;
            else
                return ID.CompareTo(comparedSP.ID);
        }
        public override string ToString()
        {
            return $"{ID, 3} {Title,-30} {Author.givenName,-15} {Author.familyName,-15}";
        }
    }
}
