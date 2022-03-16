import java.util.Scanner;

public class wk45exercise1 {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter the number of students: ");
		int students = input.nextInt();
		
		String bestStudent = "";
		double highestScore = 0;
		
		for (int i = 1; i < students + 1; i ++) {
			System.out.printf("Enter the name and score of student %d: ", i);
			String name = input.next();
			double score = input.nextDouble();
			
			if (score > highestScore) {
				highestScore = score;
				bestStudent = name;
			}
		}
		System.out.printf("%s is the student with the highest score %.1f", 
						  bestStudent, highestScore);
	}
}
