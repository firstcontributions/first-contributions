package Options;
import java.text.DecimalFormat;

public class Formulae {
	
	//All needed variables are stored here
	public static double Ask;
	public static double Delta;
	public static int Contracts;
	public static double Cost;
	public static double PercentageGain;
	public static double Bid;
	public static double Profit;
	public static double ProfitLow;

	//Rounding decimals
	static DecimalFormat df = new DecimalFormat("#.##");
	
	//Setters
	public static void setAsk(double Ask) {
		Formulae.Ask = Ask;
	}
	public static void setCost(double Ask, int Contracts) {
		Formulae.Cost = Ask * 100 * Contracts;		
		Cost = Double.valueOf(df.format(Cost));
	}
	public static void setDelta(double Delta) {
		Formulae.Delta = Delta / 100;
	}
	public static void setPercentageGain(double Ask, double Delta) {
		Formulae.PercentageGain = (Delta / Ask) * 100;
		PercentageGain = Double.valueOf(df.format(PercentageGain));
	}
	public static void setBid(double Ask) {
		Formulae.Bid = ((Ask / 100) * getPercentageGain()) + Ask;
	}
	public static void setProfit(double Ask, int Contracts) {
		Formulae.Profit = (getBid()-Ask) * 100 * Contracts;
		Profit = Double.valueOf(df.format(Profit));
	}
	public static void setProfitLow() {
		Formulae.ProfitLow = getProfit() / 10;
		ProfitLow = Double.valueOf(df.format(ProfitLow));
	}
	public static void setAllValues() {
		setAsk(Ask);
		setCost(Ask, Contracts);
		setDelta(Delta);
		setPercentageGain(Ask, Delta);
		setBid(Ask);
		setProfit(Ask, Contracts);
		setProfitLow();
	}
	
	//Getters
	public static double getPercentageGain() {
		return Formulae.PercentageGain;
	}
	public static double getBid() {
		return Formulae.Bid;
	}
	public static double getProfit() {
		return Formulae.Profit;
	}
}
