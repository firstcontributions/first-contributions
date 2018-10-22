`timescale 1ns/1ns
module mealy(y, a, b, rst, clk);
output reg[1:0] y;
input wire a;
input wire b;
input wire clk;
input wire rst;
reg[1:0] s;
reg[1:0] n;
always @(a,b,s) begin
	y[0] <= (~a & b) | (s[1] & s[0]) | (s[1] & b);
	y[1] <= (~s[1] & a) | (~s[0] & ~b & a);
	n[1] <= (~s[1] & a) | (~s[0] & ~b & a);
	n[0] <= (~s[0] & b) | (s[1] & s[0]) | (s[1] & b);
	
end
always @(posedge clk) begin
	if(rst == 1)
	s <= 2'b00;
	else
	s <= n;
end
endmodule

 


