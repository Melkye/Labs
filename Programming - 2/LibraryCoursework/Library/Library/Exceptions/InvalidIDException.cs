using System;

namespace LibraryBack.Library.Exceptions
{
    public class InvalidIDException : ArgumentException
    {
        public InvalidIDException() :
            base()
        { }
        public InvalidIDException(string message) :
            base(message)
        { }
    }
}
