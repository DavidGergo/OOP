using Testek;
using Testek.Hasabok;
using Testek.Henger;

namespace HasabProba
{
    internal class Futatható
    {
        static void Main(string[] args)
        {
            //Testek.Hasabok.Henger henger = new Testek.Hasabok.Henger(1,2);
            Henger henger = new Henger(1, 2);
            Console.WriteLine(henger);

            Teglatest teglatest = new Teglatest(1, 2, 3);
            Console.WriteLine(teglatest);
            Console.WriteLine(teglatest.TerfogatNagyobbMint(henger));
            Console.WriteLine(henger.TerfogatNagyobbMint(teglatest));

            HasabTomb hasabok = new HasabTomb(5);

            hasabok.HasabHozzaad(1, new Henger(1, 2));
            hasabok.HasabHozzaad(1, new Henger(3, 4));
            hasabok.HasabHozzaad(1, new Teglatest(4, 5, 6));

            Console.WriteLine(hasabok.GetHasab(1));
            Console.WriteLine(hasabok.NemNullErtekuTombelem());
            Console.WriteLine(hasabok.HasabokAtlagTerfogata());
        }
    }
}
