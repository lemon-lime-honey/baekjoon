import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            long[] costs = new long[n];
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                costs[j] = Long.parseLong(st.nextToken());
            }

            long high = costs[n - 1];
            long result = 0L;

            for (int j = n - 2; j > -1; j--) {
                if (costs[j] < high) {
                    result += high - costs[j];
                } else if (costs[j] > high) {
                    high = costs[j];
                }
            }

            System.out.println(result);
        }
    }
}