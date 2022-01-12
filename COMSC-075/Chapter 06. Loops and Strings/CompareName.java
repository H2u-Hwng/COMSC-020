public class CompareName {
    
    public static void main(String[] args) {
        String name1 = "Alan Turing";
        String name2 = "Ada lovelace";
        
        int diff = name1.compareTo(name2);
        
        if (diff < 0) {
            System.out.println(name1 + " comes before " + name2);
        } else if (diff > 0) {
            System.out.println(name2 + " comes before " + name1);
        } else {
            System.out.println("The names are the same!");
        }
    }
}
