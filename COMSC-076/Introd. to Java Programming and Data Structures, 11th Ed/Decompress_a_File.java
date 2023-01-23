/*
 * Maggie Luu, Acsa Chavez Noguera, Huu Hung Nguyen, Matthew Trans
 * 12/14/2022
 * Programming Project Part II
 * The program decompress a previously compressed file so that it replicates
 * the original source file in Part I above.
 * Pass the files from the command line using something like the following
 * command: java Decompress_a_File compressedFile.txt decompressedFile.txt
 */

import java.io.*;

public class Decompress_a_File {
    /** Main method */
    public static void main(String[] args) throws IOException,
            ClassNotFoundException {
        // Check whether the file names are passed in the command line
        if (args.length != 2) {
            // Display error messasge and console suggestion
            System.out.println("ERROR! Please use (java File_Name " +
                    "sourceFile.txt targetFile.txt) in the command line.");
            System.exit(1);
        }

        // Get the file names from the command line
        String fileName1 = args[0];

        // Check whether the source file exists
        File sourceFile = new File(fileName1);
        if (!sourceFile.exists()) {
            System.out.println("File " + fileName1 + " does not exist");
            System.exit(2);
        }

        // initializes input stream to recieve data from the source file
        FileInputStream input = new FileInputStream(fileName1);

        // decode message
        ObjectInputStream objectInput = new ObjectInputStream(input);
        // get the array of Huffman codes
        String[] codes = getCodes(objectInput);
        int messageSize = getSize(objectInput);

        // get the encoded message
        BitInputStream bitInput = new BitInputStream(input);
        StringBuilder encodedMessage = getMessage(bitInput, messageSize);

        // close the stream
        input.close();

        // gets a resulting decoded message from the codes and encoded message
        String result = getResult(codes, encodedMessage);

        DataOutputStream output = new DataOutputStream(
                new FileOutputStream(args[1]));
        output.write(result.getBytes());
        output.close();
    }

    public static String getResult(String[] codes,
            StringBuilder encodedMessage) {
        StringBuilder result = new StringBuilder();
        while (encodedMessage.length() != 0) {
            boolean isOk = false;
            for (int i = 0; i < codes.length; i++) {
                if ((codes[i] != null) &&
                        (encodedMessage.indexOf(codes[i]) == 0)) {
                    result.append((char) i);
                    encodedMessage.delete(0, codes[i].length());
                    isOk = true;
                    break;
                }
            }
            if (!isOk) {
                System.out.println("Bad source file format");
                System.exit(2);
            }
        }
        return result.toString();
    }

    /**
     * Gets the codes from the input stream.
     */
    public static String[] getCodes(ObjectInputStream input)
            throws IOException, ClassNotFoundException {
        return (String[]) (input.readObject());
    }

    /**
     * Gets the size of the message from the input stream.
     */
    public static int getSize(ObjectInputStream input) throws IOException {
        return (int) input.readLong();
    }

    /**
     * Gets the encoded message (in binary) from the input stream.
     */
    public static StringBuilder getMessage(BitInputStream input,
            int messageSize) throws IOException {
        StringBuilder message = new StringBuilder();

        int bit;
        while ((bit = input.readBit()) != -1) {
            message.append(bit);
        }
        // trim the encoded message
        message.delete(messageSize, message.length());
        return message;
    }
}

/**
 * Class to read the input bit-by-bit.
 */
class BitInputStream extends InputStream {
    private FileInputStream input;
    int currentByte;
    int bitsRead;

    /**
     * Constructs a BitInputStream, initializing the variables currentByte and
     * bitsRead.
     */
    public BitInputStream(FileInputStream input) throws IOException {
        this.input = input;
        bitsRead = 0;
        currentByte = this.input.read();
    }

    /**
     * Reads the input stream bit-by-bit.
     * 
     * @return the next bit in the input stream.
     */
    public int readBit() throws IOException {
        // reads the next byte after the current byte has been fully read
        if (bitsRead == 8) {
            bitsRead = 0;
            currentByte = input.read();
        }

        // returns -1 if there are no more bytes
        if (currentByte == -1) {
            return -1;
        }

        int bit = (currentByte >> (7 - bitsRead)) & 1; // reads the next bit
        bitsRead++; // increments bits read by 1

        return bit; // returns the bit that was read
    }

    @Override
    public int read() throws IOException {
        return input.read();
    }

    public void close() throws IOException {
        input.close();
    }
}
