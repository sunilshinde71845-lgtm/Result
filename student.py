
import sys

def student(marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    average = total / 3
    percentage = total / 300 * 100

    print("Student Result")
    print("Marks:", marks1, marks2, marks3)
    print("Total Marks:", total)
    print("Average:", average)
    print("Percentage:", percentage)

    return total, average, percentage

if __name__ == "__main__":
    marks1 = int(sys.argv[1])
    marks2 = int(sys.argv[2])
    marks3 = int(sys.argv[3])
    student(marks1, marks2, marks3)
