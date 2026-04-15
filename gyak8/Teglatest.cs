using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Testek.Hasabok
{
    internal class Teglatest:Hasab
    {

        private double aOldal;
        private double bOldal;

        public Teglatest(double aOldal, double bOldal, int magassag) : base(magassag)
        {
            this.aOldal = aOldal;
            this.bOldal = bOldal;
        }

        public override double Alapterulet()
        {
            return aOldal*bOldal;
        }
        public override string ToString()
        {
            return "aoldal: " + aOldal + " , boldal: " + bOldal +" , Magassag: " + Magassag + base.ToString();
        }
    }
}
