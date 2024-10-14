def check_grade(grade):
    if grade >= 90 and grade <= 100:
        return("Excellent! You did a great job!")
    elif grade >= 80 and grade <= 89:
        return("Good job! Keep it up!")
    elif grade >= 70 and grade <= 79:
        return("You passed, but there's room for improvement.")
    elif grade >= 1 and grade <= 69:
        return("You failed. better luck next time.")
    else:
        return("invalid input")

user = int(input("input your grade: "))
print(check_grade(user))