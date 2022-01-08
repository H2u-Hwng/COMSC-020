public class Fruit {
    
    public static void main(String[] args) {
        String fruit = "Banana";
        char letter = fruit.charAt(0);
      
        if (letter == 'A') {
            System.out.println("It's an A");
        } else {
            System.out.printf("It's a/n %s", letter);
            System.out.println();
        }
    }
}
