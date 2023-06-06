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

    
    
    
    

    last_name = input("Öğrencinin soyad'ını girin: ")
    if last_name.isalpha():
        print(" ")
    else:
        print("Lütfen sadece harf giriniz.")
    last_name()




    age= input("Öğrencinin yaş'ını girin: ")
    if age.isalpha():
        print(" ")
    else:
        print("Lütfen sadece sayı giriniz.")
    age()      
    

    gender = input("Öğrenci'nin cinsiyet'ini girin: ")
    if gender.isalpha():
        print(" ")
    else:
        print("Lütfen sadece harf giriniz.")
    gender()
    

    cursor.execute(
        "INSERT INTO students (first_name, last_name, age, gender) VALUES (?, ?, ?, ?)",
        (name, last_name, age, gender)
    )

    conn.commit()  # Değişiklikleri veritabanına kaydet

    print("Öğrenci eklenmiştir")




conn.close()
