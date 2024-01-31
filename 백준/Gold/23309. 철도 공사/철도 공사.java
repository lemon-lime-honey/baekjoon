import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder result = new StringBuilder();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        int[] before = new int[1000001];
        int[] after = new int[1000001];
        int first = -1;
        int last = -1;

        for (int i = 0; i < n; i++) {
            int station = Integer.parseInt(st.nextToken());
            if (i == 0) {
                first = station;
            }
            if (last != -1) {
                before[station] = last;
                after[last] = station;
            }
            last = station;
        }

        before[first] = last;
        after[last] = first;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String comm = st.nextToken();

            if (comm.equals("BN")) {
                int j = Integer.parseInt(st.nextToken());
                int k = Integer.parseInt(st.nextToken());
                result.append(after[j]);
                int temp = after[j];
                after[j] = k;
                before[k] = j;
                after[k] = temp;
                before[temp] = k;
            } else if (comm.equals("BP")) {
                int j = Integer.parseInt(st.nextToken());
                int k = Integer.parseInt(st.nextToken());
                result.append(before[j]);
                int temp = before[j];
                after[temp] = k;
                before[k] = temp;
                before[j] = k;
                after[k] = j;
            } else if (comm.equals("CN")) {
                int j = Integer.parseInt(st.nextToken());
                int target = after[j];
                after[j] = after[target];
                before[after[j]] = j;
                result.append(target);
            } else if (comm.equals("CP")) {
                int j = Integer.parseInt(st.nextToken());
                int target = before[j];
                before[j] = before[target];
                after[before[j]] = j;
                result.append(target);
            }

            if (i != m - 1) {
                result.append('\n');
            }
        }

        System.out.println(result.toString());
    }
}
