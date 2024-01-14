import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            fibonacci(Integer.parseInt(br.readLine()));
        }
    }

    private static void fibonacci(int n) {
        List<Integer> zero = new ArrayList<>(List.of(1, 0, 1));
        List<Integer> one = new ArrayList<>(List.of(0, 1, 1));

        if (n >= 3) {
            for (int i = 2; i < n; i++) {
                zero.add(zero.get(i) + zero.get(i - 1));
                one.add(one.get(i) + one.get(i - 1));
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(zero.get(n));
        sb.append(' ');
        sb.append(one.get(n));

        System.out.println(sb.toString());
    }
}