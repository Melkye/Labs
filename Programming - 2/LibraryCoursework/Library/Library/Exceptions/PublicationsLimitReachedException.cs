using System;

namespace LibraryBack.Library.Exceptions
{
    class PublicationsLimitReachedException : InvalidOperationException
    {
        public PublicationsLimitReachedException() :
            base()
        { }
        public PublicationsLimitReachedException(string message) :
            base(message)
        { }
    }
}
