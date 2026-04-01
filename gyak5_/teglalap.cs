using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;

namespace gyak5_1
{
    internal class Teglalap
    {


        private int elsooldal;
        private int masodikoldal;

        public Teglalap(int nagyzetoldal) : this(nagyzetoldal, nagyzetoldal)
        {
            
        }

        public bool Terulet_nagyobb_mint(Teglalap other)
        {
            return Terulet() > other.Terulet();
        }

        public bool Oldalak_egyezik( Teglalap other)
        {
            return Elso_oldal == other.Elso_oldal && Masodik_oldal == other.Masodik_oldal;
        }

        public Teglalap(int elsooldal, int masodikoldal)
        {
            Set_sides(elsooldal, masodikoldal);
        }

        //overloading - túlterhelés
        public void Set_sides(int a_side, int b_side)
        {
            this.elsooldal = a_side;
            this.masodikoldal = b_side;
        }

        public void Set_teglalap(int negyzetoldal)
        {
            Set_sides(negyzetoldal, negyzetoldal);
        }

        public int Elso_oldal 
        {
            get { return elsooldal; }
            set { elsooldal = value; } 
        }
        
        public int Masodik_oldal
        {
            get { return masodikoldal; }
            set { masodikoldal = value; }
        }

        public int Terulet()
        {
            return (elsooldal * masodikoldal);
        }
        public override string ToString()
        {
            return "  " + elsooldal + ", " + masodikoldal + " : " + Terulet();
        }
    }
}
