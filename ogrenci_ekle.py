import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()


def student_add():

    while True:
        name = input("Öğrencinin ismini girin: ")
        if name.isalpha():
             break
        else:
            print("Lütfen sadece harf giriniz.")
        
    while True:
        last_name = input("Öğrencinin soyad'ını girin: ")
        if last_name.isalpha():
            break
        else:
            print("Lütfen sadece harf giriniz.")
            
    while True:
        age= input("Öğrencinin yaş'ını girin: ")
        if age.isalpha():
            break
        else:
            print("Lütfen sadece sayı giriniz.")
                
    while True:
        gender = input("Öğrenci'nin cinsiyet'ini girin: ")
        if gender.isalpha():
            break
        else:
            print("Lütfen sadece harf giriniz.")


    cursor.execute(
        "INSERT INTO students (first_name, last_name, age, gender) VALUES (?, ?, ?, ?)",
        (name, last_name, age, gender)
    )

    conn.commit()  # Değişiklikleri veritabanına kaydet

    print("Öğrenci eklenmiştir")




conn.close()
