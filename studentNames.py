# רשימה לשמירת שמות התלמידים
students = []

print("Enter the names of the students. To stop, type '='.")

# לולאה לקליטת השמות
while True:
    name = input("Enter student name: ")  # קולט שם תלמיד
    if name == "=":  # בדיקה אם המשתמש הקליד "=" כדי לעצור
        break  # יציאה מהלולאה אם הוכנס סימן =
    students.append(name)  # הוספת השם לרשימת התלמידים

# הדפסת כל שמות התלמידים
print("\nList of students:")
for student in students:
    print(student)
