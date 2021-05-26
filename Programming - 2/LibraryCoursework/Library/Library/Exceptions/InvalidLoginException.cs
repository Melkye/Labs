using System;

namespace LibraryBack.Library.Exceptions
{
    public class InvalidLoginException : ArgumentException
    {
        public InvalidLoginException() :
            base()
        { }
        public InvalidLoginException(string message) :
            base(message)
        { }
    }
}
