import sqlite3

conn = sqlite3.connect("students.db") 
cursor = conn.cursor()

def student_edit ():
   
    edit_input = input("Düzenlemek istediğiniz öğrencinin ID'sini sini giriniz:  ")

    
    edit_input = " "  
    cursor.execute("SELECT * FROM students WHERE id = ?", (edit_input,))
    ogrenci = cursor.fetchone()

    
    while True:
        first_name = input("Öğrencinin yeni ismini girin: ")
        if first_name.isalpha():
             break
        else:
            print("Lütfen sadece harf giriniz.")
        
    while True:
        last_name = input("Öğrencinin yeni soyad'ını girin: ")
        if last_name.isalpha():
            break
        else:
            print("Lütfen sadece harf giriniz.")
            
    while True:
        age= input("Öğrencinin yeni yaş'ını girin: ")
        if age.isdigit():
            break
        else:
            print("Lütfen sadece sayı giriniz.")
                
    while True:
        gender = input("Öğrenci'nin yeni cinsiyet'ini girin: ")
        if gender.isalpha():
            break
        else:
            print("Lütfen sadece harf giriniz.")

    id = print("Öğrencinin yeni veya eski id'sini giriniz")



    cursor.execute("UPDATE students SET first_name = ?, last_name = ?, age = ?, gender = ? WHERE id=?", (first_name, last_name, age, gender, id))
    conn.commit()



    print("Öğrenci düzenlendi.")

    conn.commit()
    conn.close()