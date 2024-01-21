import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> result = new ArrayList<>();
        int[] sub = new int[n];
        result.add(a[0]);

        for (int i = 1; i < n; i++) {
            if (result.get(result.size() - 1) < a[i]) {
                result.add(a[i]);
                sub[i] = result.size() - 1;
            } else {
                int lo = 0;
                int hi = result.size() - 1;

                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if (result.get(mid) < a[i]) {
                        lo = mid + 1;
                    } else {
                        hi = mid;
                    }
                }

                result.set(hi, a[i]);
                sub[i] = hi;
            }
        }

        int ref = result.size() - 1;
        StringBuilder sb = new StringBuilder();
        List<Integer> answer = new ArrayList<>();
        sb.append(result.size());
        sb.append('\n');

        for (int i = n - 1; i > -1; i--) {
            if (sub[i] == ref) {
                answer.add(a[i]);
                ref--;
            }
        }

        for (int i = answer.size() - 1; i > -1; i--) {
            sb.append(answer.get(i));
            if (i != 0) {
                sb.append(' ');
            }
        }

        System.out.println(sb.toString());
    }
}
