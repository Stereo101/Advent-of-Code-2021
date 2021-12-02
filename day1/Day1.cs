using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

public class Globals {
    public static string input_file {get;} = "day1.input";
}

public class Program {
        public static int Main(string[] args) {
            List<string> lines = File.ReadLines(Globals.input_file).ToList();
            int[] sonar = new int[lines.Count];
            

            for(int i = 0; i < sonar.Length; i++) {
                sonar[i] = int.Parse(lines[i]);
                Console.WriteLine("{0}: {1}",i,sonar[i]);
            }
    
            int gold = 
                (from int i in Enumerable.Range(3,sonar.Length-3)
                where sonar[i] > sonar[i-3]
                select 1).Sum();
            Console.WriteLine("Gold {0}",gold);
            
            int silver =
                (from int i in Enumerable.Range(1,sonar.Length-1)
                where sonar[i] > sonar[i-1]
                select 1).Sum();
            Console.WriteLine("Silver {0}",silver);
            
            return 0;
        }
}
