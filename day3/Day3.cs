using System;
using System.Linq;
using System.Collections.Generic;


public class Program {
    public static int Main(string[] args) {
        List<ulong> lines = (from string s in System.IO.File.ReadLines("bigboy.txt")
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
        ulong gold = Program.filter_mcb(lines,bitwidth) * Program.filter_mcb(lines,bitwidth,lcb:true);
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

    private static ulong filter_mcb(List<ulong> arr,ulong bitwidth,bool lcb = false) {
        ulong mask = 1;
        mask <<= (int)(bitwidth-1);
        ulong bit; 
        while(arr.Count() > 1) {
            bit = mcb(arr,mask,lcb:lcb); 
            arr = (from ulong e in arr
                where (e&mask) == bit
                select e).ToList();
            mask /= 2;
        }
        return arr[0];
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


/*
def mcb(arr,mask,lcb=False):
    return mask if (sum(e&mask==mask for e in arr) >= len(arr)/2)^lcb else 0

def filter_mcb(arr,bitwidth,lcb=False):
    mask = 1 << (bitwidth-1) 
    while len(arr) > 1:
        bit = mcb(arr,mask,lcb)
        arr = [e for e in arr if (e&mask) == bit]
        mask >>= 1
    return arr[0]

def get_bitwidth(arr):
    m = max(arr)
    mask,result = 1,0
    while mask < m:
        mask <<= 1
        result += 1
    return result

prlong(len(lines),"loaded")
bitwidth = get_bitwidth(lines)
silver = sum(mcb(lines,1 << i) for i in range(bitwidth))
silver *= ((1 << (bitwidth))-1) ^ silver
gold = filter_mcb(lines,bitwidth) * filter_mcb(lines,bitwidth,lcb=True)
prlong(silver,gold)

*/
