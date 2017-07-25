using System;
using System.Collections.Generic;
using System.Text;

namespace AAA
{
    namespace Chp0
    {
        class Dialog
        {
            public static string GetUser()
            {
                Console.Clear();
                Console.WriteLine("Welcome to AAA");
                Console.WriteLine("Please enter your username: ");
                string user = Console.ReadLine();
                return user;
            }

            public static int GetClass()
            {
                Console.Clear();
                Console.WriteLine(
                    "There are 4 main classes in AAA.\n" +
                    "Knight  Thief  Rogue  Mage\n" +
                    "Please choose one.");
                string mainClass = Console.ReadLine();
                if (mainClass.StartsWith("k|K"))
                    return 0;
                else if (mainClass.StartsWith("t|T"))
                    return 1;
                else if (mainClass.StartsWith("r|R"))
                    return 2;
                else if (mainClass.StartsWith("m|M"))
                    return 3;
                else return 4;
            }
        }
    }

    namespace Chp1
    {
        class Dialog
        {
            public static void Part1()
            {

            }
        }
    }
}
