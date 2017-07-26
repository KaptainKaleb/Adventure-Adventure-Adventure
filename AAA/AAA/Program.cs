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
        public int[]  Wpns { get; set; }
        public int[]  Item { get; set; }
        public int[]  Spll { get; set; }
        public int[]  Levl { get; set; }
        public int    Prgs { get; set; }
        public int    Htpt { get; set; }
        public int    Gold { get; set; }
        public User(string name, int clss)
        {
            Name = name;
            Clss = clss;
            switch (clss)
            {
                case 0:             // Knight
                    Wpns[0] = 01;   // Steel Shortsword
                    Wpns[1] = 11;   // Leather Shield (offhand)
                    Item[0] = 01;   // Minor Healing
                    Item[1] = 01;   // Minor Healing
                    Item[2] = 21;   // Flint & Steel
                    Levl[0] = 01;   // Main Level
                    Levl[1] = 03;   // Combat Level
                    Levl[2] = 02;   // Speech Level
                    Levl[3] = 01;   // Crafting Level
                    Levl[4] = 02;   // Agility Level
                    Prgs = 01;      // Progress XY (X = Chapter, Y = Section)
                    Htpt = 18;      // Base: 15 Armor: 3
                    Gold = 50;      // Base Gold
                    break;
                case 1:             // Thief
                    Wpns[0] = 03;   // Steel Dagger
                    Wpns[1] = 03;   // Steel Dagger (offhand)
                    Item[0] = 01;   // Minor Healing
                    Item[1] = 22;   // Lockpicks
                    Spll[0] = 31;   // Minor speechcraft (persuade)
                    Levl[0] = 01;   // Main Level
                    Levl[1] = 02;   // Combat Level
                    Levl[2] = 03;   // Speech Level
                    Levl[3] = 01;   // Crafting Level
                    Levl[4] = 02;   // Agility Level
                    Prgs = 01;      // Progress XY (X = Chapter, Y = Section)
                    Htpt = 16;      // Base: 15 Armor: 1
                    Gold = 60;      // Base Gold
                    break;
                case 2:             // Rogue
                    Wpns[0] = 01;   // Steel Shortsword
                    Wpns[1] = 11;   // Leather Shield (offhand)
                    Item[0] = 01;   // Minor Healing
                    Item[1] = 01;   // Minor Healing
                    Item[2] = 21;   // Flint & Steel
                    Levl[0] = 01;   // Main Level
                    Levl[1] = 03;   // Combat Level
                    Levl[2] = 02;   // Speech Level
                    Levl[3] = 01;   // Crafting Level
                    Levl[4] = 02;   // Agility Level
                    Prgs = 01;      // Progress XY (X = Chapter, Y = Section)
                    Htpt = 18;      // Base: 15 Armor: 3
                    Gold = 50;      // Base Gold
                    break;
                case 3:             // Mage
                    Wpns[0] = 03;   // Steel Dagger
                    Wpns[1] = 03;   // Steel Dagger (offhand)
                    Item[0] = 01;   // Minor Healing
                    Item[1] = 02;   // Minor Mana
                    Item[2] = 22;   // Lockpicks
                    Levl[0] = 01;   // Main Level
                    Levl[1] = 02;   // Combat Level
                    Levl[2] = 03;   // Speech Level
                    Levl[3] = 01;   // Crafting Level
                    Levl[4] = 02;   // Agility Level
                    Prgs = 01;      // Progress XY (X = Chapter, Y = Section)
                    Htpt = 16;      // Base: 15 Armor: 1
                    Gold = 60;      // Base Gold
                    break;

            }
        }
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