using System;

namespace LibraryBack.Library.Exceptions
{
    public class PublicationsLimitReachedException : InvalidOperationException
    {
        public PublicationsLimitReachedException() :
            base()
        { }
        public PublicationsLimitReachedException(string message) :
            base(message)
        { }
    }
}
