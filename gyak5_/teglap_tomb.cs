using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace gyak5_1
{
    internal class teglap_tomb
    {
        private Teglalap[] t_lapok;

        private int meret;

        public int Size
        {
            get { return t_lapok.Length; }
        }

        public Teglalap GetTeglalap(int ind)
        {
            return t_lapok[ind];
        }

        public teglap_tomb(int meret)
        {
            t_lapok = new Teglalap[meret];
            Random rnd = new Random();

            for (int i = 0; i < t_lapok.Length; i++)
            {
                t_lapok[i] = new Teglalap(rnd.Next(2, 21), rnd.Next(2,21));
            }
        }

        public void List_arr()
        {
            Console.WriteLine("Tlapok Listázása: ");
            for (int i = 0; i < t_lapok.Length; i++)
            {
                Console.WriteLine($"\t{i+1}. elem: {t_lapok[i]}");
            }
        }

        public Teglalap Min_ter()
        {
            int min_ind = 0;
            for (int i = 1; i < t_lapok.Length; i++)
            {
                if (t_lapok[min_ind].Terulet_nagyobb_mint(t_lapok[i]))
                {
                    min_ind = i;
                }
            }

            return t_lapok[min_ind];
        }

        public override string ToString()
        {
            return "Tlapok száma: " + t_lapok.Length;
        }
    }
}
