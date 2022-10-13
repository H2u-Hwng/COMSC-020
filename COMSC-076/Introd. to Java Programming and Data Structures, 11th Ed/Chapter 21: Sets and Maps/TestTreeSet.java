import java.util.*;

public class TestTreeSet {
  public static void main(String[] args) throws Exception {
    TreeSet<String> set = new TreeSet<>();
    
    set.add("Huu");
    set.add("Hung");
    set.add("Nguyen");
    
    System.out.println(set); // [Hung, Huu, Nguyen]
    System.out.println(set.first()); // Hung
    System.out.println(set.last()); // Nguyen
  }
}
