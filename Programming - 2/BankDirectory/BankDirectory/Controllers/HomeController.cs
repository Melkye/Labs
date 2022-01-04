using BankDirectory.Data;
using BankDirectory.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;

namespace BankDirectory.Controllers
{
    public class HomeController : Controller
    {
        private readonly BankDirectoryContext _bankDirectoryContext;

        public HomeController(BankDirectoryContext context)
        {
            _bankDirectoryContext = context;
        }

        public IActionResult Index()
        {
            return View(_bankDirectoryContext.Banks.ToList());
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
