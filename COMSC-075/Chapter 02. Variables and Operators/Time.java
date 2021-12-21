public class Time {
    
    public static void main(String[] args) {
        int hour = 11;    // set hour to 11
        int minute = 59;  // set minute to 59
        
        String output_prompt = "The current time is "; 
        
        // display the current time
        System.out.print(output_prompt);
        System.out.println(hour + ":" + minute + ".");
        
        // calculate and display the number of minutes
        int n_minutes = hour * 60 + minute;
        System.out.print("Number of minutes since midnight: ");
        System.out.println(n_minutes + " minutes");
    }
}
