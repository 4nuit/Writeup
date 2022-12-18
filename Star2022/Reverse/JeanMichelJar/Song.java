package chall;

import java.util.Scanner;
/* loaded from: Song.class */
public class Song {
    public static void main(String[] strArr) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("J'aime le java mais seul une personne qui adore le java connait le mot de passe:");
        if ("6_OTf;Da\"ATDB>\u001fO;]Hh".equals(hide(scanner.nextLine()))) {
            System.out.println("Tu as le mot de passe mais as tu écouté la chanson ?");
        } else {
            System.out.println("Fan de python");
        }
    }

    static String hide(String str) {
        String str2 = "";
        for (int i = 0; i < str.length(); i++) {
            str2 = str2 + ((char) (str.charAt(i) + ("GORFOU".charAt(i % "GORFOU".length()) - 'd')));
        }
        return str2;
    }
}
