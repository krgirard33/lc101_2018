def calculate_gpa(grades):
    total_quality_score = 0
    total_credits = 0

    for dictionary in grades:
        total_quality_score += dictionary["grade"]*dictionary["credits"]
        total_credits += dictionary["credits"]

    print(total_quality_score/total_credits)

def main():
    grades = []

    while True:
        grade = float(input("Enter a grade between 1-4"))
        credits = int(input("how many credits was the class?"))
        grades.append({"grade":grade, "credits":credits})

        more_entries = input("Got more?")
        if more_entries == 'n':
            break

if __name__ == '__main__':
    main()

