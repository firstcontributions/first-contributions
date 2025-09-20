public class Grade {
    public static String getLetterGrade(int score) {
        if (score >= 90) return "A";
        else if (score >= 80) return "B";
        else if (score >= 70) return "C";
        else if (score >= 60) return "D";
        else return "F";
    }

    public static boolean isPass(int score) {
        return score >= 60;
    }

    public static void main(String[] args) {
        System.out.println("Grade: " + getLetterGrade(85));
        System.out.println("Pass: " + isPass(85));
    }
}
