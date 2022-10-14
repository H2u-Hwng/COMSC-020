import java.util.*;

public class TestSortedSet {
    public static void main(String[] args) throws Exception {
        TreeSet<Integer> set = new TreeSet<>();
        
        set.add(1);
        set.add(9);
        set.add(4);
        set.add(2);
        // set = [1, 2, 4, 9]
        
        SortedSet temp1 = set.headSet(5); // temp1 = [1, 2, 4]
        System.out.println(temp1.first());
        
        SortedSet temp2 = set.tailSet(2); // temp2 = [2, 4, 9]
        System.out.println(temp2.last());
    }
}
