def calculate_percentage(marks):
    total_marks = sum(marks)
    percentage = (total_marks / (len(marks) * 100)) * 100
    return total_marks, percentage


def display_result(name, class_name, section, total_marks, percentage):
    print("Name:", name)
    print("Class:", class_name)
    print("Section:", section)
    print("Total Marks:", total_marks)
    print("Percentage:", percentage)


def student_details():
    name = input("Enter student name: ")
    class_name = input("Enter class: ")
    section = input("Enter section: ")

    marks = []
    for i in range(5):
        subject_marks = float(input("Enter marks for Subject {}: ".format(i+1)))
        marks.append(subject_marks)

    total_marks, percentage = calculate_percentage(marks)
    display_result(name, class_name, section, total_marks, percentage)


student_details()
