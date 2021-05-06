def studentData():
    studentList = []
    students = int(input('How many students do you have?:'))
    for i in range(0, students, 1):
        name = input('What is the students name?:')
        grade = int(input('What is the students grade?:'))
        course = input('What class is the student in?:')
        studentList.append({
            "name": name,
            "grade": grade,
            "course": course,
        })
    for student in studentList:
        print('Name: ' + student["name"]+', ' + 'Grade: ' + str(student["grade"])+', ' + 'Course: ' + student["course"])
studentData()

