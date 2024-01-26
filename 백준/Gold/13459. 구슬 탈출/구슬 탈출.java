import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    private static String[] board;
    private static int[][] delta = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] initialInfo = {0, 0, 0, 0, 0};
        board = new String[n];

        for (int i = 0; i < n; i++) {
            board[i] = br.readLine();
            for (int j = 0; j < m; j++) {
                if (board[i].charAt(j) == 'B') {
                    initialInfo[0] = i;
                    initialInfo[1] = j;
                } else if (board[i].charAt(j) == 'R') {
                    initialInfo[2] = i;
                    initialInfo[3] = j;
                }
            }
        }

        System.out.println(bfs(initialInfo));
    }

    private static int bfs(int[] initialInfo) {
        Queue<int[]> que = new ArrayDeque<>();
        Set<int[]> chk = new HashSet<>();
        que.add(initialInfo);
        chk.add(Arrays.copyOfRange(initialInfo, 0, 4));

        while (!que.isEmpty()) {
            int[] now = que.poll();

            if (now[4] >= 10) {
                return 0;
            }

            for (int i = 0; i < 4; i++) {
                int[] blue = move(now[0], now[1], i);
                int[] red = move(now[2], now[3], i);

                if (board[blue[0]].charAt(blue[1]) != 'O') {
                    if (board[red[0]].charAt(red[1]) == 'O') {
                        return 1;
                    }

                    if (blue[0] == red[0] && blue[1] == red[1]) {
                        if (blue[2] <= red[2]) {
                            red[0] -= delta[i][0];
                            red[1] -= delta[i][1];
                        } else {
                            blue[0] -= delta[i][0];
                            blue[1] -= delta[i][1];
                        }
                    }

                    int[] temp = {blue[0], blue[1], red[0], red[1], now[4] + 1};

                    if (chk.contains(Arrays.copyOfRange(temp, 0, 4))) {
                        continue;
                    }

                    chk.add(Arrays.copyOfRange(temp, 0, 4));
                    que.add(temp);
                }
            }
        }

        return 0;
    }

    private static int[] move(int r, int c, int idx) {
        int mv = 0;

        while (board[r + delta[idx][0]].charAt(c + delta[idx][1]) != '#' && board[r].charAt(c) != 'O') {
            r += delta[idx][0];
            c += delta[idx][1];
            mv++;
        }

        return new int[]{r, c, mv};
    }
}
