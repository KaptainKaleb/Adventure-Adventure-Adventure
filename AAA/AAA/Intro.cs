using System;
using System.IO;

namespace AAA
{
    class Intro
    {
        public static bool Check()
        {
            if (File.Exists("savegame.txt"))
                return true;
            else return false;
        }
        
        public static string[] Read()
        {
            string[] saveInfo = new string[20]; // 1 name, 1 class, 2 weapons, 6 items, 5 levels, 3 spells, 1 progress, 1 hitpoints
            using (FileStream fs = new FileStream("savegame.txt", FileMode.Open))
            {
                using (StreamReader sr = new StreamReader(fs))
                {
                    for (int i = 0; i < 20; i++)
                        saveInfo[i] = sr.ReadLine();
                }
            }
            return saveInfo;
        }

        public static void New(string username, int clss)
        {
            string[] saveS = {
                "name=",
                "clss=",
                "wpn1=",
                "wpn2=",
                "inv0=",
                "inv1=",
                "inv2=",
                "inv3=",
                "inv4=",
                "inv5=",
                "lvl0=",
                "lvl1=",
                "lvl2=",
                "lvl3=",
                "lvl4=",
                "spl0=",
                "spl1=",
                "spl2=",
                "pgrs=",
                "htpt="
            };

            using (FileStream fs = new FileStream("savegame.txt", FileMode.Create, FileAccess.Write))
            {
                using (StreamWriter sw = new StreamWriter(fs))
                {
                    sw.WriteLine("name=" + username);
                    sw.WriteLine("clss=" + clss);
                    for (int i = 2; i < 20; i++)
                        sw.WriteLine(saveS[i]);
                }
            }
        }
    }
}
