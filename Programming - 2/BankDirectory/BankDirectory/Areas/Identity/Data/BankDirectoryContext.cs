using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using BankDirectory.Areas.Identity.Data;
using BankDirectory.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;

namespace BankDirectory.Data
{
    public class BankDirectoryContext : IdentityDbContext<BankDirectoryUser>
    {
        public DbSet<BankDirectoryUser> BankDirectoryUsers { get; set; }
        public DbSet<Bank> Banks { get; set; }
        public BankDirectoryContext(DbContextOptions<BankDirectoryContext> options)
            : base(options)
        {
            Database.EnsureCreated();
        }
    }
}
