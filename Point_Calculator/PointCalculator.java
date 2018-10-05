/* POINT CALCULATOR
   This calculator performs some operations on points.For eg., you can add two points, find the slope..
   
   While entering a point in calculator follow this format : (x,y)
   where x,y are integer values
*/
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class PointCalculator extends JFrame implements ActionListener {
	JTextField tfield;

	int z = 0,a = 0,b = 0,x = 0,y = 0 ;
	char ch;
	Point temp1 = new Point();
	Point temp2 = new Point();
	Point result = new Point();
	double scl; 
		
	JButton b1, b2, b3, b4, b5, b6, b7, b8, b9, zero, clr, plus, mul, eq, dot, addSub, 
			edist, mdist, slope, quad, xproj, yproj, xref, yref, obrac, cbrac, comma , equl;

	Container cont;

	JPanel textPanel, buttonpanel;

	PointCalculator() {
		cont = getContentPane();
		cont.setLayout(new BorderLayout());
		JPanel textpanel = new JPanel();
		tfield = new JTextField(35);
		tfield.setHorizontalAlignment(SwingConstants.RIGHT);
		tfield.addKeyListener(new KeyAdapter() {
			public void keyTyped(KeyEvent keyevent) {
				char k = keyevent.getKeyChar();
				if (k>='0'&&k<='9') {
				} else {
					keyevent.consume();
				}
			}
		});
		textpanel.add(tfield);
		buttonpanel = new JPanel();
		buttonpanel.setLayout(new GridLayout(8, 3, 3, 3));
		
		obrac = new JButton("(");
		buttonpanel.add(obrac);
		obrac.addActionListener(this);

		cbrac = new JButton(")");
		buttonpanel.add(cbrac);
		cbrac.addActionListener(this);
		
		b1 = new JButton("1");
		buttonpanel.add(b1);
		b1.addActionListener(this);
		
		b2 = new JButton("2");
		buttonpanel.add(b2);
		b2.addActionListener(this);
		
		b3 = new JButton("3");
		buttonpanel.add(b3);
		b3.addActionListener(this);

		b4 = new JButton("4");
		buttonpanel.add(b4);
		b4.addActionListener(this);
		
		b5 = new JButton("5");
		buttonpanel.add(b5);
		b5.addActionListener(this);
		
		b6 = new JButton("6");
		buttonpanel.add(b6);
		b6.addActionListener(this);

		b7 = new JButton("7");
		buttonpanel.add(b7);
		b7.addActionListener(this);
		
		b8 = new JButton("8");
		buttonpanel.add(b8);
		b8.addActionListener(this);
		
		b9 = new JButton("9");
		buttonpanel.add(b9);
		b9.addActionListener(this);

		zero = new JButton("0");
		buttonpanel.add(zero);
		zero.addActionListener(this);
		
		comma = new JButton(",");
		buttonpanel.add(comma);
		comma.addActionListener(this);
		
		dot = new JButton(".");
		buttonpanel.add(dot);
		dot.addActionListener(this);
		
		addSub = new JButton("-");
		buttonpanel.add(addSub);
		addSub.addActionListener(this);
		
		eq = new JButton("=");
		buttonpanel.add(eq);
		eq.addActionListener(this);

		quad =  new JButton("Quadrant");
		buttonpanel.add(quad);
		quad.addActionListener(this);
		
		plus = new JButton("Add");
		buttonpanel.add(plus);
		plus.addActionListener(this);

		mul = new JButton("Sca. Mul");
		buttonpanel.add(mul);
		mul.addActionListener(this);

				
		edist = new JButton("Eucl. Dist");
		buttonpanel.add(edist);
		edist.addActionListener(this);

		mdist = new JButton("Manh. Dist");
		buttonpanel.add(mdist);
		mdist.addActionListener(this);
		
		slope = new JButton("Slope");
		buttonpanel.add(slope);
		slope.addActionListener(this);
		
		xproj = new JButton("X Proj");
		buttonpanel.add(xproj);
		xproj.addActionListener(this);
		
		yproj =  new JButton("Y Proj");
		buttonpanel.add(yproj);
		yproj.addActionListener(this);
		
		xref = new JButton("X Refl");
		buttonpanel.add(xref);
		xref.addActionListener(this);
		
		yref =  new JButton("Y Refl");
		buttonpanel.add(yref);
		yref.addActionListener(this);
		
		equl =  new JButton("Equ. line");
		buttonpanel.add(equl);
		equl.addActionListener(this);
		
		clr = new JButton("AC");
		buttonpanel.add(clr);
		clr.addActionListener(this);
		
		cont.add("Center", buttonpanel);
		cont.add("North", textpanel);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	public void actionPerformed(ActionEvent e) {
		try {
		String s = e.getActionCommand();
		if (s.equals("1")) {
			
			if (z == 0) {
				tfield.setText(tfield.getText() + "1");
			} else {
				tfield.setText("");
				tfield.setText(tfield.getText() + "1");
				z = 0;
			}
		}
		if (s.equals("2")) {
			
			if (z == 0) {
				tfield.setText(tfield.getText() + "2");
			} else {
				tfield.setText("");
				tfield.setText(tfield.getText() + "2");
				z = 0;
			}
		}
		if (s.equals("3")) {
			
			if (z == 0) {
				tfield.setText(tfield.getText() + "3");
			} else {
				tfield.setText("");
				tfield.setText(tfield.getText() + "3");
				z = 0;
			}
		}
		if (s.equals("4")) {
			
			if (z == 0) {
				tfield.setText(tfield.getText() + "4");
			} else {
				tfield.setText("");
				tfield.setText(tfield.getText() + "4");
				z = 0;
			}
		}
		if (s.equals("5")) {
			
			if (z == 0) {
				tfield.setText(tfield.getText() + "5");
			} else {
				tfield.setText("");
				tfield.setText(tfield.getText() + "5");
				z = 0;
			}
		}
		if (s.equals("6")) {
			
			if (z == 0) {
				tfield.setText(tfield.getText() + "6");
			} else {
				tfield.setText("");
				tfield.setText(tfield.getText() + "6");
				z = 0;
			}
		}
		if (s.equals("7")) {
			
			if (z == 0) {
				tfield.setText(tfield.getText() + "7");
			} else {
				tfield.setText("");
				tfield.setText(tfield.getText() + "7");
				z = 0;
			}
		}
		if (s.equals("8")) {
			
			if (z == 0) {
				tfield.setText(tfield.getText() + "8");
			} else {
				tfield.setText("");
				tfield.setText(tfield.getText() + "8");
				z = 0;
			}
		}
		if (s.equals("9")) {
			
			if (z == 0) {
				tfield.setText(tfield.getText() + "9");
			} else {
				tfield.setText("");
				tfield.setText(tfield.getText() + "9");
				z = 0;
			}
		}
		if (s.equals("0")) {
			if (z == 0) {
				tfield.setText(tfield.getText() + "0");
			} else {
				tfield.setText("");
				tfield.setText(tfield.getText() + "0");
				z = 0;
			}
		}
		if (s.equals("(")) {
			if (z == 0) {
					tfield.setText("" + "(");
				} else {
					tfield.setText("");
					tfield.setText(tfield.getText() + "(");
					z = 0;
				}
				b=1;
			}
		
		if (s.equals(")")) {
			if(b==2) {
				if (z == 0) {
					tfield.setText(tfield.getText() + ")");
				} else {
					tfield.setText("");
					tfield.setText(tfield.getText() + ")");
					z = 0;
				}
				b=0;
			}
		}
		if (s.equals(",")) {
			if(b==1) {
				if (z == 0) {
					tfield.setText(tfield.getText() + ",");
				} else {
					tfield.setText("");
					tfield.setText(tfield.getText() + ",");
					z = 0;
				}
				b=2;
			}
		}
		if (s.equals("AC")) {
			tfield.setText("");
			z = 0;
			y = 0;
			x = 0;
			a = 0;
			b = 0;
		}
		if (s.equals("-")) {
			if (x == 0 || x ==1) {
				tfield.setText(tfield.getText()+"-" );
				x++;
			} else {
				tfield.setText(tfield.getText());
			}
		}
		if (s.equals(".")) {
			if (y == 0 || y ==1) {
				tfield.setText(tfield.getText() + ".");
				y++;
			} else {
				tfield.setText(tfield.getText());
			}
		}
		if (s.equals("Add")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
				temp1.setX(0);
				temp1.setY(0);
				ch = '+';
			} else {
				String aa = tfield.getText();
				tfield.setText("");
				
				String[] cord = aa.substring(1, aa.length()-1).split(",");
				temp1.setX(Double.parseDouble(cord[0]));
				temp1.setY(Double.parseDouble(cord[1]));
				ch = '+';
				y = 0;
				x = 0;
			}
			tfield.requestFocus();
		}
		if (s.equals("Slope")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
				temp1.setX(0);
				temp1.setY(0);
				ch = 's';
			} else {
				String aa = tfield.getText();
				tfield.setText("");
				String[] cord = aa.substring(1, aa.length()-1).split(",");
				temp1.setX(Double.parseDouble(cord[0]));
				temp1.setY(Double.parseDouble(cord[1]));
				ch = 's';
				y = 0;
				x = 0;
			}
		}
		if (s.equals("Equ. line")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
				temp1.setX(0);
				temp1.setY(0);
				ch = 'l';
			} else {
				String aa = tfield.getText();
				tfield.setText("");
				String[] cord = aa.substring(1, aa.length()-1).split(",");
				temp1.setX(Double.parseDouble(cord[0]));
				temp1.setY(Double.parseDouble(cord[1]));
				ch = 'l';
				y = 0;
				x = 0;
			}
		}
		if (s.equals("Manh. Dist")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
				temp1.setX(0);
				temp1.setY(0);
				ch = 'm';
			} else {
				String aa = tfield.getText();
				tfield.setText("");
				String[] cord = aa.substring(1, aa.length()-1).split(",");
				temp1.setX(Double.parseDouble(cord[0]));
				temp1.setY(Double.parseDouble(cord[1]));
				ch = 'm';
				y = 0;
				x = 0;
			}
			
		}
		if (s.equals("Eucl. Dist")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
				temp1.setX(0);
				temp1.setY(0);
				ch = 'e';
			} else {
				String aa = tfield.getText();
				tfield.setText("");
				String[] cord = aa.substring(1, aa.length()-1).split(",");
				temp1.setX(Double.parseDouble(cord[0]));
				temp1.setY(Double.parseDouble(cord[1]));
				ch = 'e';
				y = 0;
				x = 0;
			}
			
		}
		if (s.equals("Sca. Mul")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
				temp1.setX(0);
				temp1.setY(0);
				ch = '*';
			} else {
				String aa = tfield.getText();
				tfield.setText("");
				String[] cord = aa.substring(1, aa.length()-1).split(",");
				temp1.setX(Double.parseDouble(cord[0]));
				temp1.setY(Double.parseDouble(cord[1]));
				x = 0;
				y = 0;
				ch = '*';
			}
		}
		if (s.equals("Quadrant")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
				temp1.setX(0);
				temp1.setY(0);
			} else {
				String aa = tfield.getText();
				String[] cord = aa.substring(1, aa.length()-1).split(",");
				temp1.setX(Double.parseDouble(cord[0]));
				temp1.setY(Double.parseDouble(cord[1]));
				tfield.setText("Q"+temp1.whichQuadrant());
			}
		}
		if (s.equals("X Proj")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
				temp1.setX(0);
				temp1.setY(0);
			} else {
				String aa = tfield.getText();
				String[] cord = aa.substring(1, aa.length()-1).split(",");
				temp1.setX(Double.parseDouble(cord[0]));
				temp1.setY(Double.parseDouble(cord[1]));
				tfield.setText(temp1.xProj().toString());
			}
		}
		if (s.equals("Y Proj")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
				temp1.setX(0);
				temp1.setY(0);
			} else {
				String aa = tfield.getText();
				String[] cord = aa.substring(1, aa.length()-1).split(",");
				temp1.setX(Double.parseDouble(cord[0]));
				temp1.setY(Double.parseDouble(cord[1]));
				tfield.setText(temp1.yProj().toString());
			}
		}
		if (s.equals("X Refl")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
				temp1.setX(0);
				temp1.setY(0);
			} else {
				String aa = tfield.getText();
				String[] cord = aa.substring(1, aa.length()-1).split(",");
				temp1.setX(Double.parseDouble(cord[0]));
				temp1.setY(Double.parseDouble(cord[1]));
				tfield.setText(temp1.xRefl().toString());
			}
		}
		if (s.equals("Y Refl")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
				temp1.setX(0);
				temp1.setY(0);
			} else {
				String aa = tfield.getText();
				String[] cord = aa.substring(1, aa.length()-1).split(",");
				temp1.setX(Double.parseDouble(cord[0]));
				temp1.setY(Double.parseDouble(cord[1]));
				tfield.setText(temp1.yRefl().toString());
			}
		}
		if (s.equals("=")) {
			if (tfield.getText().equals("")) {
				tfield.setText("");
			} else {
				if(ch == '+') {
					String aa = tfield.getText();
					String[] cord = aa.substring(1, aa.length()-1).split(",");
					temp2.setX(Double.parseDouble(cord[0]));
					temp2.setY(Double.parseDouble(cord[1]));
					tfield.setText(temp1.sumPoint(temp2).toString());
					z = 1;
				}
				if(ch == '*') {
					scl = Double.parseDouble(tfield.getText());
					tfield.setText(temp1.scalarMult(scl).toString());
					z = 1;
				}
				if(ch == 'm') {
					String aa = tfield.getText();
					String[] cord = aa.substring(1, aa.length()-1).split(",");
					temp2.setX(Double.parseDouble(cord[0]));
					temp2.setY(Double.parseDouble(cord[1]));
					tfield.setText(""+temp1.distanceM(temp2));
				}
				if(ch == 'e') {
					String aa = tfield.getText();
					String[] cord = aa.substring(1, aa.length()-1).split(",");
					temp2.setX(Double.parseDouble(cord[0]));
					temp2.setY(Double.parseDouble(cord[1]));
					tfield.setText(""+temp1.distanceE(temp2));
				}
				if(ch == 's') {
					String aa = tfield.getText();
					String[] cord = aa.substring(1, aa.length()-1).split(",");
					temp2.setX(Double.parseDouble(cord[0]));
					temp2.setY(Double.parseDouble(cord[1]));
					tfield.setText(""+temp1.slope(temp2));
				}
				if(ch == 'l') {
					String aa = tfield.getText();
					String[] cord = aa.substring(1, aa.length()-1).split(",");
					temp2.setX(Double.parseDouble(cord[0]));
					temp2.setY(Double.parseDouble(cord[1]));
					tfield.setText(""+temp1.equLine(temp2));
				}
			}
		}
		tfield.requestFocus();
		}
		catch(Exception e1) {
			System.out.println("Enter the point in the Correct format (a,b)");
			System.out.println(e1);
		}
	}

	
	public static void main(String[] args) {
		
		try {
			UIManager.setLookAndFeel("com.sun.java.swing.plaf.gtk.GTKLookAndFeel"); 
		} 
		catch(Exception e) {
			System.out.println(e);
		}
		
		PointCalculator f = new PointCalculator();
		f.setTitle("Point Calculator");
		f.pack();
		f.setVisible(true);
		

	}

}
