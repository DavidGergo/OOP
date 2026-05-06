using System.Collections;
using System;

namespace Filekezeles
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string fajlNev = "pelda.txt";

            // 1. Stream típusú objektum létrehozása (FileStream)
            using (FileStream fsIr = new FileStream(fajlNev, FileMode.Create, FileAccess.Write))
            {
                // 2. Fájl adatfolyamot író létrehozása a Stream objektumból (StreamWriter)
                using (StreamWriter sw = new StreamWriter(fsIr))
                {
                    // 3. Fájlkezelő műveletek megadása (írás)
                    sw.WriteLine("Első sor");
                    sw.WriteLine("Második sor");
                } // 4. StreamWriter lezárása (using miatt automatikus)
            }     // FileStream lezárása (using miatt automatikus)

            // 1. Stream típusú objektum létrehozása olvasáshoz
            using (FileStream fsOlvas = new FileStream(fajlNev, FileMode.Open, FileAccess.Read))
            {
                // 2. Fájl adatfolyamot olvasó létrehozása (StreamReader)
                using (StreamReader sr = new StreamReader(fsOlvas))
                {
                    // 3. Fájlkezelő műveletek megadása (olvasás)
                    string sor;
                    while ((sor = sr.ReadLine()) != null)
                    {
                        Console.WriteLine(sor);
                    }
                } // 4. StreamReader lezárása
            }     // FileStream lezárása

            Console.WriteLine("Kész, nyomj egy gombot...");
            Console.ReadKey();



        }
    }
}
