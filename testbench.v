`timescale 1ns/1ns
module testbench();
wire [1:0] y;
reg a;
reg b;
reg clk;
initial clk = 1;
initial a = 0;
initial b = 0;
always #10 clk = ~clk;
reg rst;
initial rst = 1;
mealy mymachine(y, a, b, rst, clk);
initial begin
$dumpfile("TimingDiagram.vcd");
$dumpvars(0, y, a, b, rst, clk);
#20
rst = 0;
a = 0;
b = 0;
#20
a = 0;
b = 1;
#20
a = 0;
b = 0;
#20
a = 1;
b = 0;
#20
a = 1;
b = 1;
#20



$finish;
end
endmodule 	
