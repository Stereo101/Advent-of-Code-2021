from advent import *

aoc = Session(2021,16)

with aoc.fp() as f:
    hexi = f.read().strip()

def hex_conv(hexi):
    d = {   "0":"0000",
            "1":"0001",
            "2":"0010",
            "3":"0011",
            "4":"0100",
            "5":"0101",
            "6":"0110",
            "7":"0111",
            "8":"1000",
            "9":"1001",
            "A":"1010",
            "B":"1011",
            "C":"1100",
            "D":"1101",
            "E":"1110",
            "F":"1111"}
    return "".join(d[c] for c in hexi.strip())

class Packet:
    def __init__(self,bin_s,offset=0):
        i = offset
        print("Reading packet starting from offset=",i)
        self.subpackets = []

        header = bin_s[i:i+3]
        i += 3
        
        self.header = int(header,2)
        
        type_id = bin_s[i:i+3]
        i += 3

        self.type_id = int(type_id,2)

        if self.type_id != 4:
            #operator packet
            type_len = int(bin_s[i:i+1],2)
            i += 1
            print(i)

            if type_len == 0:
                len_in_bits = int(bin_s[i:i+15],2)
                i += 15
                end = i+len_in_bits
                print("Reading until",end,"total of",len_in_bits,"bits")
                while i < end:
                    p = Packet(bin_s,offset=i)
                    i = p.offset
                    self.subpackets.append(p)
                    print("seq: read packet ending at",i)
            else:
                number_subpackets = int(bin_s[i:i+11],2)
                i += 11
                print("Reading",number_subpackets,"subpackets")
                for k in range(number_subpackets):
                    p = Packet(bin_s,offset=i)
                    i = p.offset
                    self.subpackets.append(p)
                    print("count: read packet ending at",i)
            #calc literal value
            if self.type_id == 0:
                self.value = sum(p.value for p in self.subpackets)
            elif self.type_id == 1:
                v = 1
                for p in self.subpackets:
                    v *= p.value
                self.value = v
            elif self.type_id == 2:
                m = float("INF")
                for p in self.subpackets:
                    m = min(m,p.value)
                self.value = m
            elif self.type_id == 3:
                m = float("-INF")
                for p in self.subpackets:
                    m = max(m,p.value)
                self.value = m
                
            elif self.type_id == 5:
                p1,p2 = self.subpackets
                if p1.value > p2.value:
                    self.value = 1
                else:
                    self.value = 0
            elif self.type_id == 6:
                p1,p2 = self.subpackets
                if p1.value < p2.value:
                    self.value = 1
                else:
                    self.value = 0
            elif self.type_id == 7:
                p1,p2 = self.subpackets
                if p1.value == p2.value:
                    self.value = 1
                else:
                    self.value = 0
        else:
            groups = []
            while True:
                e = bin_s[i:i+5]
                i += 5
                groups.append(int(e[1:],2))
                if e[0] == "0":
                    break

            v = 0 
            for g in groups:
                v <<= 4
                v += g
            self.value = v
        self.offset = i

    def version_sum(self):
        v = 0
        for p in self.subpackets:
            v += p.version_sum()
        return v + self.header

packet = []
bin_s = hex_conv(hexi)
p = Packet(bin_s)

silver = p.version_sum()
gold = p.value

aoc.solution(1,silver)
aoc.solution(2,gold)
