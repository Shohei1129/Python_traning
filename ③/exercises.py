grades = {
    'class1': [88, 82, 91, 74, 86, 92],
    'class2': [78, 88, 85, 89, 90, 92],
    'class3': [95, 90, 91, 92, 88, 86],
    'class4': [70, 72, 75, 73, 68, 72],
}

def calculate_averages(grades):
    averages = {}
    for class_name, class_grades in grades.items():
        averages[class_name] = sum(class_grades) / len(class_grades)
    return averages


averages = calculate_averages(grades)
for class_name, average in averages.items():
    print(f"The average grade of {class_name} is: {average:.2f}")
