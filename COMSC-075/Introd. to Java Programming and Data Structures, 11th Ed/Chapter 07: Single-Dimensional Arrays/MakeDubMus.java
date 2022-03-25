import java.util.*;

/**
 * Stack diagram exercise.
 */

public class MakeDubMus {

    public static int[] make(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = i + 1;
        }
        return a;
    }

    public static void dub(int[] jub) {
        for (int i = 0; i < jub.length; i++) {
            jub[i] *= 2;
        }
    }

    public static int mus(int[] zoo) {
        return Arrays.stream(zoo).sum();
    }
    
    public static int mus2(int[] zoo2) {
    	int fus = 0;
    	
    	for (int value : zoo2) {
    		fus += value;
    	}
    	
    	return fus;
    }

    public static void main(String[] args) {
        int[] bob = make(5);
        dub(bob);
        System.out.println(mus(bob));
        System.out.println(mus2(bob));
    }
}
