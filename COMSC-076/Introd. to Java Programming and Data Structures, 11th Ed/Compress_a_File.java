/*
 * Maggie Luu, Acsa Chavez Noguera, Huu Hung Nguyen, Matthew Trans
 * 12/14/2022
 * Programming Project Part I
 * The program compress a source file into a target file using the Huffman
 * coding method. First, use ObjectOutputStream to output the Huffman codes
 * into the target file, then use BitOutputStream from Assignment #2 to output
 * the encoded binary contents to the target file.
 * Pass the files from the command line using something like the following
 * command: java Compress_a_File sourceFile.txt compressedFile.txt
 */

import java.io.*;
import java.util.*;

public class Compress_a_File {
    /** Main method */
    public static void main(String[] args) throws IOException {
        // Check whether the file names are passed in the command line
        if (args.length != 2) {
            // Display error messasge and console suggestion
            System.out.println("ERROR! Please use (java File_Name " +
                    "sourceFile.txt targetFile.txt) in the command line.");
            System.exit(1);
        }

        // Get the file names from the command line
        String fileName1 = args[0];
        String fileName2 = args[1];

        // Check whether the source file exists
        File sourceFile = new File(fileName1);
        if (!sourceFile.exists()) {
            System.out.println("File " + fileName1 + " does not exist");
            System.exit(2);
        }

        // Create the compressed file
        File compressedFile = new File(fileName2);

        // Create DataInputStream object to read the file to the text
        DataInputStream inputStream = new DataInputStream(
                new BufferedInputStream(new FileInputStream(sourceFile)));
        int size = inputStream.available();
        byte[] bytes = new byte[size];
        inputStream.read(bytes);
        inputStream.close();
        // Create string from data read from the source file
        String text = new String(bytes);

        int[] counts = getCharacterFrequency(text); // Count frequency
        Tree tree = getHuffmanTree(counts); // Create a Huffman tree
        String[] codes = getCode(tree.root); // Get codes for each character

        StringBuilder sBuilder = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            sBuilder.append(codes[text.charAt(i)]);
        }

        // Output the Huffman codes into the target file
        storeCodes(fileName2, codes, sBuilder.length());

        // Output the encoded binary contents to the target file
        encode(compressedFile, sBuilder);
    }

    /** Use ObjectOutputStream to output the Huffman codes into the file */
    public static void storeCodes(String fileName, String[] codes,
            long numChars) throws IOException {
        ObjectOutputStream output = new ObjectOutputStream(
                new FileOutputStream(fileName));
        output.writeObject(codes);
        output.writeLong(numChars);
        output.close();
    }

    /**
     * Use BitOutputStream to output the encoded binary contents to the
     * target file
     */
    public static void encode(File targetFile, StringBuilder contents)
            throws IOException {
        BitOutputStream output = new BitOutputStream(targetFile);
        output.writeBit(contents.toString());
        output.close();
    }

    /**
     * Get Huffman codes for the characters
     * This method is called once after a Huffman tree is built
     */
    public static String[] getCode(Tree.Node root) {
        if (root == null)
            return null;
        String[] codes = new String[2 * 128];
        assignCode(root, codes);
        return codes;
    }

    /* Recursively get codes to the leaf node */
    private static void assignCode(Tree.Node root, String[] codes) {
        if (root.left != null) {
            root.left.code = root.code + "0";
            assignCode(root.left, codes);

            root.right.code = root.code + "1";
            assignCode(root.right, codes);
        } else {
            codes[(int) root.element] = root.code;
        }
    }

    /** Get a Huffman tree from the codes */
    public static Tree getHuffmanTree(int[] counts) {
        // Create a heap to hold trees
        Heap<Tree> heap = new Heap<>();
        for (int i = 0; i < counts.length; i++) {
            if (counts[i] > 0)
                heap.add(new Tree(counts[i], (char) i)); // A leaf node tree
        }

        while (heap.getSize() > 1) {
            Tree t1 = heap.remove(); // Remove the smallest weight tree
            Tree t2 = heap.remove(); // Remove the next smallest weight
            heap.add(new Tree(t1, t2)); // Combine two trees
        }

        return heap.remove(); // The final tree
    }

    /** Get the frequency of the characters */
    public static int[] getCharacterFrequency(String text) {
        int[] counts = new int[256]; // 256 ASCII characters

        for (int i = 0; i < text.length(); i++)
            counts[(int) text.charAt(i)]++; // Count the character in text

        return counts;
    }

    /** Define a Huffman coding tree */
    public static class Tree implements Comparable<Tree> {
        Node root; // The root of the tree

        /** Create a tree with two subtrees */
        public Tree(Tree t1, Tree t2) {
            root = new Node();
            root.left = t1.root;
            root.right = t2.root;
            root.weight = t1.root.weight + t2.root.weight;
        }

        /** Create a tree containing a leaf node */
        public Tree(int weight, char element) {
            root = new Node(weight, element);
        }

        @Override /** Compare trees based on their weights */
        public int compareTo(Tree t) {
            if (root.weight < t.root.weight) // Purposely reverse the order
                return 1;
            else if (root.weight == t.root.weight)
                return 0;
            else
                return -1;
        }

        public class Node {
            char element; // Stores the character for a leaf node
            int weight; // weight of the subtree rooted at this node
            Node left; // Reference to the left subtree
            Node right; // Reference to the right subtree
            String code = ""; // The code of this node from the root

            /** Create an empty node */
            public Node() {
            }

            /** Create a node with the specified weight and character */
            public Node(int weight, char element) {
                this.weight = weight;
                this.element = element;
            }
        }
    }
}

class Heap<E extends Comparable<E>> {
    private java.util.ArrayList<E> list = new java.util.ArrayList<>();

    /** Create a default heap */
    public Heap() {
    }

    /** Create a heap from an array of objects */
    public Heap(E[] objects) {
        for (int i = 0; i < objects.length; i++)
            add(objects[i]);
    }

    /** Add a new object into the heap */
    public void add(E newObject) {
        list.add(newObject); // Append to the heap
        int currentIndex = list.size() - 1; // The index of the last node

        while (currentIndex > 0) {
            int parentIndex = (currentIndex - 1) / 2;
            // Swap if the current object is greater than its parent
            if (list.get(currentIndex).compareTo(list.get(parentIndex)) > 0) {
                E temp = list.get(currentIndex);
                list.set(currentIndex, list.get(parentIndex));
                list.set(parentIndex, temp);
            } else {
                break; // the tree is a heap now
            }
            currentIndex = parentIndex;
        }
    }

    /** Remove the root from the heap */
    public E remove() {
        if (list.size() == 0)
            return null;

        E removedObject = list.get(0);
        list.set(0, list.get(list.size() - 1));
        list.remove(list.size() - 1);

        int currentIndex = 0;
        while (currentIndex < list.size()) {
            int leftChildIndex = 2 * currentIndex + 1;
            int rightChildIndex = 2 * currentIndex + 2;

            // Find the maximum between two children
            if (leftChildIndex >= list.size())
                break; // The tree is a heap
            int maxIndex = leftChildIndex;
            if (rightChildIndex < list.size()) {
                if (list.get(maxIndex).compareTo(
                        list.get(rightChildIndex)) < 0) {
                    maxIndex = rightChildIndex;
                }
            }

            // Swap if the current node is less than the maximum
            if (list.get(currentIndex).compareTo(list.get(maxIndex)) < 0) {
                E temp = list.get(maxIndex);
                list.set(maxIndex, list.get(currentIndex));
                list.set(currentIndex, temp);
                currentIndex = maxIndex;
            } else {
                break; // The tree is a heap
            }
        }

        return removedObject;
    }

    /** Get the number of nodes in the tree */
    public int getSize() {
        return list.size();
    }

    /** Return true if heap is empty */
    public boolean isEmpty() {
        return list.size() == 0;
    }
}

/** Create a class BitOutputStream to write bit values into a file */
class BitOutputStream {
    // Declare required variables
    private DataOutputStream output;
    private int value;
    private int count = 0;

    // Creates a BitOutputStream to write bits to the file
    public BitOutputStream(File file) throws IOException {
        output = new DataOutputStream(new FileOutputStream(file, true));
    }

    // Writes a string of bits to the output stream
    public void writeBit(String bitString) throws IOException {
        for (int i = 0; i < bitString.length(); i++) {
            writeBit(bitString.charAt(i));
        }
    }

    // Writes a bit '0' or '1' to the output stream
    public void writeBit(char bit) throws IOException {
        count++;
        value = value << 1;
        if (bit == '1') {
            value = value | 1;
        }

        if (count == 8) {
            count = 0;
            output.write(value);
        }
    }

    // Write the last byte and close the stream
    public void close() throws IOException {
        // Check if the last byte is not full, right-shfit with zeros
        if (count > 0) {
            value = value << (8 - count);
            output.write(value);
        }
        // close method for a FileOutputStream object
        output.close();
    }
}