using System;
using System.Linq;
using System.Collections.Generic;


public class Program {
    public static int Main(string[] args) {
        List<ulong> lines = (from string s in System.IO.File.ReadLines("day3.input")
            select Convert.ToUInt64(s,2)).ToList();
       
        ulong bitwidth = Program.get_bitwidth(lines);
        Console.WriteLine("Bitwidth is {0}",bitwidth);

        ulong mask = 1;
        ulong silver = 0;
        foreach(int i in Enumerable.Range(0,(int)bitwidth)) {
            silver += Program.mcb(lines,mask);
            mask <<= 1;
        }
        ulong silver_comp = 1;
        silver_comp = silver_comp << (int)bitwidth;
        silver_comp -= 1;
        silver *= silver_comp ^ silver;
        Console.WriteLine("Silver {0}",silver);

        ulong gold = Program.filter_mcb(lines,bitwidth);
        Console.WriteLine("Gold {0}",gold);
        return 0;
    }

    private static ulong mcb(List<ulong> arr,ulong mask,bool lcb = false) {
        ulong sum = 0;
        foreach (ulong e in arr) {
            if((e&mask) == mask) {
                sum += 1;
            }
        }
        return (sum >= (ulong)(arr.Count()/2))^lcb ? mask : 0;
    }

    private static int partition(List<ulong> arr,int start,int end,ulong mask) {
        int left_p = start;
        int right_p = end; 
        while(left_p < right_p) {
            while(((arr[left_p]&mask) == 0) && (left_p < right_p)) {
                left_p += 1;
            }
            while(((arr[right_p]&mask) != 0) && (left_p < right_p)) {
                right_p -= 1;
            } 

            if(left_p < right_p) {
                ulong temp = arr[left_p];        
                arr[left_p] = arr[right_p];
                arr[right_p] = temp;
            }
        }

        //Adjust left_p back onto the last 0-element
        if(left_p != start && (arr[left_p]&mask) != 0) {
            left_p -= 1;
        }
        
        return left_p;
    }
    private static ulong filter_mcb(List<ulong> arr,ulong bitwidth) {
        ulong mask = 1UL << (int)(bitwidth-1);

        int start = 0;
        int end = arr.Count() - 1;
        int first_part = Program.partition(arr,start,end,mask);
        int part = first_part;

        while(start != end) {
            if(part > (end+start)/2) {
                start = part+1;
            } else {
                end = part;
            }
            mask >>= 1;
            part = Program.partition(arr,start,end,mask);
        }
        ulong p1 = arr[end];

        part = first_part;
        start = 0;
        end = arr.Count()-1;
        mask = 1UL << (int)(bitwidth-1);
        while(start != end) {
            if(part > (end+start)/2) {
                end = part; 
            } else {
                start = part+1;
            }
            mask >>= 1; 
            part = Program.partition(arr,start,end,mask);
        }
        return arr[end] * p1;
    }

    private static ulong get_bitwidth(List<ulong> arr) {
        ulong m = 0;
        foreach (ulong e in arr) {
            m = e > m ? e : m;
        }
        ulong count = 0;
        ulong mask = 1;
        while(mask<m){
            mask <<= 1;
            count += 1;
        }
        return count;
    }
}
