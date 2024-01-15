import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;

class CustomComparator implements Comparator<String> {
    @Override
    public int compare(String s1, String s2) {
        if (s1.length() != s2.length()) {
            return s1.length() - s2.length();
        }
        return s1.compareTo(s2);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Comparator comparator = new CustomComparator();
        PriorityQueue<String> words = new PriorityQueue<>(comparator);
        Set<String> set = new HashSet<>();

        for (int i = 0; i < n; i++) {
            String target = br.readLine();
            if (!set.contains(target)) {
                words.add(target);
                set.add(target);
            }
        }

        while (!words.isEmpty()) {
            System.out.println(words.poll());
        }
    }
}