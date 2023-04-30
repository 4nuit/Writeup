package defpackage;

import java.util.Scanner;
/* renamed from: Sekai  reason: default package */
/* loaded from: Matrix_Lab_1.class */
public class Sekai {
    private static int length;
    static final /* synthetic */ boolean $assertionsDisabled;

    static {
        $assertionsDisabled = !Sekai.class.desiredAssertionStatus();
        length = ((int) Math.pow(2.0d, 3.0d)) - 2;
    }

    public static void main(String[] strArr) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the flag: ");
        String next = scanner.next();
        if (next.length() != 43) {
            System.out.println("Oops, wrong flag!");
            return;
        }
        String substring = next.substring(0, length);
        String substring2 = next.substring(length, next.length() - 1);
        String substring3 = next.substring(next.length() - 1);
        if (substring.equals("SEKAI{") && substring3.equals("}")) {
            if (!$assertionsDisabled && substring2.length() != length * length) {
                throw new AssertionError();
            }
            if (solve(substring2)) {
                System.out.println("Congratulations, you got the flag!");
                return;
            } else {
                System.out.println("Oops, wrong flag!");
                return;
            }
        }
        System.out.println("Oops, wrong flag!");
    }

    public static String encrypt(char[] cArr, int i) {
        char[] cArr2 = new char[length * 2];
        int i2 = length - 1;
        int i3 = length;
        for (int i4 = 0; i4 < length * 2; i4 = i4 + 1 + 1) {
            int i5 = i2;
            i2--;
            cArr2[i4] = cArr[i5];
            int i6 = i3;
            i3++;
            cArr2[i4 + 1] = cArr[i6];
        }
        for (int i7 = 0; i7 < length * 2; i7++) {
            int i8 = i7;
            cArr2[i8] = (char) (cArr2[i8] ^ ((char) i));
        }
        return String.valueOf(cArr2);
    }

    public static char[] getArray(char[][] cArr, int i, int i2) {
        char[] cArr2 = new char[length * 2];
        int i3 = 0;
        for (int i4 = 0; i4 < length; i4++) {
            cArr2[i3] = cArr[i][i4];
            i3++;
        }
        for (int i5 = 0; i5 < length; i5++) {
            cArr2[i3] = cArr[i2][(length - 1) - i5];
            i3++;
        }
        return cArr2;
    }

    public static char[][] transform(char[] cArr, int i) {
        char[][] cArr2 = new char[i][i];
        for (int i2 = 0; i2 < i * i; i2++) {
            cArr2[i2 / i][i2 % i] = cArr[i2];
        }
        return cArr2;
    }

    public static boolean solve(String str) {
        char[][] transform = transform(str.toCharArray(), length);
        for (int i = 0; i <= length / 2; i++) {
            for (int i2 = 0; i2 < (length - (2 * i)) - 1; i2++) {
                char c = transform[i][i + i2];
                transform[i][i + i2] = transform[((length - 1) - i) - i2][i];
                transform[((length - 1) - i) - i2][i] = transform[(length - 1) - i][((length - 1) - i) - i2];
                transform[(length - 1) - i][((length - 1) - i) - i2] = transform[i + i2][(length - 1) - i];
                transform[i + i2][(length - 1) - i] = c;
            }
        }
        return "oz]{R]3l]]B#50es6O4tL23Etr3c10_F4TD2".equals(encrypt(getArray(transform, 0, 5), 2) + encrypt(getArray(transform, 1, 4), 1) + encrypt(getArray(transform, 2, 3), 0));
    }
}
