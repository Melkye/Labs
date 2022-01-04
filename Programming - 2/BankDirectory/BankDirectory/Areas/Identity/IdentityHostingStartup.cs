using System;
using BankDirectory.Areas.Identity.Data;
using BankDirectory.Data;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Identity.UI;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

[assembly: HostingStartup(typeof(BankDirectory.Areas.Identity.IdentityHostingStartup))]
namespace BankDirectory.Areas.Identity
{
    public class IdentityHostingStartup : IHostingStartup
    {
        public void Configure(IWebHostBuilder builder)
        {
            builder.ConfigureServices((context, services) => {
                services.AddDbContext<BankDirectoryContext>(options =>
                    options.UseSqlServer(
                        context.Configuration.GetConnectionString("BankDirectoryContextConnection")));

                services.AddDefaultIdentity<BankDirectoryUser>(options => {
                    options.SignIn.RequireConfirmedAccount = false;
                    options.Password.RequireUppercase = false;
                    options.Password.RequireLowercase = false;
                    options.Password.RequireNonAlphanumeric = false;
                    })
                    .AddEntityFrameworkStores<BankDirectoryContext>();
            });
        }
    }
}