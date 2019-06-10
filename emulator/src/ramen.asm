        OUT 0b0111
LOOP1:  ADD A,1
        JNC LOOP1
LOOP2:  ADD A,1
        JNC LOOP2
        OUT 0b0110
LOOP3:  ADD A,1
        JNC LOOP3
LOOP4:  ADD A,1
        JNC LOOP4
LOOP5:  OUT 0b0000
        OUT 0b0100
        ADD A,1
        JNC LOOP5
        OUT 0b1000
HALT:   JMP HALT
