using System;
using System.Collections.Generic;
using System.Diagnostics.Tracing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Termekek.Elelmiszerek;

namespace Termekek
{
    class Aru
    {

        private string nev;
        private int netto_ar;
        private int afa_kulcs;

        public string Nev
        {
            get { return nev; }
            set { nev = value; }
        }

        public int Netto_ar
        {
            get { return netto_ar; }
            set { netto_ar = value; }
        }

        public int Afa_kulcs
        {
            get { return afa_kulcs; }
            set { afa_kulcs = value; }
        }


        public Aru(string nev, int ar, int afa) 
        {
           this.nev = nev;
            this.netto_ar = ar;
            this.afa_kulcs = afa;

        }
        public Aru(string nev, int afa) : this("aru", 2500,  afa) 
        {
            this.nev = nev;
            this.netto_ar = 2500;
            this.afa_kulcs = afa;

        }

        public int Brutto_ar
        {
            get { return Convert.ToInt32(netto_ar * (1 + afa_kulcs / 100.0)); }
        }

        public void Netto_novel(int szazalek)
        {
            netto_ar = SzazalekNovelo(szazalek);
        }

        private int SzazalekNovelo(int szazalek)
        {
            return -1;
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
