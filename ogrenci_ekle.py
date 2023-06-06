import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()


def student_add():
    first_name = input("Öğrenci adı giriniz: ")
    last_name = input("Öğrenci'nin soyadını giriniz: ")
    age = input("Öğrenci'nin yaşını giriniz: ")
    gender = input("Öğrenci'nin cinsiyetini giriniz: ")

    cursor.execute(
        "INSERT INTO students (first_name, last_name, age, gender) VALUES (?, ?, ?, ?)",
        (first_name, last_name, age, gender)
    )

    conn.commit()  # Değişiklikleri veritabanına kaydet

    print("Öğrenci eklenmiştir")




conn.close()
