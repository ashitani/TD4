
module TD4(clk,rst, io_in, io_out);

input clk,rst;
input  [3:0] io_in;
output [3:0] io_out;
wire [3:0] adr;
wire [7:0] dat;

reg [3:0] io_out;

TD4_core CORE(
    clk,
    rst,
    io_in,
    io_out,
    adr,
    dat);

TD4_ROM ROM(adr,dat);

endmodule
