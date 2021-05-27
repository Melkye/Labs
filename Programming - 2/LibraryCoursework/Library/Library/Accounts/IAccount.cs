using LibraryBack.Publications;

namespace LibraryBack.Library.Accounts
{
    interface IAccount
    {
        void TakePublication(Publication pub);
        Publication ReturnPublication(PublicationType pubType, int id);
    }
}
