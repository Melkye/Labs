using System;
using System.Collections.Generic;
using System.Text;

namespace Library
{
    public class SerialPublication : Publication
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
        public bool Equals(SerialPublication comparedSP)
        {
            if (comparedSP == null) return false;
            return ID.Equals(comparedSP.ID);
        }
        public override string ToString()
        {
            return $"{Title} {Author.givenName} {Author.familyName} {ID}";
        }
    }
}
