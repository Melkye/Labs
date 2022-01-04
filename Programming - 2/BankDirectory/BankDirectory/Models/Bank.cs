using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Threading.Tasks;

namespace BankDirectory.Models
{
    public class Bank
    {
        public int Id {get; set; }
        [DisplayName("Назва банку")]
        public string Title {get; set; }
        [DisplayName("Рік заснування")]
        public int FoundationYear {get; set; }
        [DisplayName("Голова")]
        public string CEO { get; set; }
        [DisplayName("Прибуток")]
        public double NetIncome { get; set; } 
    }
}
