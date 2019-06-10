module TD4_ROM(adr,dat);

input [3:0] adr;
output [7:0] dat;

reg [7:0] dat;
reg [7:0] mem [0:15]; // address 4bit data 8bit

initial begin
    $readmemh("rom.txt",mem,4'd0,4'd15);
end
//always @(adr) begin
//    dat <= mem[adr];
//end
assign    dat = mem[adr];

endmodule