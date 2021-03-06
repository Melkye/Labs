﻿using System.Collections.Generic;

using LibraryBack.Publications;

namespace LibraryBack.Library.Accounts
{
    public class UserAccount : IAccount
    {
        private List<Publication> _publicationsTaken;
        public UserAccount(int id, string login)
        {
            ID = id;
            Login = login;

            _publicationsTaken = new List<Publication>();
        }
        public int ID { get; private set; }
        public string Login { get; private set; }

        public List<Publication> PublicationsTaken
        {
            get => new List<Publication>(_publicationsTaken);
        }
        public void TakePublication(Publication pub)
        {
            if (pub is Book)
            {
                _publicationsTaken.Add(new Book(pub as Book));
            }
            else
            {
                _publicationsTaken.Add(new SerialPublication(pub as SerialPublication));
            }
        }
        public Publication ReturnPublication(PublicationType pubType, int id)
        {
            Publication returnPub = null;
            if (pubType == PublicationType.Book)
            {
                if (_publicationsTaken.Exists(x => x is Book && x.ID == id))
                {
                    returnPub = new Book(_publicationsTaken.Find(x => x is Book && x.ID == id) as Book);
                    _publicationsTaken.Remove(_publicationsTaken.Find(x => x is Book && x.ID == id));
                }
            }
            else if (pubType == PublicationType.SerialPublication)
            {
                if (_publicationsTaken.Exists(x => x is SerialPublication && x.ID == id))
                {
                    returnPub = new SerialPublication(_publicationsTaken.Find(x => x is SerialPublication && x.ID == id) as SerialPublication);
                    _publicationsTaken.Remove(_publicationsTaken.Find(x => x is SerialPublication && x.ID == id));
                }
            }
            return returnPub;
        }
    }
}
