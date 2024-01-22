import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {
    static class CustomComparator implements Comparator<String> {
        public int compare(String x, String y) {
            if (Character.isDigit(x.charAt(0)) && !Character.isDigit(y.charAt(0))) {
                return -1;
            }
            if (!Character.isDigit(x.charAt(0)) && Character.isDigit(y.charAt(0))) {
                return 1;
            }

            List<StringBuilder> xList = new ArrayList<>();
            List<StringBuilder> yList = new ArrayList<>();

            for (int i = 0; i < x.length(); i++) {
                if (xList.isEmpty() || !Character.isDigit(x.charAt(i))) {
                    StringBuilder sb = new StringBuilder();
                    sb.append(x.charAt(i));
                    xList.add(sb);
                } else if (!Character.isDigit(xList.get(xList.size() - 1).charAt(0))) {
                    StringBuilder sb = new StringBuilder();
                    sb.append(x.charAt(i));
                    xList.add(sb);
                } else {
                    StringBuilder sb = xList.get(xList.size() - 1);
                    sb.append(x.charAt(i));
                }
            }

            for (int i = 0; i < y.length(); i++) {
                if (yList.isEmpty() || !Character.isDigit(y.charAt(i))) {
                    StringBuilder sb = new StringBuilder();
                    sb.append(y.charAt(i));
                    yList.add(sb);
                } else if (!Character.isDigit(yList.get(yList.size() - 1).charAt(0))) {
                    StringBuilder sb = new StringBuilder();
                    sb.append(y.charAt(i));
                    yList.add(sb);
                } else {
                    StringBuilder sb = yList.get(yList.size() - 1);
                    sb.append(y.charAt(i));
                }
            }

            int i = 0;
            int j = 0;

            while (i < xList.size() && j < yList.size()) {
                if (Character.isDigit(xList.get(i).charAt(0)) && !Character.isDigit(yList.get(j).charAt(0))) {
                    return -1;
                }
                if (!Character.isDigit(xList.get(i).charAt(0)) && Character.isDigit(yList.get(j).charAt(0))) {
                    return 1;
                }
                if (Character.isDigit(xList.get(i).charAt(0)) && Character.isDigit(yList.get(j).charAt(0))) {
                    BigInteger xVal = new BigInteger(xList.get(i).toString());
                    BigInteger yVal = new BigInteger(yList.get(j).toString());
                    if (xVal.compareTo(yVal) < 0) {
                        return -1;
                    } else if (xVal.compareTo(yVal) > 0) {
                        return 1;
                    } else if (xList.get(i).length() < yList.get(j).length()) {
                        return -1;
                    } else if (xList.get(i).length() > yList.get(j).length()) {
                        return 1;
                    }
                }
                if (Character.toLowerCase(xList.get(i).charAt(0)) == Character.toLowerCase(yList.get(j).charAt(0))) {
                    if (Character.isUpperCase(xList.get(i).charAt(0)) && Character.isLowerCase(yList.get(j).charAt(0))) {
                        return -1;
                    } else if (Character.isLowerCase(xList.get(i).charAt(0)) && Character.isUpperCase(yList.get(j).charAt(0))) {
                        return 1;
                    }
                } else if (Character.toLowerCase(xList.get(i).charAt(0)) < Character.toLowerCase(yList.get(j).charAt(0))) {
                    return -1;
                } else if (Character.toLowerCase(xList.get(i).charAt(0)) > Character.toLowerCase(yList.get(j).charAt(0))) {
                    return 1;
                }

                i++;
                j++;
            }

            if (i == xList.size()) {
                return -1;
            }
            if (j == yList.size()) {
                return 1;
            }

            return 0;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<String> strs = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            strs.add(br.readLine());
        }

        Collections.sort(strs, new CustomComparator());
        StringBuilder sb = new StringBuilder();

        for (String str: strs) {
            sb.append(str);
            sb.append('\n');
        }

        sb.deleteCharAt(sb.length() - 1);
        System.out.println(sb.toString());
    }
}
