public class ex7 {
    public class Main {
    public static void main(String[] args) {
        
        String name = "Tejasvi";
        
        System.out.println("Length: " + name.length());
        System.out.println("Uppercase: " + name.toUpperCase());
        System.out.println("Lowercase: " + name.toLowerCase());
        System.out.println("First character: " + name.charAt(0));
        
        if (name.equals("Tejasvi")) {
            System.out.println("Name matched!");
        }
    }
}
}
