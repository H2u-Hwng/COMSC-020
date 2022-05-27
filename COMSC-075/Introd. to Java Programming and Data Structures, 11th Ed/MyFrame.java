import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class MyFrame extends JFrame implements ActionListener{

    private static JFrame f; // frame
 
    private static JLabel l, l1; // label

	private static JComboBox comboBox; // combobox
	
	private Object service;
	private static double totalCost = 0.0;
 
	
	public MyFrame(){
		// create a new frame
        f = new JFrame("frame");
		
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLayout(new FlowLayout()); 
	  
		String[] services = {"mowing", "tree removal", "planting"};
	  
		comboBox = new JComboBox(services);
		comboBox.addActionListener(this);
	  
		//comboBox.setEditable(true);
		//System.out.println(comboBox.getItemCount());
		//comboBox.addItem("horse");
		//comboBox.insertItemAt("pig", 0);
		//comboBox.setSelectedIndex(0);
		//comboBox.removeItem("cat");
		//comboBox.removeItemAt(0);
		//comboBox.removeAllItems();
	  
		// create labels
        l = new JLabel("select your city ");
        l1 = new JLabel("Jalpaiguri selected");
 
        // set color of text
        l.setForeground(Color.red);
        l1.setForeground(Color.blue);
        
        // create a new panel
        JPanel p = new JPanel();
 
        p.add(l);
 
        // add combobox to panel
        p.add(comboBox);
 
        p.add(l1);
 
        // add panel to frame
        f.add(p);
 
        // set the size of frame
        f.setSize(400, 300);
 
        //f.show();
        
		this.add(comboBox);
		this.pack();
		this.setVisible(true);
	}
 
	public Object getItem() {
		return comboBox.getSelectedItem();
	}
	
	public int getIndex() {
		return comboBox.getSelectedIndex();
	}
	
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==comboBox) {
			service = comboBox.getSelectedItem();
			System.out.println(service);
//			System.out.println(comboBox.getSelectedIndex());
			if (service == "mowing") {
				System.out.println("Its base charge: $" + 100.0);
				
				totalCost += 100.0;
			}
			else if (service == "tree removal") {
				System.out.println("Its base charge: $" + 1000.0);
				
				totalCost += 1000.0;
			}
			else {
				System.out.println("Its base charge: $" + 300.0);
				
				totalCost += 300.0;
			}
		}
	}
}