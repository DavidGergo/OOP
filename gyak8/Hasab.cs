using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Testek
{
    internal abstract class Hasab
    {

		private int magassag;

        public Hasab(int magassag)
        {
            this.magassag = magassag;
        }

        public int Magassag
		{
			get { return magassag; }
			//set { magassag = value; }
		}

        abstract public double Alapterulet();

        public double Terfogat()
        {
            return Alapterulet()* Magassag;
        }

        public bool TerfogatNagyobbMint(Hasab h2)
        {
            return  Terfogat() > h2.Terfogat();
        }

        public override string ToString()
        {
            return " , Terfogat: " + Terfogat();
        }

	}
}
