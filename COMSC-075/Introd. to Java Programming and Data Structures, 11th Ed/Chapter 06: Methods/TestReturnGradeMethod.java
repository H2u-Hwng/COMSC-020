public class TestReturnGradeMethod {
  
  public static char getGrade(double score) {
    char result;
    if (score >= 90.0) result = 'A';
    else if (score >= 80.0) result = 'B';
    else if (score >= 70.0) result = 'C';
    else if (score >= 60.0) result = 'D';
    else result = 'F';
    
    return result;
  }
  
  public static void main(String[] args) {
    System.out.print("The grade is " + getGrade(78.5));
    System.out.print("\nThe grade is " + getGrade(59.5));
  }
}
