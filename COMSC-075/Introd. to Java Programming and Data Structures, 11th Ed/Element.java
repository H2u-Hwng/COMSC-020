
public class Element {
	
	private String name;
	private String symbol;
	private double weight;
	private int period;
	private int group;
	
	public Element(String name, String symbol, double weight, int period, int group) {
		 this.name = name;
		 this.symbol = symbol;
		 this.weight = weight;
		 this.period = period;
		 this.group = group;
	}
	
	public String getName() {
		return name;
	}
	
	public String getSymbol() {
		return symbol;
	}
	
	public double getWeight() {
		return weight;
	}
	
	public int getPeriod() {
		return period;
	}
	
	public int getGroup() {
		return group;
	}
}
