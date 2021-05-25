using System;

using LibraryBack.Publications;

namespace LibraryBack.Library.Accounts
{
    public interface IAccount // necessary to write "public"?
    {
        void TakePublication(Publication pub);
        Publication ReturnPublication(PublicationType pubType, int id);
        //void ListAllPublications(); //??????????
    }
}
