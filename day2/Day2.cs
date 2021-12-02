using System;
using System.Linq;
using System.Collections.Generic;

public class Program {
    public static int Main(string[] args) {
        List<string> lines = System.IO.File.ReadLines("day2.input").ToList();
        List<(string,int)> commands = (from string line in lines
            select (line.Split(" ")[0],int.Parse(line.Split(" ")[1]))).ToList();
    
        int depth = 0;
        int horizontal = 0;
        int aim = 0;
        int depth_part_2 = 0;

        foreach((string direction, int dist) cmd in commands) {
            switch(cmd.direction) {
                case "forward":
                        horizontal += cmd.dist;
                        depth_part_2 += aim*cmd.dist;
                        break;
                case "up":
                        depth -= cmd.dist;
                        aim -= cmd.dist;
                        break;
                case "down":
                        depth += cmd.dist;
                        aim += cmd.dist;
                        break;
                default:
                        Console.WriteLine("Unknown direction '{0}' in command",cmd.direction);
                        break;
            };
        }

        Console.WriteLine("Silver: {0}",horizontal*depth);
        Console.WriteLine("Gold: {0}",horizontal*depth_part_2);

        return 0;
    }
}
