import java.util.ArrayList;

class Student {
    String name;

    Student(String name) {
        this.name = name;
    }
}

public class ex24 {
    public static void main(String[] args) {
        
        ArrayList<Student> list = new ArrayList<>();
        
        list.add(new Student("Tejasvi"));
        list.add(new Student("Tarun"));
        
        for (Student s : list) {
            System.out.println(s.name);
        }
    }
}