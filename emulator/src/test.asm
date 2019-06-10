        MOV A,7     ; 0x37
LOOP:   ADD A,1     ; 0x01
        JNC LOOP    ; 0xE1
        OUT 15      ; 0xBF
HALT:   JMP HALT    ; 0xF4
