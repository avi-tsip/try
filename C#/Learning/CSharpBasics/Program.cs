using System;

namespace CSharpBasics
{
    public class LessonOne
    {
        public static void Main(string[] args)
        {
            float result = 0;
            float numberOne = 0;
            float numberTwo = 0;

            Console.WriteLine("Enter your first number: ");
            string firstNumber = Console.ReadLine();

            Console.WriteLine("Enter your second number: ");
            string secondNumber = Console.ReadLine();

            try
            {
                numberOne = float.Parse(firstNumber);
                numberTwo = float.Parse(secondNumber);
            }
            catch (OverflowException)
            {
                Console.WriteLine("The number is too long!");
            }
            catch (FormatException)
            {
                Console.WriteLine("Please enter a number!");
            }
            catch (ArgumentNullException)
            {
                Console.WriteLine("The entry was empty, please add a valid number");
            }
            catch (Exception)
            {
                Console.WriteLine("General error occured");
            }

            try
            {
                result = numberOne / numberTwo;
            }
            catch (DivideByZeroException)
            {
                Console.WriteLine("Dividign by zero is not allowed");
            }
            finally
            {
                Console.WriteLine("The result is: " + result);
            }
        }
    }
}
