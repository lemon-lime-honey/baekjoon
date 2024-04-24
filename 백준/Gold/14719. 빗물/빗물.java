import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        int[] heights = new int[w];

        for (int i = 0; i < w; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
        }

        int lo = 0, hi = w - 1;
        int maxL = heights[0], maxR = heights[w - 1];
        int result = 0;

        while (lo < hi) {
            if (maxL < maxR) {
                lo++;
                maxL = Math.max(maxL, heights[lo]);
                result += Math.max(0, maxL - heights[lo]);
            } else {
                hi--;
                maxR = Math.max(maxR, heights[hi]);
                result += Math.max(0, maxR - heights[hi]);
            }
        }

        System.out.println(result);
    }
}
