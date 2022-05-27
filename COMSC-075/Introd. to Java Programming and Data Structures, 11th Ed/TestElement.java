
public class TestElement {

	public static void main(String[] args) {
		Element[] chemicals = {
				new Element("hydrogen", "H", 1.008, 1, 1),
				new Element("helium", "He", 4.0026, 1, 18),
				new Element("lithium", "Li", 6.94, 2, 1),
				new Element("beryllium", "be", 9.0122, 2, 2),
		};
		
		double totalWeight = 0.0;
		for (Element el: chemicals) {
			totalWeight += el.getWeight();
		}		
		double averageWeight = totalWeight / chemicals.length;
		System.out.printf("Average atomic weight: %.3f\n", averageWeight);
	}
}
