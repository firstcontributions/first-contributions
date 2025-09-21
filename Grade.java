package first_contributions;

public class Grade {

    // Return letter grade based on numeric score
    public String getLetterGrade(double score) {
        if (score >= 90) return "A";
        else if (score >= 80) return "B";
        else if (score >= 70) return "C";
        else if (score >= 60) return "D";
        else return "F";
    }

    // Return pass/fail based on score
    public boolean isPass(double score) {
        return score >= 60;
    }
}

