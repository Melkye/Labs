using System;

namespace LibraryBack.Library.Exceptions
{
    public class PublicationNotFoundException : ArgumentException
    {
        public PublicationNotFoundException() :
            base()
        { }
        public PublicationNotFoundException(string message) :
            base(message)
        { }
    }
}
