using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Testek.Henger;

namespace Testek
{
    internal class HasabTomb
    {
        Hasab[] hasabok;

        public HasabTomb(int hasabokMaximalisSzama)
        {
            this.hasabok = new Hasab[hasabokMaximalisSzama];
        }

        public void HasabHozzaad(int index, Hasab hasab)
        {
            this.hasabok[index] = hasab;
        }

        public int HasabokMaximalisSzama()
        {
            return this.hasabok.Length;
        }

        public Hasab GetHasab(int index)
        {
            return this.hasabok[index];
        }

        public int NemNullErtekuTombelem()
        {
            int counter = 0;
            foreach (Hasab item in hasabok)
            {
                if (item != null)
                {
                    counter++;
                }
            }

            if (NemNullErtekuTombelem() == 0)
            {
                return -1;
            }
            return counter;
        }

        public double HasabokAtlagTerfogata()
        {
            double terfogatok = 0;

            foreach (Hasab item in hasabok)
            {
                if (item != null)
                {
                    terfogatok += item.Terfogat();
                }
                
            }

            return terfogatok/NemNullErtekuTombelem();
        }

        public int HengerekSzama()
        {
            int counter = 0;

            foreach (Hasab item in hasabok)
            {
                if (item is Henger)
                {
                    counter++;
                }
            }
            return counter;
        }



    }
}
