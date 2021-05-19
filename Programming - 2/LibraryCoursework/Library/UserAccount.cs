using System;
using System.Collections.Generic;
using System.Text;

namespace Library
{
    public class UserAccount : IAccount //change access modif's
    {
        public UserAccount(int id, string login)
        {
            ID = id;
            Login = login;
            PublicationsTaken = new List<Publication>();
        }
        public int ID { get; private set; }
        public string Login { get; private set; }
        public List<Publication> PublicationsTaken { get; private set; } // public get? free to change data?
        public void TakePublication(Publication pub)
        {
            if (pub is Book)
            {
                PublicationsTaken.Add(new Book(pub as Book));
            }
            else
            {
                PublicationsTaken.Add(new SerialPublication(pub as SerialPublication));
            }
        }
        public void ReturnPublication(Publication pub) // call event add pub in library
        {

        }
    }
}
