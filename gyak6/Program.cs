using AlkalmazottNevter;

namespace FuttathatóNevter
{
    internal class Futtathato
    {
        static void Main(string[] args)
        {
            Console.WriteLine("NYugdíjazas");

            Alkalmazott alkalmazott = new Alkalmazott();

            int evek_nyugdijig = alkalmazott.EvekNyugdijig();
            Console.WriteLine("Évek nyugdíjig: " + evek_nyugdijig + "\n\n");

            int alkalmazottak_szama = 5;

            Alkalmazott[] alkalmazottak = new Alkalmazott[alkalmazottak_szama];

            Random rnd = new Random();
            Console.WriteLine("Új alkalmazottak:");
            for (int i = 0; i < alkalmazottak.Length; i++)
            {
                alkalmazottak[i] = new Alkalmazott("XY" + (i + 1), rnd.Next(25, Alkalmazott.Nyugdij_korhatar));
                Console.WriteLine("\t" + alkalmazottak[i]);
            }

            Alkalmazott.SetNyugdijkorhatar(70);
            Alkalmazott.Nyugdij_korhatar = 70;

            Console.WriteLine("\nÚj nyugdíjkorhatárral: ");
            AlkalmazottKiir(alkalmazottak);

            Console.WriteLine("\nAkiknek < 5 -nél kevesebb idő nyugdíjig.");
            otevnelkevesebbnyugdijig(alkalmazottak);

            RendezesNYEvekAlapjan(alkalmazottak);

        }

        private static void RendezesNYEvekAlapjan(Alkalmazott[] alkalmazottak)
        {
            for (int i = 0; i < alkalmazottak.Length - 1; i++)
            {
                int minIND = i;
                for (int j = i + 1; j < alkalmazottak.Length; j++)
                {
                    if (alkalmazottak[j].EvekNyugdijig() < alkalmazottak[minIND].EvekNyugdijig())
                    {
                        minIND = j;
                    }
                }

                if (minIND != i)
                {
                    Alkalmazott temp = alkalmazottak[i];
                    alkalmazottak[i] = alkalmazottak[minIND];
                    alkalmazottak[minIND] = temp;
                }
            }

            Console.WriteLine("\nRendezett alkalmazottak (évek nyugdíjig növekvő):");
            AlkalmazottKiir(alkalmazottak);
        }

        private static void otevnelkevesebbnyugdijig(Alkalmazott[] alkalmazottak)
        {
            int c = 0;
            for (int i = 0; i < alkalmazottak.Length; i++)
            {
                if (alkalmazottak[i].EvekNyugdijig() < 15)
                {
                    c++;
                    Console.WriteLine("\t" + alkalmazottak[i]);
                }
            }

            if (c == 0)
            {
                Console.WriteLine("\tNincs olyan akinek ilyen kevés ideje van nyugdijig.");
            }
        }

        private static void AlkalmazottKiir(Alkalmazott[] alkalmazottak)
        {
            for (int i = 0; i < alkalmazottak.Length; i++)
            {
                Console.WriteLine("\t" + alkalmazottak[i]);
            }
        }
    
        
    }
}
