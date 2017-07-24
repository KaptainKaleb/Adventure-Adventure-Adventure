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
            string[] saveInfo = new string[21]; //8 items, 2 names, 2 classes, 6 levels, 1 date, 2 progress
            using (FileStream fs = new FileStream("savegame.txt", FileMode.Open))
            {
                using (StreamReader sr = new StreamReader(fs))
                {
                    for (int i = 0; i < 21; i++)
                        saveInfo[i] = sr.ReadLine();
                }
            }
            return saveInfo;
        }

        public static void New(string username, int clss)
        {
            
        }

    }
}
