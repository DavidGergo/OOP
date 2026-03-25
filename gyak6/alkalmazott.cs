using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AlkalmazottNevter
{
    internal class Alkalmazott
    {
		private string nev;
		private int kor;
		private long fizetes;
		private static int nyugdijkorhatar = 65;

        public Alkalmazott(string nev, int kor, long fizetes)
        {
            this.nev = nev;
            this.kor = kor;
            this.fizetes = fizetes;
        }
        public Alkalmazott(string nev, int kor) : this(nev, kor, 10000 * kor)
        {

        }
        public Alkalmazott() : this("nevtelen", 25) 
		{
		
		}

        public static int Nyugdij_korhatar
		{
			get { return nyugdijkorhatar; }
			set { nyugdijkorhatar = value; }
		}

		public static void SetNyugdijkorhatar(int value)
		{
			nyugdijkorhatar = value;
		}

		public long Fizetes
		{
			get { return fizetes; }
			set { fizetes = value; }
		}

		public int Kor
		{
			get { return kor; }
			set { kor = value; }
		}

		public string Nev
		{
			get { return nev; }
			set { nev = value; }
		}

        internal int EvekNyugdijig()
        {
			return Nyugdij_korhatar - kor;
        }

		public static Alkalmazott TobbEveVanNyugdijig(Alkalmazott egyik, Alkalmazott masik)
		{
			if (egyik.EvekNyugdijig() > masik.EvekNyugdijig())
			{
				return egyik;
			}

			return masik;
        }
        
		public override string ToString()
        {
			return "nev: " + Nev + ", kor: " + Kor + ", Fizetés: " + Fizetes + ", Évek Nyugdíjig: " + EvekNyugdijig();
        }




    }
}
