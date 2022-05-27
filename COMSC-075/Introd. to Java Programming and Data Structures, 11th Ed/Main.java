


public class Main extends JFrame implements ActionListener {
	
	String[] s1 = {"mowing", "tree removal", "planting"};
	
	JComboBox c1 = new JComboBox(s1);
	
    JPanel p = new JPanel();
    
    static double totalCost = 0.0;
    
    public static void main(String[] args) {
 
        // create a object
        Main s = new Main();
        centerFrame(s);
        s.setVisible(true);
    }
    
    public Main() {
    	setLayout(new FlowLayout());
    	setSize(400, 300);
    	setTitle("SERVICES");
    	setForeground(Color.red);
    	setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    	
    	c1.setSelectedItem(1);
    	c1.addActionListener(this);
    	add(c1);
    	add(p);
    }
        
       
		
		// create labels
//        l = new JLabel("Select your service: ");
//        l1 = new JLabel("mowing selected");
 
//        l1.setForeground(Color.blue);
 
        
 
//        p.add(l);
// 
//        // add combobox to panel
//        p.add(c1);
// 
//        p.add(l1);
// 
//        // add panel to frame
//        f.add(p);
// 
//   
// 
//        f.show();
        
//        Calendar calendar = Calendar.getInstance();   
//		calendar.add(Calendar.DATE, +6);  
//		System.out.println("Our next avaliable date for service: "+ calendar.get(Calendar.MONTH) + "-" + calendar.get(Calendar.DATE) + "-" + calendar.get(Calendar.YEAR));  
//		   
//		System.out.println("What time works best for you on " + calendar.get(Calendar.MONTH) + "-" + calendar.get(Calendar.DATE) + "-" + calendar.get(Calendar.YEAR) + "?");
//		System.out.println("1 pm? 2pm? 3pm? or 4pm?");
//		Scanner in = new Scanner();
//		int time= in.nextInt();
//		   
//		System.out.println("We cannot wait to see you on " + + calendar.get(Calendar.MONTH) + "-" + calendar.get(Calendar.DATE) + "-" + calendar.get(Calendar.YEAR) + " at " 
//		   + time + " pm.");
		 
    
    public void actionPerformed(ActionEvent e) {
    	
    	if (e.getSource() == c1) {
    		JComboBox cb = (JComboBox) e.getSource();
    		String msg = (String) cb.getSelectedItem();
//    		l1.setText(c1.getSelectedItem() + " selected");
//    		Object service = c1.getSelectedItem();
//    		chosenServices += service.toString();
//			System.out.println(service);
//			System.out.println(comboBox.getSelectedIndex());
    		
    		switch (msg) {
    		
    			case "mowing": p.setText("chosen mowing"); break;
    			case "tree removal": p.setText("chosen tree removal"); break;
    			case "planting": p.setText("chosen planting"); break;
    			default: p.setText("ERROR"); 
    			
    		
    		}
//			if (service.equals("mowing")) {
//				System.out.println("Its base charge: $" + 100.0);
//				
//				totalCost += 100.0;
//			}
//			else if (service == "tree removal") {
//				System.out.println("Its base charge: $" + 1000.0);
//				
//				totalCost += 1000.0;
//			}
//			else if (service == "planting") {
//				System.out.println("Its base charge: $" + 300.0);
//				
//				totalCost += 300.0;
//			} else {
//				
//				System.out.println(totalCost);
//			}
    	}
    	
    	System.out.println("Chosen services: " + chosenServices);
    	System.out.printf("Total cost: $%,.2f\n", totalCost);
//    	int zipCode;
//    	int baseZipCodeCost = 0;
//    	Scanner in = new Scanner(System.in);
//    			
//    			//collect user input
//    	System.out.println("Whats your zip code?");
//    	zipCode = in.nextInt();
//    	        
//    	        //if-else for zipcode
//    	if (95110 <= zipCode && zipCode <= 95120 ) {
//    	        baseZipCodeCost = 150;
//    	        System.out.println("The base cost in your area is: $" + baseZipCodeCost);
//    	} else if (95121 <= zipCode && zipCode <= 95129) {
//    	        baseZipCodeCost = 200;
//    	        System.out.println("The base cost in your area is: $" + baseZipCodeCost);
//    		} else if (95130 <= zipCode && zipCode <= 95139) {
//    			baseZipCodeCost = 400;
//    			System.out.println("The base cost in your area is: $" + baseZipCodeCost);
//    		} else {
//    			System.out.println("Invalid zipcode, please try again.");
//    		}
//
//		System.out.println("First name (Required): ");
//		String firstName= in.nextLine(); 
//		
//		System.out.println("Last name (Required): ");
//		String lastName= in.nextLine(); 
//
//		System.out.println("Email (Required): ");
//		String email= in.nextLine(); 
//
//		System.out.println("Phone number (Required): ");
//		String phoneNumber= in.nextLine(); 
  
		 
    	
    }
}