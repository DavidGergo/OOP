using System;

namespace _1_Bank
{
    public class InsufficientFundsException : Exception
    {
        public long Hianyzoosszeg { get; }

        public InsufficientFundsException(long hianyzoosszeg) : base("Nincs elegendő fedezet")
        {
            Hianyzoosszeg = hianyzoosszeg;
        }

        public long GetHianyzoOsszeg()
        {
            return Hianyzoosszeg;
        }
    }
    
}


