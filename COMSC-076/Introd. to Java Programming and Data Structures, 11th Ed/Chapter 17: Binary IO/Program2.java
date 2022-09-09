import java.io.*;

class Program2 {
    
    public static void main(String[] args) throws Exception {
        File file = new File("testOutput.dat");
        
        BitOutputStream output = new BitOutputStream(file);
        output.writeBit("010000100100001001101");
        output.close();
        System.out.println("Done");
    }

    public static class BitOutputStream {
        private FileOutputStream output;
        private int val;
        private int count = 0;
        private int mask = 1;
        
        // Creates a BitOutputStream to write bits to the file.
        public BitOutputStream(File file) throws IOException {
            output = new FileOutputStream(file);
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
            val = val << 1;
            if (bit == '1') {
                val = val | mask;
            }
            
            if (count == 8) {
                output.write(val);
                count = 0;
            }
        }

        /** Write the last byte and close the stream. If the last byte is not full, right-shfit with zeros */
        public void close() throws IOException {  
         // Check whether the bit values are greater // than 0 or not

            if (count > 0) {
                val = val << (8 - count);
                output.write(val);
            }
            output.close();  // This makes use of the close() method for a FileOutputStream object
        }
    }
}
