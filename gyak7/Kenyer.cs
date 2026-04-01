using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Termekek.Elelmiszerek
{
    class Kenyer : Aru
    {
        //double mennyiseg;

        private double mennyiseg;

        public double Mennyiseg
		{
			get { return mennyiseg; }
			//set { mennyiseg = value; }
		}

        public Kenyer(string nev, int ar, int afa, double mennyiseg) : base(nev, ar, afa)
        {
            this.mennyiseg = mennyiseg;
            //this.mennyiseg =
        }

        public override string ToString()
        {
            return base.ToString() + "egysegar: " + String.Format("{0:n3}", Brutto_ar/mennyiseg);
        }

        public static bool ElsoNagyobbEgysegar(Kenyer egyik, Kenyer masik)
        {
            if (egyik.Brutto_ar / egyik.Mennyiseg > masik.Brutto_ar / masik.Mennyiseg)
            {
                return true;
            }
            else return false;
        }

        public int DragabbE(Kenyer egyik, int mint)
        {
            if (egyik.Netto_ar > mint)
            {
                return 1;
            }
            else if (egyik.Netto_ar == mint)
            {
                return 0;
            }
            else return -1;
        }

    }
}
