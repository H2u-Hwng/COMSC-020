public class TestVoidMethod {
	
	public static void printGrade(double score) {
  		char result;
  		
  		if (score >= 90.0) result = 'A';
	    else if (score >= 80.0) result = 'B';
	    else if (score >= 70.0) result = 'C';
	    else if (score >= 60.0) result = 'D';
	    else result = 'F';
	    
	    System.out.println(result);
  	}
	
	public static void main(String[] args) {
  		System.out.print("The grade is ");
		  printGrade(78.5);

		  System.out.print("The grade is ");
		  printGrade(59.5);
	}	
}
