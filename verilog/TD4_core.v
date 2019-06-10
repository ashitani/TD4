`include "74161.v"
`include "74153.v"
`include "74283.v"
`include "7474.v"

module TD4_core(
    clk,
    rst,
    io_in,
    io_out,
    adr,
    dat
    );

input clk,rst;
input [3:0] io_in;
output [3:0] io_out;
output [3:0] adr;
input  [7:0] dat;

wire [3:0] d;
wire [3:0] q2,q3,q4,q5;
wire       l2,l3,l4,l5;

ttl_74161 IC2(
  .Clear_bar(rst),
  .Load_bar(l2),
  .ENT(1'b0),
  .ENP(1'b0),
  .D(d),
  .Clk(clk),
  .RCO(),
  .Q(q2)
);

ttl_74161 IC3(
  .Clear_bar(rst),
  .Load_bar(l3),
  .ENT(1'b0),
  .ENP(1'b0),
  .D(d),
  .Clk(clk),
  .RCO(),
  .Q(q3)
);

ttl_74161 IC4(
  .Clear_bar(rst),
  .Load_bar(l4),
  .ENT(1'b0),
  .ENP(1'b0),
  .D(d),
  .Clk(clk),
  .RCO(),
  .Q(q4)
);

ttl_74161 IC5(
  .Clear_bar(rst),
  .Load_bar(l5),
  .ENT(1'b1),
  .ENP(1'b1),
  .D(d),
  .Clk(clk),
  .RCO(),
  .Q(q5)
);

wire [1:0] s67;   // select
wire [7:0] a6,a7; // 4bit data x2
wire [1:0] y6,y7; // 2bit output

ttl_74153 IC6(
  .Enable_bar(2'b00),
  .Select(s67),
  .A_2D(a6),
  .Y(y6)
    );

ttl_74153 IC7(
  .Enable_bar(2'b00),
  .Select(s67),
  .A_2D(a7),
  .Y(y7)
    );

wire [3:0] a9;
wire [3:0] b9;
wire carry9;

ttl_74283 IC9(
  .A(a9),
  .B(b9),
  .C_in(1'b0),
  .Sum(d),
  .C_out(carry9)
    );

wire [1:0] q_1;

ttl_7474 IC1(
  .Preset_bar(2'b01),
  .Clear_bar({1'b0,rst}),
  .D({1'b0,carry9}),
  .Clk({1'b0,clk}),
  .Q(),
  .Q_bar(q_1)
  );



// 153 inputs

assign a6={
    1'b0,
    io_in[1],
    q3[1],
    q2[1],
    1'b0,
    io_in[0],
    q3[0],
    q2[0]
};


assign a7={
    1'b0,
    io_in[3],
    q3[3],
    q2[3],
    1'b0,
    io_in[2],
    q3[2],
    q2[2]
};

assign s67 ={
    dat[5],
    (dat[4] | dat[7])
    };

// 285 inputs

assign a9={
    y7[1:0],
    y6[1:0]
};

assign b9=dat[3:0];

// logics

assign l2=  dat[6] | dat[7];
assign l3= ~dat[6] | dat[7];
assign l4=  ~(~dat[6] & dat[7]);
assign l5=  ~(dat[6]&dat[7]& (q_1|dat[4]));


// I/O's
assign io_out=q4;

// ROM
assign adr=q5;

endmodule
