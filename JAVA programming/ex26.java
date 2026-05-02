import java.util.HashMap;
public class ex26 {
    public static void main(String[] args) {
        
        HashMap<String, Integer> map = new HashMap<>();
        
        map.put("Tejasvi", 90);
        map.put("Rahul", 80);
        map.put("Ankit", 85);
for (String key : map.keySet()) {
    System.out.println(key + " -> " + map.get(key));
}
    }
}