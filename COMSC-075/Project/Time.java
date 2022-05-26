import java.util.Scanner;
import java.util.Calendar;
import java.util.InputMismatchException;

public class Time {

	public Time() { 
		Calendar calendar = Calendar.getInstance();  
		
		calendar.add(Calendar.DATE, +6);  
		System.out.println("Our next avaliable date for service: "+ calendar.get(Calendar.MONTH) + "-" + calendar.get(Calendar.DATE) + "-" + calendar.get(Calendar.YEAR));  
		   
		System.out.println("What time works best for you on " + calendar.get(Calendar.MONTH) + "-" + calendar.get(Calendar.DATE) + "-" + calendar.get(Calendar.YEAR) + "?");
		
		boolean valid = false;
		double time = 0;
		int hours = 0;
		int minutes = 0;
		
		while (!valid) {
			try {
				Scanner input = new Scanner(System.in);
				
				System.out.println("1PM? 1.5PM? 2PM? 3PM? or 4PM?");
				time = input.nextDouble();
				
				if (time >= 1.0 && time <= 4.0) {
					time *= 60;
					hours = (int) (time / 60);
					minutes = (int) (time % 60);
					
					valid = true;
					
				} else {
					System.err.println("Invalid time, please try again.");
				}
			} catch (InputMismatchException ex) {
				System.err.println("Please use digits only.");
			} catch (Exception ex) {
				System.err.println("Error in program.");
			}
		}
		
		System.out.print("\nWe cannot wait to see you on " + 
		calendar.get(Calendar.MONTH) + "-" + calendar.get(Calendar.DATE) + 
		"-" + calendar.get(Calendar.YEAR) + " at ");
		System.out.printf("%d:%02dPM.\n", hours, minutes);
	}
}