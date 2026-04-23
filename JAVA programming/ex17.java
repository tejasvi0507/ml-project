class Animal {
    void sound() {
        System.out.println("Animal makes sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}

public class ex17 {
    public static void main(String[] args) {
        
        Animal a = new Dog();  // parent reference
        
        a.sound();  // calls Dog's method
    }
}