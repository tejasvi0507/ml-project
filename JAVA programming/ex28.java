import java.util.LinkedList;
import java.util.Queue;
public class ex28 {
    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();
        q.add(10);
        q.add(20);
        q.add(30);
        System.out.println(q);  // [10, 20, 30]
        q.remove();  // removes 10
        System.out.println(q);  // [20, 30]
        System.out.println(q.peek()); // front
    }
}

