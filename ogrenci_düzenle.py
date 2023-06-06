import sqlite3

conn = sqlite3.connect("students.db") 
cursor = conn.cursor()

def student_edit ():
   
    edit_input = input("Düzenlemek istediğiniz öğrencinin ID'sini sini giriniz:  ")

    
    edit_input = " "  
    cursor.execute("SELECT * FROM students WHERE id = ?", (edit_input,))
    ogrenci = cursor.fetchone()

    
    first_name = input("Öğrenci adı giriniz: ")
    last_name = input("Öğrenci'nin soyadını giriniz: ")
    age = input("Öğrenci'nin yaşını giriniz: ")
    gender = input("Öğrenci'nin cinsiyetini giriniz: ")
    id = input("Öğrenci'nin id'sini giriniz: ")


    cursor.execute("UPDATE students SET first_name = ?, last_name = ?, age = ?, gender WHERE id=?", (first_name, last_name, age, gender, id))
    conn.commit()



    print("Öğrenci düzenlendi.")

    conn.commit()
    conn.close()