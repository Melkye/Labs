using System;

namespace LibraryBack.Library.Exceptions
{
    class PublicationTakenException : InvalidOperationException
    {
        public PublicationTakenException() :
            base()
        { }
        public PublicationTakenException(string message) :
            base(message)
        { }
    }
}
