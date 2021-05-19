using System;
using System.Collections.Generic;
using System.Text;

namespace Library
{
    public interface IAccount // necessary to write "public"?
    {
        void TakePublication(Publication pub);
        void ReturnPublication(Publication pub);
        //void ListAllPublications(); //??????????
    }
}
