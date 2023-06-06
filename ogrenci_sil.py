import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()


def student_delete():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = input("Silmek istediğiniz Öğrencinin ID'sini girin.: ")

    cursor.execute("DELETE FROM students WHERE id = ?",(student_id,))

    print("Öğrenci silinmiştir.")

    conn.commit()

    conn.close()

