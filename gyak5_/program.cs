using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Runtime.ExceptionServices;
using System.Text;
using System.Threading.Tasks;
using gyak5_1



namespace Futtatas
{
    internal class program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(" \t  ## Teglalapok ##  ");

            //statikustipus obj_nev = new dinamikustipus();
            Teglalap a = new Teglalap(1 ,2);
            Teglalap b = new Teglalap(3);
            Teglalap c = a;

            Console.WriteLine("Méretek: ");
            Console.WriteLine(a);
            Console.WriteLine(b.ToString());
            Console.WriteLine(c);

            a.Set_sides(98, 76);
            Console.WriteLine("\n" + a);

            a.Set_teglalap(3);
            Console.WriteLine("\n" + a);
            Console.WriteLine(b.ToString());
            Console.WriteLine(c);

            Console.WriteLine("\na == b -> " + (a==b));
            Console.WriteLine("a == c -> " + (a == c));
            Console.WriteLine("a.Oldalak_egyezik(b) -> " + a.Oldalak_egyezik(b));

            Console.WriteLine("###########");

            teglap_tomb t_lapok = new teglap_tomb(5);

            t_lapok.List_arr();

            //int nagyobb_teruletuek = teglalap_count(t_lapok, a);
            
            int t_lap_ind_old_eq = ElsoOldalakEQ(t_lapok,a);
           // Console.WriteLine(t_lapok.GetTeglalap(t_lap_ind_old_eq));
            if (t_lap_ind_old_eq < )
            {
                Console.WriteLine("Nincs megegyező TL");
            }
            else Console.WriteLine(t_lapok.GetTeglalap(t_lap_ind_old_eq));
        }

        private static int ElsoOldalakEQ(teglap_tomb t_lapok, Teglalap a)
        {
            int ind = -1;
            for (int i = 0; i < t_lapok.Size; i++)
            {
                if (t_lapok.GetTeglalap(i).Oldalak_egyezik()
                {
                    Index = i; break;
                }
            }
        }

        /* private static int teglalap_count(teglap_tomb t_lapok, Teglalap a)
         {
             int tlaok_szama = 0;

             for (int i = 0; i < t_lapok.Size; i++)
             {
                 if (t_lapok.GetTeglalap(i).Terulet_nagyobb_mint()
                 {
                     tlaok_szama++;
                 }
             }
             return tlaok_szama;
         }*/

    }
}
