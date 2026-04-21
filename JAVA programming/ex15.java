public class ex15 {

    static class Student {
        String name;

        Student(String name) {
            this.name = name;
        }
    }

    public static void main(String[] args) {
        Student s1 = new Student("Tejasvi");
        System.out.println(s1.name);
    }
}