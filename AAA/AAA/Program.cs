using System;
using System.IO;
using AAA.Chp0;
using AAA.Chp1;

namespace AAA
{
    public class User
    {
        public string Name { get; set; }
        public int    Clss { get; set; }
        public int    Wpn1 { get; set; }
        public int    Wpn2 { get; set; }
        public int[]  Item { get; set; }
        public int[]  Spll { get; set; }
        public int[]  Levl { get; set; }
        public string Prgs { get; set; }
        public int    Htpt { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            if (Intro.Check() == true)
                Intro.Read();
            else Intro.New(Chp0.Dialog.GetUser(), Chp0.Dialog.GetClass());
        }
    }
}