import java.util.Scanner;

class Student {
    String name;
    int age;
    double marks;

    Student(String name, int age, double marks) {
        this.name = name;
        this.age = age;
        this.marks = marks;
    }

    void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Marks: " + marks);
    }
}

public class ex22 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of students: ");
        int n = sc.nextInt();
        sc.nextLine(); // fix input issue

        Student[] students = new Student[n];

        for (int i = 0; i < n; i++) {
            System.out.println("\nEnter details of student " + (i + 1));

            System.out.print("Name: ");
            String name = sc.nextLine();

            System.out.print("Age: ");
            int age = sc.nextInt();

            System.out.print("Marks: ");
            double marks = sc.nextDouble();
            sc.nextLine(); // clear buffer

            students[i] = new Student(name, age, marks);
        }

        System.out.println("\n--- Student Details ---");

        for (int i = 0; i < n; i++) {
            students[i].display();
            System.out.println();
        }

        sc.close();
    }
}