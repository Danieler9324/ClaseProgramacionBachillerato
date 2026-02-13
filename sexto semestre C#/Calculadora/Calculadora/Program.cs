using System;
class Program
{
    static void Main(string[] args)
    {
        bool seguir;
        double num;
        double resultado = 0;
        char operador;
        string opInput;
        // Solicitar al usuario que ingrese dos números
        Console.Write("Ingrese el primer numero: ");
        while (!double.TryParse(Console.ReadLine(), out resultado))
        {
            Console.Write("Entrada inválida. Ingrese el primer numero nuevamente: ");
        }
        do
        {
            Console.Write("Ingrese el segundo numero: ");
            while (!double.TryParse(Console.ReadLine(), out num))
            {
                Console.Write("Entrada inválida. Ingrese el segundo numero nuevamente: ");
            }
            // Solicitar operador
            do
            {
                Console.Write("Ingrese el operador (+, -, *, /): ");
                opInput = Console.ReadLine();

                if (string.IsNullOrWhiteSpace(opInput) || opInput.Length != 1 || opInput[0] != '+' && opInput[0] != '-' && opInput[0] != '*' && opInput[0] != '/')
                {
                    Console.WriteLine("Operador invalido, vuelve a ingresar el operador");
                }

            }
            while (string.IsNullOrWhiteSpace(opInput) || opInput.Length != 1 || (opInput[0] != '+' && opInput[0] != '-' && opInput[0] != '*' && opInput[0] != '/'));

            operador = opInput[0];

            // Realizar la operación según el operador ingresado
            switch (operador)
            {
                case '+':
                    resultado += num;
                    break;
                case '-':
                    resultado -= num;
                    break;
                case '*':
                    resultado *= num;
                    break;
                case '/':
                    // Verificar si el divisor es 0
                    while (num == 0)
                    {
                        Console.WriteLine("Para division el segundo numero no puede ser 0");

                        Console.Write("Ingrese el segundo numero nuevamente: ");
                        while (!double.TryParse(Console.ReadLine(), out num))
                        {
                            Console.Write("Entrada invalida. Intente nuevamente: ");
                        }
                    }

                    resultado /= num;
                    break;
                default:
                    Console.Error.WriteLine("Error: Operador no válido.");
                    return;
            }

            Console.WriteLine($"Resultado: {resultado}");

            Console.WriteLine("Quieres continuar? ( S / N ) ");
            char opcion = Char.ToUpper(Console.ReadKey().KeyChar);
            Console.ReadLine();

            seguir = opcion == 'S';

            Console.WriteLine();

        } while (seguir);
        Console.WriteLine("Presiona cualquier tecla para salir");
        Console.ReadLine();
    }
}