using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Testek.Henger
{
    internal class Henger : Hasab
    {
		private double sugar;

        public Henger(double sugar, int magassag) : base(magassag)
        {
            this.sugar = sugar;
        }

        public override double Alapterulet()
        {
            return sugar * sugar * Math.PI;
        }
        public override string ToString()
        {
            return "Sugar: " + sugar + " , Magassag: " + Magassag + base.ToString();
        }
    }
}
