import java.io.*

public class Program2 {
    public static void main(String[] args) throws Exception {
        File file = new File("testOutput.dat")
        
        BitOutputStream output = new BitOutputStream(file;
        output.writeBit("010000100100001001101");
        output.close();
        System.out.println("Done");
    }

    public static class BitOutputStream {
        private FileOutputStream output;

        // Creates a BitOutputStream to write bits to the file.
        public BitOutputStream(File file) throws IOException {
            output = new FileOutputStream(file);
        
        // Writes a string of bits to the output stream
        public void writeBit(String bitString) throws IOException {
            for (int i = 0; i < bitString.length(); i++) {
                writeBit(bitString.charAt(i));
            }
        }

        // Writes a bit '0' or '1' to the output stream
        public void writeBit(char bit) throws IOException {
            output.write(bit);
      }

     /** Write the last byte and close the stream. If the last byte is not full, right-shfit with zeros         */
     public void close() throws IOException {
         // Program statements for this method


          output.close();  // This makes use of the close() method for a FileOutputStream object
       }
   }
}
