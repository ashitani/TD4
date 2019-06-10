`timescale 1ns/1ps
module test_TD4;

reg clk,rst;
reg  [3:0] io_in;
wire [3:0] io_out;

TD4 TD4(clk,rst,io_in,io_out);

initial begin
    $dumpfile("test_TD4.vcd");
    $dumpvars(0,test_TD4);

    clk=0; rst=1; io_in=0;
#10 rst=0;
#20 rst=1;
#1000 io_in=1; // for io.asm
#5000 $finish;
end

always #10
    clk <= ~clk;

endmodule

