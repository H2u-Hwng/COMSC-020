public class TestFan {
    
    public static void main(String[] args) {
        Fan f1 = new Fan();
        System.out.println(f1.toString());
        
        Fan f2 = new Fan(3, true, 10.0, "yellow");
        System.out.println(f2.toString());
    }
}
