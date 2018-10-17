package Options;
import java.text.DecimalFormat;
import java.util.Scanner;

public class NakedTrade {
	public static void ProfitOption() {

		//Sets all the needed Values
		Formulae.setAllValues();		
		
		//Results
		System.out.println();
		System.out.println("Cost is: "+Formulae.Cost);
		System.out.println("Percentage gain per $1 rise is: %"+Formulae.PercentageGain+" ($"+Formulae.Profit+")");
		System.out.println("For every 10 cents the stock moves, you make: $"+Formulae.ProfitLow);
				
	}
}
