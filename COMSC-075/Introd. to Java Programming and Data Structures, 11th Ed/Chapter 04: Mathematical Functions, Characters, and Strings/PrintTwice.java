public class PrintTwice {

    public static void printTwice(String s) {
        System.out.println(s);
        System.out.println(s);
    }

    public static void main(String[] args) {
        printTwice("Don't make me say this twice!");

        String message = "Never say never.";
        printTwice(message);
           
        printTwice(" ");
        printTwice("HIPHOP NEVER DIE");
    }

}
