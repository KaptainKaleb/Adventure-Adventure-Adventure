using System;
using System.IO;
using AAA.Chp0;

namespace AAA
{
    class Program
    {
        static void Main(string[] args)
        {
            if (Intro.Check() == true)
                Intro.Read();
            else Intro.New(Dialog.GetUser(), Dialog.GetClass());
        }
    }
}