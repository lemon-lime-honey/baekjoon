import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int max = 0;

        for (int i = 1; i < k + 1; i++) {
            int temp = n * i;
            int chk = 0;
            while (temp != 0) {
                chk = 10 * chk + temp % 10;
                temp = temp / 10;
            }
            max = Math.max(max, chk);
        }
        System.out.println(max);
    }
}
