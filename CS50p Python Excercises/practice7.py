def main():
    students = {"Alice": [85, 90, 78], "Bob": [88,76,92], "Charlie": [90, 87, 85]}
    students["Alice"].append(95)
    students["David"] = [80, 85, 88]
    students.pop("Bob")

    highest_avg = 0
    top_student = ""

    for name, scores in students.items():
        average = sum(scores) / len(scores)
        if average > highest_avg:
            highest_avg = average
            top_student = name


        print(average, highest_avg)
    print(f"The student with the highest average is {top_student} with {highest_avg:.2f}")






main()
