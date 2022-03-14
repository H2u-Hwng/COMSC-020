public class Wugga {

    public static void ping() {
        System.out.println(".");
    }
    
    public static void baffle() {
        System.out.print("wug");
        ping();
    }
    
    public static void zoop() {
        baffle();
        System.out.print("You wugga ");
        baffle();
    }
    
    public static void main(String[] args) {
        System.out.print("Yes, we ");
        baffle();
        System.out.print("I ");
        zoop();
    }
}
