using System;

namespace LibraryBack.Library.Exceptions
{
    public class InvalidPublicationTypeException : ArgumentException
    {
        public InvalidPublicationTypeException() :
            base()
        { }
        public InvalidPublicationTypeException(string message) : // should be string? or it works well?
            base(message)
        { }
        public InvalidPublicationTypeException(string message, string paramName) : ////??????????????
            base(message, paramName)
        { }
    }
}
