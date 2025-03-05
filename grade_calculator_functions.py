def get_student_score():
    """Handles user input to obtain the student's score."""
    score = input("Please enter your score: ")
    try:
        score = float(score)
        return score
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_student_score()  

def calculate_grade(score):
    """Determines the letter grade based on the given score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == "__main__":
    score = get_student_score()  
    grade = calculate_grade(score)  
    print(f"Your grade is: {grade}")