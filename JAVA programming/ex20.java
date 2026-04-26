import java.io.FileWriter;
import java.io.IOException;

public class ex20 {
    public static void main(String[] args) {
        
        try {
            FileWriter fw = new FileWriter("test.txt");
            fw.write("Hello, this is my first file!");
            fw.close();
            
            System.out.println("File written successfully");
        } catch (IOException e) {
            System.out.println("Error writing file");
        }
    }
}