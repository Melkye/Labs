using System;

namespace LibraryBack.Library.Exceptions
{
    public class PublicationTakenException : InvalidOperationException
    {
        public PublicationTakenException() :
            base()
        { }
        public PublicationTakenException(string message) :
            base(message)
        { }
    }
}
