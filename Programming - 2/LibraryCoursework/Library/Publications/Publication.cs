
namespace LibraryBack.Publications
{
    public abstract class Publication
    {
        public int ID { get; protected set; }
        public string Title { get; protected set; }
        public (string givenName, string familyName) Author { get; protected set; } 

    }
}
