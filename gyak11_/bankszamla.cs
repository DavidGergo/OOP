using _1_Bank;
using System;

namespace Bank
{
    internal class Bankszamla
    {
        private long egyenleg;
        private string szamlaszam;

        public long Egyenleg
        {
            get { return egyenleg; }
        }

        public string Szamlaszam
        {
            get { return szamlaszam; }
        }

        public Bankszamla(string szsz)
        {
            this.egyenleg = 0;
            this.szamlaszam = szsz;
        }

        public void Penzbefizetes(long value)
        {
            if (value <= 0)
            {
                Console.WriteLine("Pozitiv kell legyen");
            }
            egyenleg += value;
        }

        public void Penzkivetel(long value)
        {
            if (value <= 0)
            {
                Console.WriteLine("Pozitiv kell legyen");
                return;
            }

            if (egyenleg >= value)
            {
                egyenleg -= value;
            }
            else
            {
                throw new InsufficientFundsException(value - egyenleg);
            }
        }
        
        public override string ToString()
        {
            return $"{Szamlaszam} egyenlege: {egyenleg}";
        }

    }

}
