public class PassedHour {
    
    public static void main(String[] args) {
        double minute = 58.30; // set minute to 58.30
        
        // calculate and display the fraction
        double fraction = minute / 60.0; 
        System.out.print("Fraction of the hour that has passed: ");
        System.out.println(fraction);
        
        // calculate and display the percent
        double percent = fraction * 100.0;
        System.out.print("Percent of the hour that has passed: ");
        System.out.println(percent + "%");
    }
}
