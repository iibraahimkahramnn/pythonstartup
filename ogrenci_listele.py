import sqlite3

def student_list():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print(students)

    for student in students:
        print(f"id: {student[0]}, Ad: {student[1]}, Soyad: {student[2]}, Yaş: {student[3]}, Cinsiyet: {student[4]}")

    conn.close()


