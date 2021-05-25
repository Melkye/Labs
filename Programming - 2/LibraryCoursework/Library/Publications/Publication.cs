
namespace LibraryBack.Publications
{
    public abstract class Publication //partial to insert into library class?
    {
        // make all this overridable
        public int ID { get; protected set; }
        public string Title { get; protected set; } //how admin will access this?
        public (string givenName, string familyName) Author { get; protected set; } 

    }
}
