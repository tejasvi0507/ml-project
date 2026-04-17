public class ex12 {

    class Student {
        String name;
        int age;
    }

    public static void main(String[] args) {
        ex12 obj = new ex12();              // create outer class object
        Student s1 = obj.new Student();    // create inner class object

        s1.name = "Tejasvi";
        s1.age = 20;

        System.out.println(s1.name);
        System.out.println(s1.age);
    }
}