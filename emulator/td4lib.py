#/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import re

import sdl2
import sdl2.ext

class TD4:

    def __init__(self):
        self.a=0
        self.b=0
        self.c=0
        self.pc=0

        self.inp=0
        self.out=0

        self.clock=10 #[Hz]
        self.time=0

        self.rom=[0 for i in range(16)]

    def dump_reg(self):
        txt=""
        txt+="%05d:  " % self.time
        txt+= "A[%01X] " % self.a
        txt+= "B[%01X] " % self.b
        txt+= "C[%01X] " % self.c
        txt+= "PC[%01X] " % self.pc
        txt+= "INST[%02X] " % self.rom[self.pc_old]
        txt+= "   "
        txt+= "IN[%s] " % format(self.inp, '04b')
        txt+= "OUT[%s] " % format(self.out, '04b')
        print(txt)

    def MOV_A(self,im):
        self.a=im
        return self.pc+1

    def MOV_A(self,im):
        self.a=im
        return self.pc+1

    def MOV_B(self,im):
        self.b=im
        return self.pc+1

    def MOV_AB(self,im):
        self.a=self.b
        return self.pc+1

    def MOV_BA(self,im):
        self.b=self.a
        return self.pc+1

    def ADD_A(self,im):
        self.c = 0
        self.a += im
        if self.a&0xf0!=0:
            self.c=1
        self.a =  self.a & 0xF
        return self.pc+1

    def ADD_B(self,im):
        self.c = 0
        self.b += im
        if self.b&0xf0!=0:
            self.c=1
        self.b =  self.b & 0xF
        return self.pc+1

    def IN_A(self):
        self.a = self.inp
        return self.pc+1

    def IN_B(self):
        self.b = self.inp
        return self.pc+1

    def OUT_IM(self, im):
        self.out = im
        return self.pc+1

    def OUT_B(self):
        self.out = self.b
        return self.pc+1

    def JMP(self, im):
        return im

    def JNC(self, im):
        if self.c==0:
            return im
        return self.pc+1

    def exec_code(self, code):
        inst = (0xF0 & code)>>4
        im   = (0x0F & code)

        if inst == 3:
            r=self.MOV_A(im)
        elif inst == 7:
            r=self.MOV_B(im)
        elif inst == 1:
            r=self.MOV_AB()
        elif inst == 4:
            r=self.MOV_BA()
        elif inst == 0:
            r=self.ADD_A(im)
        elif inst == 5:
            r=self.ADD_B(im)
        elif inst == 2:
            r=self.IN_A()
        elif inst == 6:
            r=self.IN_B()
        elif inst == 0xb:
            r=self.OUT_IM(im)
        elif inst == 9:
            r=self.OUT_B()
        elif inst == 0xF:
            r=self.JMP(im)
        elif inst == 0xE:
            r=self.JNC(im)
        else:
            print("UNKNOWN INSTRUCTION!")
            r=0

        return r


    def run(self, start_pc=0, freq=10):
        self.clock=float(freq)
        self.pc=start_pc
        self.pc_old = self.pc
        sdl2.ext.init()

        while(True):

            instruction = self.rom[self.pc]
            self.pc = self.exec_code(instruction)
            self.pc &= 0xf
            self.dump_reg()
            if self.pc_old==self.pc:
                print("HALTED")
                exit(-1)
            self.pc_old=self.pc
            self.time+=1
            time.sleep( 2.0/self.clock) # 2clock per instruction

            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_KEYUP:
                    k = event.key.keysym.sym
                    if k>96 and k<103:
                        self.inp = k-87 # A-F
                    if k>47 and k<58:
                        self.inp = k-48 # 0-9

    def set_rom(self,rom):
        for i,x in enumerate(rom):
            self.rom[i]=x

    def load_asm(self, file):
        with open(file) as f:
            txt=f.read()
            self.assemble(txt)

    def preprocess(self,txt):
        ans=[]
        labels={}
        address=0
        # clean codes
        for l in txt.split("\n"):
            l = re.sub(r';.*',r'',l)  # clear comment
            label=re.match(r"^\S+:",l)
            label_txt=""
            if label!=None:
                l = l.replace(label[0],"")
                label_txt = label[0][:-1]
            l=re.sub(r'^\s+',"",l) # remove header spaces
            l=re.sub(r'\s+$',"",l) # remove footer spaces
            l=re.sub(r'\s+'," ",l) # replace spaces to monospace

            if label_txt!="":
                labels[label_txt] = "%d" % address
                l.replace(label_txt,"")
            if l!="":
                ans.append(l)
                if(address>15):
                    print("Asemble error: address exeeds 0xF!")
                    exit()
                address+=1
        return ans, labels

    def decode(self,txt,labels):
        rom=[]
        for l in txt:
            inst=0
            words=l.split(" ")
            inst_txt = words[0]

            sub = words[1].split(",")
            if len(sub)==2:
                dst,src = sub
            else:
                dst=sub[0]
                src=""

            keys=labels.keys()
            if dst in keys:
                dst=labels[dst]
            if src in keys:
                src=labels[src]

            if src=="":
                src=-1
            elif src!="A" and src!="B":
                src=eval(src) & 0xf

            if dst!="A" and dst!="B":
                dst=eval(dst)&0x0f

            if inst_txt=="MOV" and dst=="A":
                if src=="B":
                    inst = 0x10
                else:
                    inst=0x30 + src
            if inst_txt=="MOV" and dst=="B":
                if src=="A":
                    inst = 0x40
                else:
                    inst=0x70 + src

            if inst_txt=="ADD":
                if dst=="A":
                    inst = 0x00 + src
                elif dst=="B":
                    inst = 0x50 + src

            if inst_txt=="IN":
                if dst=="A":
                    inst = 0x20
                elif dst=="B":
                    inst = 0x60

            if inst_txt=="OUT":
                if dst=="B":
                    inst = 0x90
                else:
                    inst = 0xB0 + dst
            if inst_txt=="JMP":
                inst = 0xF0 + dst
            if inst_txt=="JNC":
                inst = 0xE0 + dst

            rom.append(inst)
        self.set_rom(rom)

    def assemble(self, txt):
        rom=[]

        txt,labels=self.preprocess(txt)
        self.decode(txt,labels)
        self.set_rom(rom)

    def dump_rom(self):
        for i,l in enumerate(self.rom):
            bin_str = format(l, '08b')
            print("%01X: 0x%02X 0b%s" % (i,l,bin_str))


'''
## instruction list
MOV A.Im    0011 Im
MOV B,Im    0111 Im
MOV A,B     0001 0000
MOV B,A     0100 0000
ADD A,Im    0000 Im
ADD B,Im    0101 Im
IN A        0010 0000
IN B        0110 0000
OUT Im      1011 Im
OUT B       1001 0000
JMP Im      1111 Im
JNC Im      1110 Im
'''

if __name__ == '__main__':

    td4=TD4()
    td4.load_asm("test.asm")

    td4.run()


