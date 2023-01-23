/*
 * Huu Hung Nguyen
 * 11/23/2022
 * Assignment 10
 * Fully implement the BST class in Listing 25.4.
 * Design and write a driver program to completely test every method
 * in the BST class to ensure the class meets all its requirements.
 */

import java.util.*;

public class TestBST {
    public static void main(String[] args) {
        // Create a BST
        BST<String> tree = new BST<>();
        tree.insert("George");
        tree.insert("Michael");
        tree.insert("Tom");
        tree.insert("Adam");
        tree.insert("Jones");
        tree.insert("Peter");
        tree.insert("Daniel");
        printTree(tree); 

        // Search for an element
        System.out.println("\nIs Peter in the tree? " + tree.search("Peter"));
        System.out.println("Is Huu in the tree? " + tree.search("Huu"));
        
        // Check the root of tree
        System.out.println("\nThe root of the tree is: " + tree.getRoot().element);

        // Get a path from the root to Peter
        System.out.print("A path from the root to Peter is: ");
        ArrayList<BST.TreeNode<String>> path = tree.path("Peter");
        for (int i = 0; path != null && i < path.size(); i++)
            System.out.print(path.get(i).element + " ");
            
        System.out.println(); // new line
    
        // Test delete
        System.out.println("\nAfter delete George:");
        tree.delete("George");
        printTree(tree);

        System.out.println("\nAfter delete Adam:");
        tree.delete("Adam");
        printTree(tree);

        System.out.println("\nAfter delete Michael:");
        tree.delete("Michael");
        printTree(tree);

        System.out.println(); // new line

        // Test iterator
        for (String s: tree)
            System.out.print(s.toUpperCase() + " ");

        System.out.println(); // new line

        // Test clear
        tree.clear();
        System.out.print("\nAfter clear: \nThe tree size is now: " +
                         tree.size);

        System.out.println(); // new line

        // Test array constructor
        Integer[] numbers = {2, 4, 3, 1, 8, 5, 6, 7};
        BST<Integer> intTree = new BST<>(numbers); 
        intTree.insert(10);
        
        // Traverse tree
        System.out.print("\nInorder (sorted): ");
        intTree.inorder();
        System.out.print("\nPostorder: ");
        intTree.postorder();
        System.out.print("\nPreorder: ");
        intTree.preorder();
        System.out.println("\nThe number of nodes is " + intTree.size());

        // Test delete
        System.out.println("\nDelete 28: " + intTree.delete(28));

        System.out.println("Delete 5: " + intTree.delete(5));
        System.out.println("After delete 5:");
        System.out.print("Inorder (sorted): ");
        intTree.inorder();
        System.out.print("\nPostorder: ");
        intTree.postorder();
        System.out.print("\nPreorder: ");
        intTree.preorder();
        System.out.println("\nThe number of nodes is " + intTree.size());

        // Test iterator
        System.out.print("\nPrinting intTree using iterator: ");
        Iterator<Integer> iterator = intTree.iterator();
        while (iterator.hasNext())
            System.out.print(iterator.next() + " ");
        
        // Test clear
        intTree.clear();
        System.out.print("\nAfter clear: \nInorder (sorted): ");
        intTree.inorder();
    }

    public static void printTree(BST<String> tree) {
        // Traverse tree
        System.out.print("Inorder (sorted): ");
        tree.inorder();
        System.out.print("\nPostorder: ");
        tree.postorder();
        System.out.print("\nPreorder: ");
        tree.preorder();
        System.out.print("\nThe number of nodes is " + tree.size());
        System.out.println();
    }
}

class BST<E extends Comparable<E>> implements Tree<E> {
    protected TreeNode<E> root;
    protected int size = 0;
  
    /** Create a default binary tree */
    public BST() {
    }
  
    /** Create a binary tree from an array of objects */
    public BST(E[] objects) {
        for (int i = 0; i < objects.length; i++)
            add(objects[i]);
    }
  
    @Override /** Returns true if the element is in the tree */
    public boolean search(E e) {
        TreeNode<E> current = root; // Start from the root
    
        while (current != null) {
            if (e.compareTo(current.element) < 0) {
                current = current.left; // go left
            } else if (e.compareTo(current.element) > 0) {
                current = current.right; // go right
            } else { // element matches current.element
                return true; // Element is found
            }
        }
    
        return false; // element is not in the tree
    }
  
    @Override /** Insert element e into the binary tree
     * Return true if the element is inserted successfully */
    public boolean insert(E e) {
        if (root == null) {
            root = createNewNode(e); // Create a new root
        } else {
            // Locate the parent node
            TreeNode<E> parent = null;
            TreeNode<E> current = root;
            while (current != null) {
                if (e.compareTo(current.element) < 0) {
                    parent = current;
                    current = current.left;
                } else if (e.compareTo(current.element) > 0) {
                    parent = current;
                    current = current.right;
                } else {
                    return false; // Duplicate node not inserted
                }
            }

            // Create the new node and attach it to the parent node
            if (e.compareTo(parent.element) < 0) {
                parent.left = createNewNode(e);
            } else {
                parent.right = createNewNode(e);
            }
        }
  
        size++;
        return true; // Element inserted successfully
    }
  
    protected TreeNode<E> createNewNode(E e) {
        return new TreeNode<>(e);
    }
  
    @Override /** Inorder traversal from the root */
    public void inorder() {
        inorder(root);
    }
  
    /** Inorder traversal from a subtree */
    protected void inorder(TreeNode<E> root) {
        if (root == null) return;

        inorder(root.left);
        System.out.print(root.element + " ");
        inorder(root.right);
    }
  
    @Override /** Postorder traversal from the root */
    public void postorder() {
        postorder(root);
    }
  
    /** Postorder traversal from a subtree */
    protected void postorder(TreeNode<E> root) {
        if (root == null) return;

        postorder(root.left);
        postorder(root.right);
        System.out.print(root.element + " ");
    }
  
    @Override /** Preorder traversal from the root */
    public void preorder() {
        preorder(root);
    }
  
    /** Preorder traversal from a subtree */
    protected void preorder(TreeNode<E> root) {
        if (root == null) return;
        
        System.out.print(root.element + " ");
        preorder(root.left);
        preorder(root.right);
    }
  
    /** This inner class is static, because it does not access 
        any instance members defined in its outer class */
    public static class TreeNode<E> {
        protected E element;
        protected TreeNode<E> left;
        protected TreeNode<E> right;
    
        public TreeNode(E e) {
            element = e;
        }
    }
  
    @Override /** Get the number of nodes in the tree */
    public int getSize() {
        return size;
    }
  
    /** Returns the root of the tree */
    public TreeNode<E> getRoot() {
        return root;
    }
  
    /** Returns a path from the root leading to the specified element */
    public ArrayList<TreeNode<E>> path(E e) {
        ArrayList<TreeNode<E>> list = new ArrayList<>();
        TreeNode<E> current = root; // Start from the root
    
        while (current != null) {
            list.add(current); // Add the node to the list
            if (e.compareTo(current.element) < 0) {
                current = current.left;
            } else if (e.compareTo(current.element) > 0) {
                current = current.right;
            } else {
                break;
            }
        }
    
        return list; // Return an array list of nodes
    }
  
    @Override /** Delete an element from the binary tree.
     * Return true if the element is deleted successfully
     * Return false if the element is not in the tree */
    public boolean delete(E e) {
        // Locate the node to be deleted and also locate its parent node
        TreeNode<E> parent = null;
        TreeNode<E> current = root;
        while (current != null) {
            if (e.compareTo(current.element) < 0) {
                parent = current;
                current = current.left;
            } else if (e.compareTo(current.element) > 0) {
                parent = current;
                current = current.right;
            } else {
                break; // Element is in the tree pointed at by current
            }
        }
  
        if (current == null)
            return false; // Element is not in the tree
  
        // Case 1: current has no left child
        if (current.left == null) {
            // Connect the parent with the right child of the current node
            if (parent == null) {
                root = current.right;
            } else {
                if (e.compareTo(parent.element) < 0)
                    parent.left = current.right;
                else
                    parent.right = current.right;
            }
        } else {
            // Case 2: The current node has a left child
            // Locate the rightmost node in the left subtree of
            // the current node and also its parent
            TreeNode<E> parentOfRightMost = current;
            TreeNode<E> rightMost = current.left;
    
            while (rightMost.right != null) {
                parentOfRightMost = rightMost;
                rightMost = rightMost.right; // Keep going to the right
            }
  
            // Replace the element in current by the element in rightMost
            current.element = rightMost.element;
    
            // Eliminate rightmost node
            if (parentOfRightMost.right == rightMost)
                parentOfRightMost.right = rightMost.left;
            else
                // Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left;     
        }
  
        size--;
        return true; // Element deleted successfully
    }
  
    @Override /** Obtain an iterator. Use inorder. */
    public Iterator<E> iterator() {
        return new InorderIterator();
    }
  
    // Inner class InorderIterator
    private class InorderIterator implements Iterator<E> {
        // Store the elements in a list
        private ArrayList<E> list = new ArrayList<>();
        private int current = 0; // Point to the current element in list
    
        public InorderIterator() {
            inorder(); // Traverse binary tree and store elements in list
        }
    
        /** Inorder traversal from the root*/
        private void inorder() {
            inorder(root);
        }
  
        /** Inorder traversal from a subtree */
        private void inorder(TreeNode<E> root) {
            if (root == null) return;

            inorder(root.left);
            list.add(root.element);
            inorder(root.right);
        }
    
        @Override /** More elements for traversing? */
        public boolean hasNext() {
            if (current < list.size())
                return true;
    
            return false;
        }
  
        @Override /** Get the current element and move to the next */
        public E next() {
            return list.get(current++);
        }
    
        @Override // Remove the element returned by the last next()
        public void remove() {
            if (current == 0) // next() has not been called yet
                throw new IllegalStateException(); 
    
            delete(list.get(--current)); 
            list.clear(); // Clear the list
            inorder(); // Rebuild the list
        }
    }
  
    @Override /** Remove all elements from the tree */
    public void clear() {
        root = null;
        size = 0;
    }
}

interface Tree<E> extends Collection<E> {
    /** Return true if the element is in the tree */
    public boolean search(E e);
  
    /** Insert element e into the binary tree
     * Return true if the element is inserted successfully */
    public boolean insert(E e);
  
    /** Delete the specified element from the tree
     * Return true if the element is deleted successfully */
    public boolean delete(E e);
    
    /** Get the number of elements in the tree */
    public int getSize();
    
    /** Inorder traversal from the root*/
    public default void inorder() {
    }
  
    /** Postorder traversal from the root */
    public default void postorder() {
    }
  
    /** Preorder traversal from the root */
    public default void preorder() {
    }
    
    @Override /** Return true if the tree is empty */
    public default boolean isEmpty() {
        return this.size() == 0;
    }
  
    @Override
    public default boolean contains(Object e) {
        return search((E)e);
    }
    
    @Override
    public default boolean add(E e) {
        return insert(e);
    }
    
    @Override
    public default boolean remove(Object e) {
        return delete((E)e);
    }
    
    @Override
    public default int size() {
        return getSize();
    }
}