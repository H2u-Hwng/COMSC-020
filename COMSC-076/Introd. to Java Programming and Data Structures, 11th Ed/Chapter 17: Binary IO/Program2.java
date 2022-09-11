/*
 * Huu Hung Nguyen
 * 09/12/2022
 * Assignment 2
 * Implement a class named BitOutputStream for writing bits to a file.
 * The writeBit(char bit) method stores the bit in a byte variable.
 * When a byte is full, it is sent to the output stream and is reset.
 * The program close the stream by invoking the close() method.
 * If a byte is neither empty nor full, the close() method first fills in
 * zeros to make a full 8 bits in the byte, and then closes the stream.
 */

import java.io.*;

public class Program2 {
    /** Main method */
    public static void main(String[] args) throws Exception {
        File file = new File("testOutput.dat");
        BitOutputStream output = new BitOutputStream(file);
        output.writeBit("010000100100001001101");
        output.close();
        System.out.println("Done");
    }

    /** Create a class BitOutputStream to write bit values into a file */
    public static class BitOutputStream {
        // Declare required variables
        private FileOutputStream output;
        private int value;
        private int count = 0;
        
        // Creates a BitOutputStream to write bits to the file
        public BitOutputStream(File file) throws IOException {
            output = new FileOutputStream(file);
        }
        
        // Writes a string of bits to the output stream
        public void writeBit(String bitString) throws IOException {
            for (int i = 0; i < bitString.length(); i ++) {
                writeBit(bitString.charAt(i));
            }
        }

        // Writes a bit '0' or '1' to the output stream
        public void writeBit(char bit) throws IOException {
            count ++;
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
}