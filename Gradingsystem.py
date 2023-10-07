def assign_grade(score):
    """Assigns a grade based on the score."""
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid Score'

def main():
    try:
        score = float(input("Enter the student's score (0-100): "))
        grade = assign_grade(score)
        if grade == 'Invalid Score':
            print(grade)
        else:
            print(f"The grade for a score of {score} is: {grade}")
    except ValueError:
        print("Please enter a valid numeric score.")

if __name__ == "__main__":
    main()
