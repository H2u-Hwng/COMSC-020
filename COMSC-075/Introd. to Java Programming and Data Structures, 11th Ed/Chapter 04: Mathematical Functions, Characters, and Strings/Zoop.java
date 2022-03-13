public class Zoop {
	
    public static void clink(int fork) {
        System.out.print("It's ");
        zoop("breakfast ", fork);
    }

    public static void ping(String strangStrung) {
        System.out.println("any " + strangStrung + "more ");
    }
    
    public static void zoop(String fred, int bob) {
        System.out.println(fred);
        if (bob == 5) {
            ping("not ");
        } else {
            System.out.println("!");
        }
    }
    
    public static void main(String[] args) {
        int bizz = -6;
        int buzz = 1;
        zoop("just for", bizz);
        clink(5 * buzz);
    }
}
