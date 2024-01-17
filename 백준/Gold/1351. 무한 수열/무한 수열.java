import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static Map<Long, Long> map;
    static long p;
    static long q;

    private static long getNumber(long n) {
        if (!map.containsKey(n)) {
            map.put(n, getNumber(n / p) + getNumber(n / q));
        }
        return map.get(n);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long n = Long.parseLong(st.nextToken());
        p = Long.parseLong(st.nextToken());
        q = Long.parseLong(st.nextToken());
        map = new HashMap<>();
        map.put(0L, 1L);

        System.out.println(getNumber(n));
    }
}