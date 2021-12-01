using System;

public class Globals {
    public static string input_file {get;} = "day1.input";
}

public class Program {
        public static int Main(string[] args) {
            string[] lines = System.IO.File.ReadAllLines(Globals.input_file);
            int[] sonar = new int[lines.Length];

            for(int i = 0; i < lines.Length; i++) {
                Console.WriteLine(lines[i]);
                sonar[i] = int.Parse(lines[i]);
            }

            int silver = 0;
            int gold = 0;

            int last = sonar[0];
            int window = sonar[0];
            int window_size = 1;
            int last_window = int.MaxValue;
    
            for(int i = 1; i < sonar.Length; i++) {
                window += sonar[i];
                if(window_size == 3) {
                    window -= sonar[i-3];
                    gold += window > last_window ? 1 : 0;
                    last_window = window;
                } else {
                    window_size += 1;
                }

                silver += sonar[i] > last ? 1 : 0;
                last = sonar[i]; 
            }

            Console.WriteLine("Silver {0}",silver);
            Console.WriteLine("Gold {0}",gold);
            return 0;
        }
}
