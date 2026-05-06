using _1_Bank;
using Bank;
namespace BankiAlkalmazas
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Bankszamla szamla = new Bankszamla("123456");
            Console.WriteLine($"Számla létrehozva: {szamla}");
            Console.WriteLine("\n");
            szamla.Penzbefizetes(1000);
            Console.WriteLine($"Befizetve! Új egyenleg: {szamla.Egyenleg}");
            Console.WriteLine("\n");
            try
            {
                szamla.Penzkivetel(500);
                Console.WriteLine("Sikeres pénzkivétel");
                Console.WriteLine($"Fizetve! Új egyenleg: {szamla.Egyenleg}");
            }
            catch (InsufficientFundsException ex)
            {
                Console.WriteLine($"Sikertelen Péznkivétel: {ex.Message}");
                throw;
            }
            Console.WriteLine("\n");

            try
            {
                szamla.Penzkivetel(1000);
                Console.WriteLine("Sikeres pénzkivétel");
                Console.WriteLine($"Fizetve! Új egyenleg: {szamla.Egyenleg}");
            }
            catch (InsufficientFundsException ex)
            {
                Console.WriteLine($"Sikertelen Péznkivétel: {ex.Message}");
                Console.ReadKey();
                throw;
            }

            
        }
    }
}
