using Termekek.Elelmiszerek;

namespace Termekek.futtathato

{
    class AruProba
    {
        static void Main(string[] args)
        {
            Aru aru = new Aru("Aru", 20, 25);
            //Elelmiszerek.Kenyer kenyer = new Elelmiszerek.Kenyer("kenyer", 11, 15, 3);
            Kenyer kenyer = new Kenyer("kenyer", 11, 15, 3);

            Console.WriteLine("Áru: " + aru);
            Console.WriteLine("Kenyér: " + kenyer);
            Console.WriteLine();

            int melyikDragabb = aru.DragabbE(kenyer, 2500);
            if (melyikDragabb > 0)
            {
                Console.WriteLine("Áru drágább\n" + kenyer);
            }
            else if (melyikDragabb == 0)
            {
                Console.WriteLine("stb");
            }

            Console.WriteLine();

            Aru aru2 = new Aru("aru2", 1, 1);
            Console.WriteLine(aru2);

            Kenyer kenyer2 = new Kenyer("kenyer2", 3, 3, 2);

            if (Kenyer.ElsoNagyobbEgysegar((Kenyer)aru2, kenyer2))
            {
                Console.WriteLine(aru2);
            }
            else Console.WriteLine(kenyer2);

            Console.ReadKey();
        }
    }
}
