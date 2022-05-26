import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

public class Box extends JFrame implements ActionListener {  
	
	JComboBox comboBox;
	double serviceCost = 0;
	List<String> serviceList = new ArrayList<>();
	
	public Box() {
		
		this.getDefaultCloseOperation();
		this.setLayout(new FlowLayout()); 
		setTitle("SERVICES");
		
		String[] services = {"mowing", "tree removal", "planting"};
	  
		comboBox = new JComboBox(services);
		comboBox.addActionListener(this);
 
		this.add(comboBox);
		this.pack();
		this.setVisible(true);
	}
	
	public double getServiceCost() {
		return serviceCost;
	}
	
	public List<String> getServiceList() {
		return serviceList;
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		 
		if(e.getSource() == comboBox) {
			Object chosenService = comboBox.getSelectedItem();
			comboBox.removeItem(chosenService);
			System.out.println("You chose: " + chosenService);
			switch(chosenService.toString()) {
				case "mowing":
					serviceCost += 100.0;
					serviceList.add("mowing");
					System.out.println("Its base charge: $100.0\n");
					break;
				case "tree removal":
					serviceCost += 1000.0;
					serviceList.add("tree removal");
					System.out.println("Its base charge: $1000.0\n");
					break;
				case "planting":
					serviceCost += 300.0;
					serviceList.add("planting");
					System.out.println("Its base charge: $300.0\n");
					break;
			}	
		}
	}
}  