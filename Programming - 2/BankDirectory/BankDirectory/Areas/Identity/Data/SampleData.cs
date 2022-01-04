using BankDirectory.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BankDirectory.Data
{
    public class SampleData
    {
        public static void Initialize(BankDirectoryContext context)
        {
            if (!context.Banks.Any())
            {
                context.Banks.AddRange(
                    new Bank
                    {
                        Title = "PryvitBank",
                        FoundationYear = 1992,
                        CEO = "Ідол Оболонський",
                        NetIncome = 11.6
                    },
                    new Bank
                    {
                        Title = "PolyBank",
                        FoundationYear = 2017,
                        CEO = "Ольгерд Бобовський",
                        NetIncome = 1.65
                    },
                    new Bank
                    {
                        Title = "БУМБ",
                        FoundationYear = 2006,
                        CEO = "Еразм Роттердамський",
                        NetIncome = 1.98
                    },
                    new Bank
                    {
                        Title = "Шлаффхайзен Банк",
                        FoundationYear = 1993,
                        CEO = "Євген Німецький",
                        NetIncome = 2.33
                    }
                    );
                context.SaveChanges();
            }
        }
    }
}
